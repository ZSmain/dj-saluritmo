from django.shortcuts import render
from django.http import JsonResponse

from .utils import fetch_weather_data


def home(request):
    if (
        request.headers.get("x-requested-with") == "XMLHttpRequest"
        and request.GET.get("action") == "fetch_weather"
    ):
        weather_data = fetch_weather_data()
        return JsonResponse(weather_data)
    # TODO: Calculate actual streak from user data
    context = {
        "page_title": "Home",
        "show_streak": True,
        "streak_count": 5,  # This should be calculated from actual data
    }
    return render(request, "core/home.html", context)


def fetch_weather(request):
    weather_data = fetch_weather_data()
    return JsonResponse(weather_data)


def medications(request):
    context = {"page_title": "Medications", "show_streak": False}
    return render(request, "core/medications.html", context)


def history(request):
    context = {"page_title": "History", "show_streak": False}
    return render(request, "core/history.html", context)


def settings(request):
    context = {"page_title": "Settings", "show_streak": False}
    return render(request, "core/settings.html", context)
