from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World INdex")

def home(request):
    return HttpResponse("Hello, World HOme")
