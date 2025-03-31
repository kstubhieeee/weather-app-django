# Weather App

A Django-based weather application that displays weather information using the OpenWeatherMap API.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ in your browser

## Features
- Current weather information
- Temperature in Celsius
- Weather description
- Humidity
- Wind speed 