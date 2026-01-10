from pydantic import BaseModel

class WeatherResponse(BaseModel):
    location: str
    description: str
    temperature: float
    precipitation: float
    humidity: float
    windspeed: float
    winddirection: float
    snow: float
    snowdepth: float
    alerts: list

