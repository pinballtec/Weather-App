from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.


def main(request):
    app_id = 'cd36bd3fa9df49ec3afeca695c290496'

    link = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id

    city = 'Warsaw'

    resp = requests.get(link.format(city)).json()

    city_info = {
        'city': city,
        'temp': resp["main"]["temp"],
        'icon': resp["weather"][0]["icon"]
    }

    # print(resp.text)

    context = {'info': city_info}

    return render(request, 'weather_app/index.html', context)