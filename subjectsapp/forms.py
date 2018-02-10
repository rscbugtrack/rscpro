from .models import Paperstype,Questions
from django import forms


# all forms..
class PaperstypeForm(forms.ModelForm):
    class Meta:
        model = Paperstype
        fields = ['subject_name','mode','papernumber','status']


class QuestionsForm(forms.ModelForm):
    question_name = forms.Textarea()

    class Meta:
        model = Questions
        exclude = ('date_added',)
