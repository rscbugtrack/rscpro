from django.shortcuts import render

from django.http import HttpResponse

from .models import Bugtrack
# Create your views here.


def rschome(request):
    context = {}
    return render(request,'rschome.html',context)


def rscbugtrack(request):

    rscbugs = Bugtrack.objects.all()

    context = { 'rscbugs' : rscbugs}
    return render(request,'rscbugtrack.html',context)