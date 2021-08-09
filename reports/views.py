from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from profiles.models import Profile

from .forms import ReportForm
from .models import Report
from .utils import get_report_image


class ReportListView(ListView):
    model = Report
    template_name = "reports/main.html"


class ReportDetailView(DetailView):
    model = Report
    template_name = "reports/detail.html"


def create_report_view(request):
    form = ReportForm(request.POST or None)
    if request.is_ajax():
        # name = request.POST.get("name")
        # remarks = request.POST.get("remarks")
        image = request.POST.get("image")
        img = get_report_image(image)
        author = Profile.objects.get(user=request.user)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author
            instance.save()

        # Report.objects.create(name=name, remarks=remarks, image=img, author=author)
        return JsonResponse({"msg": "send"})

    return JsonResponse({})
