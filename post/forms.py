from django import forms
from .models import Comment, SubComment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', 'first_id', 'last_id']


class SubCommentForm(forms.ModelForm):

    class Meta:
        model = SubComment
        fields = ['content']

