from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checklist', views.checklist, name='checklist'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery2', views.gallery2, name='gallery2'),
    path('gallery3', views.gallery3, name='gallery3'),
    path('gallery4', views.gallery4, name='gallery4'),
    path('gallery5', views.gallery5, name='gallery5'),
    path('gallery6', views.gallery6, name='gallery6'),
]