from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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


@login_required
def userdashbord(request):

    if request.user.is_superuser:
        return render(request, 'certifiedapp/admindashbord.html')

    return render(request,'certifiedapp/userdashbord.html')