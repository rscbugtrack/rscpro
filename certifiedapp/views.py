from django.shortcuts import render
from django.shortcuts import render, redirect, render_to_response
import random
import django
import datetime

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import *
from django.contrib.auth.models import User
from subjectsapp.models import Questions,Paperstype
from certifiedapp.models import StudentResults

def certifiedapphome(request):
    return HttpResponse('cerifiedapphome')


from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import
from certifiedapp.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from .forms import StudentProfileform
from .models import StudentProfile
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
    # only for superuser..

    if request.method == 'POST':
        form = StudentProfileform(request.POST, request.FILES)
        if form.is_valid():
            picform = form.save(commit=False)
            picform.stu_user = request.user
            picform.save()

    if request.user.is_superuser:
        return render(request, 'certifiedapp/admindashbord.html')
    # only for nonsuper users / general users...
    else:
        form = StudentProfileform()
        # stu = StudentProfile.objects.get(stu_user=request.user)
        try:

            stupic = StudentProfile.objects.get(stu_user=request.user)
        except:
            stupic = 'None'

        return render(request,'certifiedapp/userdashbord.html',{'profilepic_form':form,'stupic':stupic})



from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            
            return redirect('login')
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
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
def simple(request):
    import random
    import django
    import datetime
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 800))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "certifiedapp/Take_Test.html", data)
    # if not GET, then proceed
    else:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("certifiedapp:upload_csv"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("certifiedapp:upload_csv"))

        file_data = csv_file.read().decode("utf-8")

        x=[]
        y=[]
        fig=Figure()
        ax=fig.add_subplot(111)
        import csv
        import io
        io_string = io.StringIO(file_data)
        plots = csv.reader(io_string, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
        ax.plot(x, y, label='$x^3$')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Sample Data Graph')
        canvas = FigureCanvas(fig)
        response = HttpResponse( content_type = 'image/png')
        canvas.print_png(response)
        return response

@login_required
def test_list(request):
    t_list = Testlist.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(t_list, 5)
    try:
        t_list = paginator.page(page)
    except PageNotAnInteger:
        t_list = paginator.page(1)
    except EmptyPage:
        t_list = paginator.page(paginator.num_pages)
    context = { 't_list' : t_list,'t_list':t_list}
    return render(request,'certifiedapp/Test_List.html',context)

@login_required
def takepredict(request):
    import numpy as np
    A = np.array([[1, 2, 3], [4, 5, 6]]) #iprint A # [[1 2 3] # [4 5 6]] 
    context = {'example1':A}
    return render(request,'certifiedapp/Take_Test.html', context)

def test_results(request):

    return render(request,'certifiedapp/Test_Results.html')


# student free test.
@login_required
def student_freetest(request):
    stu_user = User.objects.get(username=request.user)
    paper = Paperstype.objects.get(pk=2)
    request.session['papertype'] = paper.id
    print(request.session['papertype'])

    questions = Questions.objects.filter(papertype=paper)
    que_count = questions.count()
    request.session['total_que'] = que_count
    context = {'stu_questions':questions, 'que_count':que_count}



    print(stu_user)
    return render(request, 'certifiedapp/free_test.html', context)
    # return HttpResponse(questions)



@login_required
def student_test_submit(request):
    try:
        print(request.session['papertype'])
    except:
        raise ValueError('Your test done....')
    print(request.session['total_que'])
    total_que = int(request.session['total_que'])
    paper_type = Paperstype.objects.get(pk=int(request.session['papertype']))
    print('Total marks-->:',request.POST.get('totalmarks'))
    total_marks = int(request.POST.get('totalmarks'))

    stu_results = StudentResults(stu_user=request.user, total_marks = total_marks, total_question = total_que,paper_type = paper_type)
    stu_results.save()
    del request.session['papertype']
    request.session['student_resultid'] = stu_results.id
    # print(request.POST)
    return redirect('certifiedapp:student_testresult')
    # return HttpResponse(stu_results)

@login_required
def student_testresult(request):
    student_resultid = int(request.session['student_resultid'])

    return render(request, 'certifiedapp/student_results.html', context={'sturesults':StudentResults.objects.get(pk=student_resultid)})


