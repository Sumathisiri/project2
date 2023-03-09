from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def MSD(request):
    return HttpResponse('<h1>MSD....</h1>')

