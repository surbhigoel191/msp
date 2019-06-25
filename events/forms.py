from django import forms

from .models import Candidate
from .models import Question
class PostForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('firstname', 'lastname','email', 'bitsid', 'contact')

class QuesForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('ques', 'opt1','opt2', 'opt3', 'opt4')