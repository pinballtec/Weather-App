from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.http import HttpResponse
# Create your views here.


def main(request):
    app_id = 'cd36bd3fa9df49ec3afeca695c290496'

    link = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        resp = requests.get(link.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': resp["main"]["temp"],
            'icon': resp["weather"][0]["icon"]
        }

        all_cities.append(city_info)
    # print(resp.text)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather_app/index.html', context)


def info(request):
    return render(request, 'weather_app/info.html')


def faq(request):
    return render(request, 'weather_app/faq.html')


# def delete_item(request):
#     record = City.objects.get(id=City.name)
#     record.delete()
#     print("Record doesn't exists")