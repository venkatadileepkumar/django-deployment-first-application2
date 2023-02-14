from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f11(request):
    return HttpResponse("<h1>Hello User...!!! HAve A Nice Day</h1><hr/>");
