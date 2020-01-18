from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login'),
    path('register/', views.register, name='register'),
    #path('login/', user_views.LoginView.as_view(template_name=''), name='login'),
    #path('logout/', user_views.LogoutView.as_view(template_name=''), name='logout'),
    path('home', views.home, name='home'),
    path('checklist', views.checklist, name='checklist'),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]