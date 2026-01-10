from pydantic import BaseModel
from typing import Optional

class WeatherResponse(BaseModel):
    location: str
    description: str
    temperature: float
    precipitation: float
    humidity: float
    windspeed: float
    winddirection: float
    snow: Optional[float]
    snowdepth: Optional[float]
    alerts: list

