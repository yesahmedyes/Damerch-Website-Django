from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('payment/', views.payment, name="payment"),
    path('order/', views.order, name="order"),
    path('order/<id>', views.order_success, name="order_success"),
    path('order/status/<id>', views.order_status, name="order_status"),
]
