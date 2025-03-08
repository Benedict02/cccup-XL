from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, *args, **kwargs):
    context = {
        'message': 'hello admin from django'
    }
    return render(request, 'admin/index.html', context)