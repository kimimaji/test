from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    return HttpResponse('Hello, Miki!')

def index_page(request):
    return render( request,'hello/index.html')