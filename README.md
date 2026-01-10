# Weather API 
<img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white"/><img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/><img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=Pydantic&logoColor=white"/>
<img width="3000" height="750" alt="PoweredByVC-WeatherLogo-RoundedRectBlack" src="https://github.com/user-attachments/assets/98646418-d761-4512-8a3b-8050be4bfb9c" />

Production-style Weather API that fetches data from Visual Crossing Weather, normalizes and validates responses using Pydantic, and serves clean JSON schemas. Frequently requested data is cached with Redis to reduce latency and external API usage. The service includes rate limiting and health checks to ensure reliability.

This project was built as part of a backend engineering learning roadmap inspired by roadmap.sh.

https://roadmap.sh/projects/weather-api-wrapper-service

# API Endpoints 📍

### GET /{city}
Returns current weather data for a given city.

(Ex. GET London,UK)

### GET /health
Returns status of API.


# Tech Stack 📚
* Framework: FastAPI
* Language: Python
* Validation: Pydantic
* Caching: Redis
* Rate Limiting: SlowAPI
* HTTP Client: Requests
# Blueprint 📝
<img width="2048" height="1059" alt="weather-api-f8i1q" src="https://github.com/user-attachments/assets/b7ac855b-a3aa-418d-b2c9-a06a2d2d24d1" />

