from django.shortcuts import render
from django.http import HttpResponse
from .multiplication import mul
# Create your views here.
def index(request):
    return HttpResponse(mul)
