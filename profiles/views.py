from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ProfileForm
from .models import Profile


@login_required
def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    confirmed = False

    if form.is_valid():
        form.save()
        confirmed = True

    context = {"profile": profile, "form": form, "confirmed": confirmed}
    return render(request, "profiles/main.html", context)
