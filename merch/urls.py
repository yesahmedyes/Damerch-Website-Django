from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace="home")),
    path('nav/', views.nav, name="nav"),
    path('footer/', include('footer.urls', namespace="footer")),
    path('products/', include('products.urls', namespace="products")),
    path('search/', include('search.urls', namespace="search")),
    path('cart/', include('carts.urls', namespace="carts")),
    path('subscribe/', include('subscribe.urls', namespace="subscribe")),
    path('people/', include('people.urls', namespace="people")),
    path('checkout/', include('checkout.urls', namespace="checkout")),
    path('myauth/', include('myauth.urls', namespace="myauth")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'merch.views.my_404'
handler500 = 'merch.views.my_404'
handler400 = 'merch.views.my_404'
