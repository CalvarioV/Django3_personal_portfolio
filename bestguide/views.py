from django.shortcuts import render


# Create your views here.
def besthome(request):
    return render(request, 'bestguide/besthome.html')


def testing(request):
    return render(request, 'bestguide/testing2.html')


def motd(request):
    return render(request, 'bestguide/testing.html')
