from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse, Http404

# Create your views here.


def home(request):
    years = YearbookData.objects.values('year').order_by('-year').distinct()
    return render(request, 'yearbook/home.html', {'years': years})

def yearlist(request):
    regnos = None
    year = ""
    namee = ""
    if request.method == 'GET':
        year = request.GET['year']
        regnos = YearbookData.objects.values('regno', 'name', 'photo').filter(year=year).order_by('regno').distinct()

    if request.method == 'POST':
        name = request.POST['name']
        namee = name
        regnos = YearbookData.objects.values('regno', 'name', 'photo').filter(name__contains=name).order_by('regno').distinct()
        year = None

    return render(request, 'yearbook/yearlist.html', {'regnos': regnos ,'year': year, 'name': namee})

def alumni(request):
    profile = None
    if request.method == 'GET':

        regno = request.GET['regno']
        try:
            profile = YearbookData.objects.get(regno=regno)
        except:
            messages.error(request, "There is no entry for this registration number")
            return render(request, 'yearbook/yearlist.html')

    return render(request, 'yearbook/alumni.html', {'profile': profile})

def uploadData(request):
    form = YearbookDataForm()

    if request.method == 'POST':

        string = request.POST['links']
        r = string.find("testing123xyz")
        regno = request.POST['regno']

        st = False
        if r!=-1:
            st = True

        error = 0
        msg = "invalid entries"
        duplicate = YearbookData.objects.filter(regno=regno).count()
        if duplicate!=0:
            error = error + 1
            msg = "The entry for this registration number already exists"

        form = YearbookDataForm(request.POST, request.FILES)
        if form.is_valid() and error==0:
            form.save()
            if st:
                YearbookData.objects.filter(regno=regno).update(links="")
            return render(request, 'yearbook/success.html', {'regno': regno})
        else:
            messages.error(request, msg)
            return redirect('upload')

    return render(request, 'yearbook/upload.html', {'form': form})


