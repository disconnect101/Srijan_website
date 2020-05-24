from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    years = YearbookData.objects.values('year').order_by('-year').distinct()
    return render(request, 'yearbook/home.html', {'years': years})

def yearlist(request):
    regnos = None
    if request.method == 'GET':
        year = request.GET['year']
        regnos = YearbookData.objects.values('regno').filter(year=year).order_by('regno').distinct()

    return render(request, 'yearbook/yearlist.html', {'regnos': regnos})

def alumni(request):
    profile = None
    if request.method == 'GET':
        regno = request.GET['regno']
        profile = YearbookData.objects.get(regno=regno)

    return render(request, 'yearbook/alumni.html', {'profile': profile})
