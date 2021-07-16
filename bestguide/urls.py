from django.urls import path
from . import views

app_name = 'bestguide'

urlpatterns = [
    path('', views.besthome, name='besthome'),
    path('testing', views.testing, name='testing'),


]