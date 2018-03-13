from django.shortcuts import render

from django.http import HttpResponse

from .models import Bugtrack
# Create your views here.

from blog.models import Blog,Post
def blog(request):
    blog_obj = Post.objects.all().order_by('-id')[:3]
    context = {'blog':blog_obj}
    return render(request,'blog.html',context)

def rschome(request):
    blog_obj = Post.objects.all().order_by('-id')[:3]
    context = {'blog':blog_obj}
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
