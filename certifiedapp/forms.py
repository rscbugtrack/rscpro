from django.forms import * 

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import StudentProfile
class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
                               widget=TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    username = CharField(widget=TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = CharField(label="Password", widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = CharField(label="Confirm Password", widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return


class StudentProfileform(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('stu_photo',)


