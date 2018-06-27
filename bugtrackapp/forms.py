from django import forms

from .models import Comments


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = []