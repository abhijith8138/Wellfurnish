from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def home(request):
    return render(request,'home.html')
def bed(request):
    bed= Bed.objects.all()
    return render(request,'bed.html',{'bed':bed})
def curtains(request):
    curtains = Curtains.objects.all()
    return render(request,'curtains.html',{'curtains':curtains})
def doorlocks(request):
    doorlocks = Doorlock.objects.all()
    return render(request,'doorlocks.html',{'doorlock':doorlocks})
def sofa(request):
    sofa = Sofa.objects.all()
    return render(request,'sofa.html',{'sofa':sofa})

def blinds(request):
    blinds = Blinds.objects.all()
    return render(request,'blinds.html',{'blinds':blinds})