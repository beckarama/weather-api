from pydantic import BaseModel

class WeatherResponse(BaseModel):
    location: str
    description: str
    temperature: float
    max_temperature: float
    min_temperature: float
    precipitation: float
    humidity: float
    wind_speed: float
    wind_direction: float
    snow: float
    snow_depth: float
    sunrise: str
    sunset: str
    alerts: list

