from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'resume/index.html')

def blog(request):
    return HttpResponse('This is a blog page')
