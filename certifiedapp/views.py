from django.shortcuts import render
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import *

def certifiedapphome(request):
    return HttpResponse('cerifiedapphome')


from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import
from certifiedapp.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm


def forgot_password(request):
    return render(request,'forgot_password.html',context={})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/certapp_signup.html', {'form': form})


@login_required
def userdashbord(request):

    if request.user.is_superuser:
        return render(request, 'certifiedapp/admindashbord.html')

    return render(request,'certifiedapp/userdashbord.html')



from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/Change_password.html', {
        'form': form
    })


from django.contrib.auth import *
from certifiedapp.models import Testlist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def test_list(request):
        t_list = Testlist.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(t_list, 5)
        try:
          users = paginator.page(page)
        except PageNotAnInteger:
           users = paginator.page(1)
        except EmptyPage:
           users = paginator.page(paginator.num_pages)

        context = { 't_list' : t_list,'users':users}

	return render(request,'certifiedapp/Test_List.html',context)


def take_test(request):

	return render(request,'certifiedapp/Take_Test.html')

def test_results(request):

	return render(request,'certifiedapp/Test_Results.html')
