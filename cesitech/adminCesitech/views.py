from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'admin/index.html', {'date':datetime.now()})
