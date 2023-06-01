from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request): #обязательно писать request - браузер присылает реквест, мы ее обрабатываем
    return HttpResponse('<h1>About site<h1>')

def login(request):
    return HttpResponse('Page login')

def contacts(request):
    return HttpResponse('Contacts')