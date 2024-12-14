from django.shortcuts import render


def home(request):
    # TODO: Calculate actual streak from user data
    context = {
        "page_title": "Home",
        "show_streak": True,
        "streak_count": 5,  # This should be calculated from actual data
    }
    return render(request, "core/home.html", context)


def medications(request):
    context = {"page_title": "Medications", "show_streak": False}
    return render(request, "core/medications.html", context)


def history(request):
    context = {"page_title": "History", "show_streak": False}
    return render(request, "core/history.html", context)


def settings(request):
    context = {"page_title": "Settings", "show_streak": False}
    return render(request, "core/settings.html", context)
