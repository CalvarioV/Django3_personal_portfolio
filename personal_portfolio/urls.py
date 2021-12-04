"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vibes, name='vibes'),
    path('portfolio/', views.home, name='portfolio'),
    path('blog/', include('blog.urls')),
    # mothers day project
    path('fabis/', views.fabis, name='fabis'),
    #bestbuy guide
    path('bestguide/', include('bestguide.urls')),
    #amys nails page
    path('amyloks/', views.amynails, name='amynails'),
    #javascript bs
    path('cool/', views.particles, name='particles'),
    #2nd portfolio page
    path('about/', views.about, name='about'),
    path('resume', views.resume, name='resume')




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
