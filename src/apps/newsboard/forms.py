from django import forms
from .models import Comment


class CommentForm(forms.Form):
    text = forms.CharField(label='', max_length=70, widget=forms.Textarea(attrs={'size': 70}))
