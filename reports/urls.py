from django.urls import path

from .views import ReportListView  # noqa

from .views import ReportDetailView, create_report_view, render_pdf_view  # isort:skip

app_name = "reports"

urlpatterns = [
    path("", ReportListView.as_view(), name="main"),
    path("save/", create_report_view, name="create-report"),
    path("<pk>/", ReportDetailView.as_view(), name="detail"),
    path("<pk>/pdf/", render_pdf_view, name="pdf"),
]
