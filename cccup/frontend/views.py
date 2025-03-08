from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, *args, **kwargs):
    context = {
        'message': 'hello from django'
    }
    return render(request, 'frontend/index.html', context)