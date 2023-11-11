from django.shortcuts import render
import random
from .models import Project
from django.http import HttpResponse

fortuneList = [
    "Your dreams are the key to unlocking your true potential.",
    "Diamonds are a symbol of your inner strength and resilience.",
    "The universe has great things in store for you. Trust the journey.",
    "Your dreams are the stars guiding your destiny.",
    "The universe conspires to bring you closer to your dreams.",
    "Your visions are the bridge between imagination and reality.",
    "The magic you're looking for, is in the work you're avoiding.",
]

def home(request):

    return render(request, 'portfolio/home.html')


def fabis(request):
    return render(request, 'portfolio/fabis.html')


def amynails(request):
    return render(request, 'portfolio/amynails.html')


def vibes(request):
    fortune = random.choice(fortuneList)
    context = {"fortune": fortune}
    return render(request, 'portfolio/about.html', context)


def particles(request):
    return render(request, 'portfolio/particles.html')


def about(request):
    return render(request, 'portfolio/vibes.html')


def resume(request):
    return render(request, 'portfolio/resume.html')


def vboard(request):
    return render(request, 'portfolio/vboard.html')