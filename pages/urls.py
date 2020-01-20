from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login'),
    
    path('home', views.home, name='home'),
    path('checklist', views.checklist, name='checklist'),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]