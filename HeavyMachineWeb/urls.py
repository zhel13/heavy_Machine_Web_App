"""
URL configuration for HeavyMachineWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
import profile
from signal import pthread_sigmask

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',  include('common.urls')),

    path('admin/', admin.site.urls),
    path('profile/', include('user_profile.urls')),
    path('machine/', include('machine.urls')),
    path('order/', include('order.urls')),
    path('part', include('part.urls')),
]
