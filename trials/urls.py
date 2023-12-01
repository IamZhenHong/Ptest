from django.urls import path
from .views import index, result, landing

urlpatterns = [
    path('', landing, name='landing'),
    path('index/', index, name='index'),
    path('result/', result, name='result'),
]