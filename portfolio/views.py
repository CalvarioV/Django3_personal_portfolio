from django.shortcuts import render
from .models import Project
from django.http import HttpResponse


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def fabis(request):
    return render(request, 'portfolio/fabis.html')

def amynails(request):
    return render(request, 'portfolio/amynails.html')
