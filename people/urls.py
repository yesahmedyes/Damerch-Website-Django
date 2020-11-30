from django.urls import path
from . import views


app_name = 'people'

urlpatterns = [
    path('', views.people_list, name='list'),
    path('<slug>', views.people_detail, name='detail'),
    path('<slug>/admin', views.artist_page, name='admin'),
]
