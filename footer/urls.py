from django.urls import path
from footer import views

app_name = 'footer'

urlpatterns = [
    path('refund/', views.refund_page, name="refund"),
    path('about/', views.about_page, name="about"),
    path('privacy-statement/', views.ps_page, name="ps"),
    path('terms-of-service/', views.tos_page, name="tos"),
    path('faq/', views.faq_page, name="faq"),
    path('contact/', views.contact_page, name="contact"),
    path('career/', views.career_page, name="career"),
]
