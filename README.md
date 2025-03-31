# Weather App

A Django-based weather application that displays weather information using the WeatherAPI.com service.

## Features

- Real-time weather information
- Temperature in Celsius
- Weather description with icons
- Humidity
- Wind speed
- Feels like temperature
- Atmospheric pressure
- Responsive design
- Modern UI with Bootstrap

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/kstubhieeee/weather-app-django.git
cd weather-app-django
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your WeatherAPI.com API key:
```
WEATHERAPI_KEY=your_api_key_here
```
You can get a free API key from [WeatherAPI.com](https://www.weatherapi.com/)

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Usage

1. Enter a city name in the search box
2. Click "Get Weather" to see the current weather information
3. The app will display:
   - Current temperature
   - Weather condition with icon
   - Humidity percentage
   - Wind speed in km/h
   - "Feels like" temperature
   - Atmospheric pressure

## Technologies Used

- Django 5.0.2
- Python 3.x
- Bootstrap 5.3.0
- WeatherAPI.com API
- python-dotenv for environment variables

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Weather data provided by [WeatherAPI.com](https://www.weatherapi.com/)
- Icons and UI elements from Bootstrap 