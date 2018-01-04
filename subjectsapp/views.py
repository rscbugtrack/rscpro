from django.shortcuts import render,redirect,get_object_or_404
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

from subjectsapp.models import TechType
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
def edit_subject(request, pk=2):

    subject = TechType.objects.get(pk=pk)
    template = 'subjectsapp/subjectedit.html'
    form = Subjectform(request.POST or None, instance=subject)
    context= { 'form':form }
    if request.method == 'POST':
        form.save()
        return redirect('subjectapp:subjectlist')
    return render(request,template,context)





