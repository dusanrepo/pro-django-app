from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  msg = 'My Message'
  return render(request, 'index.html', {'message': msg})

def about(request):
  return HttpResponse("<h1>About!</h1>")

def contact(request):
  return HttpResponse("<h1>Contact Us!</h1>")