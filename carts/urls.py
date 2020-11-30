from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.cart_home, name="cart"),
    path('update/', views.cart_update, name="cart_update"),
    path('delete/', views.cart_delete, name="cart_delete"),
]

