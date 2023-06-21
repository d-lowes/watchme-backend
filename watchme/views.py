from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# request handler

# URLConf
def display_shows(request):
    """"""
    return HttpResponse('Call API here and display shows.')