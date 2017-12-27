from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def certifiedapphome(request):
    return HttpResponse('cerifiedapphome')


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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


def userdashbord(request):
    return render(request,'certifiedapp/userdashbord.html')