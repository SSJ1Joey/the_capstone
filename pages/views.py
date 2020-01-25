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

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')





