from django import forms
from .models import MrDr

class AskQuestionForm(forms.Form):
    # class Meta:
    #     model = MrDr
    #     fields = ('name','email','title','body')
    name = forms.CharField()
    email = forms.EmailField()
    title = forms.CharField()
    question = forms.CharField(widget=forms.Textarea)
    answer = forms.TextInput()
    
