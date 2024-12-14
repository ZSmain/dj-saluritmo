from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def medications(request):
    return render(request, "core/medications.html")


def history(request):
    return render(request, "core/history.html")


def settings(request):
    return render(request, "core/settings.html")
