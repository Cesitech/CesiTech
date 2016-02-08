from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import *

# Create your views here.
def index(request):
    return render(request, 'administration/index.html', {'date':datetime.now()})
