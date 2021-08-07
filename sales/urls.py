from django.urls import path

from .views import SaleDetailView, SaleListView, home_view

app_name = "sales"

urlpatterns = [
    path("", home_view, name="home"),
    path("list/", SaleListView.as_view(), name="list"),
    path("list/<pk>/", SaleDetailView.as_view(), name="detail"),
]
