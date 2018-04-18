from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, World INdex")

def home(request):
    return render(request, "templates/index.html", {})
