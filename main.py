from models import WeatherResponse
import requests, os, json

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from redis import Redis

load_dotenv()
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
API_KEY = os.getenv("WEATHER_API_KEY")
PARAMETERS = {
    "key": API_KEY
}

# Create API using Limiter to implement rate limiting and Redis for caching data
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
cache = Redis(host="localhost", port=6379, decode_responses=True)


@app.get("/weather/{city}", response_model=WeatherResponse)
@limiter.limit("10/minute")
@limiter.limit("200/day")
def get_weather(request: Request, city: str):
    # Checks cache for data
    city_norm = city.strip().lower()
    cache_name = f"weather:{city_norm}"
    cached_data = cache.get(cache_name)
    if cached_data:
        print("returned from cached_data!")
        return json.loads(cached_data)

    # Sends GET request to visualcrossing. Error Handling
    url = f"{BASE_URL}/{city_norm}"
    try:
        response = requests.get(url, params=PARAMETERS, timeout=10)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Invalid location or API error")
        data_json = response.json()

    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=502, detail="Failed to connect to weather provider.")

    # Sets data to cache. Expires after 5 minutes
    cache.set(cache_name, json.dumps(data_json), ex=300)

    # Validate JSON
    return WeatherResponse(
        location=data_json["resolvedAddress"],
        description=data_json["days"][0]["description"],
        temperature=data_json["days"][0]["temp"],
        precipitation=data_json["days"][0]["precip"],
        humidity=data_json["days"][0]["humidity"],
        windspeed=data_json["days"][0]["windspeed"],
        winddirection=data_json["days"][0]["winddir"],
        alerts=data_json["alerts"],
        snow=data_json["days"][0]["snow"],
        snowdepth=data_json["days"][0]["snowdepth"]
    )

@app.get("/health")
def health():
    redis_status = True
    api_key_status = bool(API_KEY)
    try:
        cache.ping()
    except Exception:
        redis_status = False


    return {
        "redis": "ok" if redis_status else "down",
        "weather_api_key": "valid" if api_key_status else "missing"
    }