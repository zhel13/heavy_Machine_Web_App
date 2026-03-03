from django.urls import path

from part.views import dashboard
urlpatterns = [
    path('', dashboard, name='dashboard'),
]