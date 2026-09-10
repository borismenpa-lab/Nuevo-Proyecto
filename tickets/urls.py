from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo_ticket, name='demo_ticket'),
]