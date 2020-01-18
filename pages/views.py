from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def home(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html' )

def register(request):
    return render(request, 'pages/register.html')

def checklist(request):
    return render(request, 'pages/checklist.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')



