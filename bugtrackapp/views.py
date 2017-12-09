from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def rschome(request):
    return HttpResponse('rsc home')