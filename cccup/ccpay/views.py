from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, *args, **kwargs):
    return HttpResponse("This is the CCPAY page.")