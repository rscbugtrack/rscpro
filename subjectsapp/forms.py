from .models import Paperstype
from django import forms


# all forms..
class PaperstypeForm(forms.ModelForm):
    class Meta:
        model = Paperstype
        fields = ['subject_name','mode','papernumber','status']