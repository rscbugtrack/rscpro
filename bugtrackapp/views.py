from django.shortcuts import render

from django.http import HttpResponse

from .models import Bugtrack
# Create your views here.


def rschome(request):
    context = {}
    return render(request,'home.html',context)

def contactus(request):
    context = {}
    return render(request,'contact_us.html',context)

def rscbugtrack(request):

    rscbugs = Bugtrack.objects.all()

    context = { 'rscbugs' : rscbugs}
    return render(request,'rscbugtrack.html',context)
def aboutus(request):


    context = {}
    return render(request,'aboutus.html',context)

def ourteam(request):


    context = {}
    return render(request,'ourteam.html',context)
