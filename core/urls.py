from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("medications/", views.medications, name="medications"),
    path("history/", views.history, name="history"),
    path("settings/", views.settings, name="settings"),
    path("fetch_weather/", views.fetch_weather, name="fetch_weather"),
]
