from django.shortcuts import render


def home_view(request):
    hello = "hello from view"
    return render(request, "sales/main.html", {"hello": hello})
