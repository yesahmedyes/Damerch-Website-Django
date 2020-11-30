from django.urls import path
from . import views

app_name = 'myauth'

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('artist/', views.artist_login, name="artist"),
    path('<redirected>/login', views.login_landing, name="login_landing"),
    path('register/', views.register_page, name="register"),
    path('register/myauth/<id>', views.register_success, name="register_success"),
    path('logout/', views.logout_page, name="logout"),
    path('reset/', views.reset_main, name="reset"),
    path('reset/<id>', views.reset_page, name="reset_page"),
]
