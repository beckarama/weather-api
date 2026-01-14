# Weather API 
<img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white"/><img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/><img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=Pydantic&logoColor=white"/>
<img width="3000" height="750" alt="PoweredByVC-WeatherLogo-RoundedRectBlack" src="https://github.com/user-attachments/assets/98646418-d761-4512-8a3b-8050be4bfb9c" />

Production-style Weather API that fetches data from Visual Crossing Weather, normalizes and validates responses using Pydantic, and serves clean JSON schemas. Frequently requested data is cached with Redis to reduce latency and external API usage. The service includes rate limiting and health checks to ensure reliability.
<br><br/>
This project was built as part of a backend engineering learning roadmap inspired by roadmap.sh.  
https://roadmap.sh/projects/weather-api-wrapper-service

# API Endpoints 📍
* `GET /{city}` - Returns current weather data for a given city.

* `GET /api/health` - Returns status of API.

# Tech Stack 📚
* Framework: FastAPI
* Language: Python
* Validation: Pydantic
* Caching: Redis
* Rate Limiting: SlowAPI
* HTTP Client: Requests

## Installation ⚙️

### Prerequisites
- **Python 3.10+**
- **Redis** (local installation or Docker)
- **Visual Crossing Weather API Key**

---

1. **Clone the repository**
```bash
git clone https://github.com/your-username/weather-api.git
cd weather-api
```
2. **Create and activate a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
```
3. **Install dependencies**
   
```bash 
pip install -r requirements.txt
```

5. **Environment variables**
Create a ```.env``` file in the project root:

```
VISUAL_CROSSING_API_KEY=your_api_key_here
REDIS_HOST=localhost
REDIS_PORT=6379
```

5. **Start Redis**
```bash
redis-server
```

7. **Run the API**
```bash
uvicorn main:app --reload
```

9. **Test the API**
Example Request:

```bash 
curl http://127.0.0.1:8000/London
```

Health check:

```bash
curl http://127.0.0.1:8000/api/health
```

