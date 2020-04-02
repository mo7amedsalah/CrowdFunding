from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Image, Project, Comment, Donation


# Create your views here.
@login_required
def profile(request):
    context = {}

    user_projects = Project.objects.filter(owner=request.user)  # get user projects
    donations = Project.objects.filter(donations__user=request.user)  # get user projects
    context['user_projects'] = user_projects
    context['donations'] = donations

    return render(request, "users/profile.html", context)
