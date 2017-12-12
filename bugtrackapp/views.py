from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def rschome(request):
    context = {}
    return render(request,'rschome.html',context)

def rscbugtrack(request):
    context = {}
    return render(request,'rscbugtrack.html',context)