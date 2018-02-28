from django.shortcuts import render,redirect,get_object_or_404
from django import forms
from django.contrib.auth.decorators import login_required
from subjectsapp.forms import PaperstypeForm,QuestionsForm
# Create your views here.

from subjectsapp.models import TechType,Paperstype,Questions


class Subjectform(forms.ModelForm):
    class Meta:
        model = TechType
        fields = ['subject_name','status']


@login_required
def subjectlist(request):
    subjects_list = TechType.objects.all()
    context ={'subjects':subjects_list}
    template = 'subjectsapp/subject_list.html'
    return render(request,template,context)

def allresults(request):
    template = 'subjectapp/subject_result.html'

def add_subject(request):
    subform = Subjectform(request.POST)

    if subform.is_valid():
        subject_name =request.POST.get('subject_name')
        status = request.POST.get('status')
        if status:
            status=True
        else:
            status=False
        user =request.user
        t = TechType(subject_name=subject_name,status=status,user=user)

        t.save()
        return redirect('subjectapp:subjectlist')

    subform = Subjectform()

    template = 'subjectsapp/subjectadd_list.html'
    context = {'subform':subform}
    return render(request,template,context)


@login_required
def edit_subject(request, pk):

    subject = TechType.objects.get(pk=pk)
    template = 'subjectsapp/subjectedit.html'
    form = Subjectform(request.POST or None, instance=subject)
    context= { 'form':form }
    if request.method == 'POST':
        form.save()
        return redirect('subjectapp:subjectlist')
    return render(request,template,context)


# papertype CRUD

@login_required
def paperslist(request):
    allpapers = Paperstype.objects.all()
    context = {'paperslist':allpapers}
    template = 'subjectsapp/papers_list.html'
    return render(request, template,context)


@login_required
def add_papers(request):
    paperform = PaperstypeForm(request.POST)

    if paperform.is_valid():
        paperform.save()

        return redirect('subjectapp:paperslist')

    paperform = PaperstypeForm()

    template = 'subjectsapp/papersadd_list.html'
    context = {'paperform':paperform}
    return render(request,template,context)

@login_required
def edit_papertype(request, pk):
    paper = Paperstype.objects.get(pk=pk)
    template = 'subjectsapp/papersedit.html'
    form = PaperstypeForm(request.POST or None, instance=paper)
    context = {'form':form}
    if request.method == 'POST':
        form.save()
        return redirect('subjectapp:paperslist')
    return render(request,template,context)


# questions CRUD
@login_required
def questionlist(request):
    allquestions = Questions.objects.all()
    context = {'questions':allquestions}
    template = 'subjectsapp/questions_list.html'
    return render(request, template,context)


@login_required
def add_questions(request):
    question_form = QuestionsForm(request.POST)

    if question_form.is_valid():
        question_form.save()

        return redirect('subjectapp:questionlist')

    question_form = QuestionsForm()

    template = 'subjectsapp/questionadd_list.html'
    context = {'question_form':question_form}
    return render(request,template,context)



@login_required
def edit_questions(request, pk):
    que = Questions.objects.get(pk=pk)
    template = 'subjectsapp/questionedit.html'
    form = QuestionsForm(request.POST or None, instance=que)
    context = {'form':form}
    if request.method == 'POST':
        form.save()
        return redirect('subjectapp:questionlist')

    return render(request,template,context)
