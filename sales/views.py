from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Sale


def home_view(request):
    hello = "hello from view"
    return render(request, "sales/home.html", {"hello": hello})


class SaleListView(ListView):
    model = Sale
    template_name = "sales/main.html"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"
