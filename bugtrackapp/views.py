from django.shortcuts import render
from .models import Bugtrack
from blog.models import Post
from bugtrackapp.forms import FeedbackForm
from bugtrackapp.models import Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.exceptions import ImproperlyConfigured

from .models import SysConfig


def send_mail(subject, message, recipients, is_html):
    """
    Sends email using predefined System Configs and Django settings
    """
    sys_configs = SysConfig.get_configs()

    if 'SITE_NAME' not in sys_configs or 'DOMAIN' not in sys_configs:
        raise ImproperlyConfigured('SITE_NAME and DOMAIN not found. It should be defined in System Configurations')

    if not hasattr(settings, 'EMAIL_HOST') or not hasattr(settings, 'EMAIL_PORT'):
        raise ImproperlyConfigured('Email server configurations not found in django settings.py.')

    from_email = '%s <noreply@%s>' % (sys_configs['SITE_NAME'], sys_configs['DOMAIN'])
    msg = EmailMessage(subject, message, from_email, recipients)
    if is_html:
        msg.content_subtype = "html"
    msg.send()




def blog_id(request,post_id):
    blog_obj = Post.objects.get(id=post_id)
    body_contain = blog_obj.body.split("^")
    context = {'blog':blog_obj,'body_contain':body_contain}
    return render(request,'blog_id.html',context)

def rschome(request):


    #blog_obj = Post.objects.all().order_by('-id')[:15]
    #page = request.GET.get('page', 1)
    #cmnt_objs = Comments.objects.all().order_by('-id')[:3]
    #paginator = Paginator(blog_obj, 5)
    #try:
    #    blog_page = paginator.page(page)
    #except PageNotAnInteger:
    #    blog_page = paginator.page(1)
    #except EmptyPage:
    #    blog_page = paginator.page(paginator.num_pages)

    context = {}#'blog_obj':blog_obj,'blog_page':blog_page,'comments':cmnt_objs}
    return render(request,'home.html',context)

def comments(request):
    blog_obj = Post.objects.all().order_by('-id')[:15]
    page = request.GET.get('page', 1)
    cmnt_objs = Comments.objects.all().order_by('-id')[:3]
    paginator = Paginator(blog_obj, 5)
    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        blog_page = paginator.page(1)
    except EmptyPage:
        blog_page = paginator.page(paginator.num_pages)

    #context = {'blog_obj':blog_obj,'blog_page':blog_page,'comments':cmnt_objs}
    if request.method == 'POST':
        print (request.POST)
        form = FeedbackForm(request.POST)

        if form.is_valid():

            form.save()
            #return render(request, '.html')
            return render(request,'home.html',{'form':form,'blog_obj':blog_obj,'blog_page':blog_page,'comments':cmnt_objs})
    else:
        form = FeedbackForm()

    return render(request,'feedback.html',{'form':form,'blog_obj':blog_obj,'blog_page':blog_page,'comments':cmnt_objs})

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
