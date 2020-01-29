from django.urls import path
from collection import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]