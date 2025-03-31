import requests
from django.shortcuts import render
from django.conf import settings

def get_weather(city):
    api_key = settings.WEATHERAPI_KEY
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': city,
        'aqi': 'no'  # Disable air quality data
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return None

def index(request):
    weather_data = None
    error_message = None
    
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            weather_data = get_weather(city)
            if not weather_data:
                error_message = "City not found or API error occurred."
    
    return render(request, 'weather/index.html', {
        'weather_data': weather_data,
        'error_message': error_message
    })
