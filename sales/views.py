from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .forms import SalesSearchForm
from .models import Sale


def home_view(request):
    form = SalesSearchForm(request.POST or None)
    if request.method == "POST":
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")
        print(date_from, date_to, chart_type)
    context = {"form": form}
    return render(request, "sales/home.html", context)


class SaleListView(ListView):
    model = Sale
    template_name = "sales/main.html"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"
