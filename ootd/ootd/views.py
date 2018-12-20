from django.http import HttpResponse, request
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from pyowm import OWM

def home(request):
    # model = Clothes
    API_key = '5010bcb0746e9daf22c7a1ca3de8cbce'

    owm = OWM(API_key)
    obs = owm.weather_at_place('Seoul')
    w = obs.get_weather()
    print(w.get_status())

    return render(request, "home.html",{
            "weather": w.get_status(),
            "temperature": int(w.get_temperature(unit='celsius')['temp']) })

