from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')

def home(request):
    return render(request, 'pages/index.html')

def checklist(request):
    return render(request, 'pages/checklist.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def gallery2(request):
    return render(request, 'pages/gallery2.html')

def gallery3(request):
    return render(request, 'pages/gallery3.html')

def gallery4(request):
    return render(request, 'pages/gallery4.html')

def gallery5(request):
    return render(request, 'pages/gallery5.html')

def gallery6(request):
    return render(request, 'pages/gallery6.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')





