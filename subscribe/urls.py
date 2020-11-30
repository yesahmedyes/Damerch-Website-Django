from django.urls import path
from . import views

app_name = 'subscribe'

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
]
