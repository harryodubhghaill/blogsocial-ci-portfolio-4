from django import forms
from .models import Post, Comment, Community


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
