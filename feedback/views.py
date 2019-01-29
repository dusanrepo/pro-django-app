from django.shortcuts import render
from django.http import HttpResponse
from feedback.models import Feedback
from datetime import datetime

# Create your views here.
def list(request):
  s = '<h1>data list</h1>'
  for f in Feedback.objects.all():
    s += '<h2>' + str(f.id) + ' : ' + f.name + '</h2>'
  return HttpResponse(s)

def add(request):
  name = 'Kim'
  email = 'kim@test.com'
  comment = 'Hello'

  name = request.GET.get('name')
  email = request.GET.get('email')
  comment = request.GET.get('comment')

  fb = Feedback(name = name, email = email, comment = comment, createDate = datetime.now())
  fb.save()
  return HttpResponse("<h1>Add!</h1>")

def update(request):
  return HttpResponse("<h1>Update!</h1>")