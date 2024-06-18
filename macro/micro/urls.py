from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    # path('buy_now', views.buy_now, name='buy-now'),
    path('products', views.products, name= 'products'),
    path('about', views.about, name='about'),
    path('contact_success',views.contact_success, name='contact_success')
]
