from django.shortcuts import render
from django.http import HttpResponse

a = "ты дебил?!"

def test(request):
    return HttpResponse("Hello World!")

def debil():
    return a