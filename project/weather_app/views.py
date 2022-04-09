from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.


def main(request):
    app_id = ''

    context = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + app_id

    city = 'Warsaw'

    resp = requests.get(context.format(city))
    print(resp.text)

    return render(request, 'weather_app/index.html')