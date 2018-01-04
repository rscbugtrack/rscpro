from django.shortcuts import render,redirect
from django import forms
# Create your views here.

from subjectsapp.models import TechType
class Subjectform(forms.ModelForm):
    class Meta:
        model = TechType
        fields = ['subject_name','status']


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
