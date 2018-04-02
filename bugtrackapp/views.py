from django.shortcuts import render
from .models import Bugtrack
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_id(request,post_id):
    blog_obj = Post.objects.get(id=post_id)
    body_contain = blog_obj.body.split("^")
    context = {'blog':blog_obj,'body_contain':body_contain}
    return render(request,'blog_id.html',context)

def rschome(request):
    blog_obj = Post.objects.all().order_by('-id')[:9]
    page = request.GET.get('page', 1)

    paginator = Paginator(blog_obj, 3)
    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        blog_page = paginator.page(1)
    except EmptyPage:
        blog_page = paginator.page(paginator.num_pages)

    context = {'blog_obj':blog_obj,'blog_page':blog_page}
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
