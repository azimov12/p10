from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func1(request):
    return HttpResponse('Function N1')

def func2(request):
    return HttpResponse('Function N2')    

def func3(request):
    return HttpResponse('Function N3')