from django import forms

from pybo.models import Question
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject','content']
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }