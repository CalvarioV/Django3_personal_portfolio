from django.shortcuts import render
from .models import Project
from django.http import HttpResponse


def home(request):

    return render(request, 'portfolio/home.html')


def fabis(request):
    return render(request, 'portfolio/fabis.html')


def amynails(request):
    return render(request, 'portfolio/amynails.html')


def vibes(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/about.html', {'projects': projects})


def particles(request):
    return render(request, 'portfolio/particles.html')


def about(request):
    return render(request, 'portfolio/vibes.html')


def resume(request):
    return render(request, 'portfolio/resume.html')
