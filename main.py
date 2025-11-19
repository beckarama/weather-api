import requests, os, json
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from redis import Redis

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


@app.get("/weather/{city}")
@limiter.limit("10/minute")
@limiter.limit("200/day")
def get_weather(request: Request, city: str):
    # Checks cache for data
    cache_name = f"weather:{city}"
    cached_data = cache.get(cache_name)
    if cached_data:
        print("returned from cached_data!")
        return json.loads(cached_data)

    # Sends GET request to visualcrossing. Error Handling
    url = f"{BASE_URL}/{city}"
    try:
        response = requests.get(url, params=PARAMETERS)

        if response.status_code != 200:
            return {"error": "Invalid location or API error"}, response.status_code
        data_json = response.json()

    except requests.exceptions.ConnectionError:
        return {"Error": "Failed to connect to Weather API"}

    # Sets data to cache. Expires after 5 minutes
    cache.set(cache_name, json.dumps(data_json), ex=300)

    return data_json
