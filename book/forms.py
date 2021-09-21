from django import forms
from .models import Book, Sentence


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'content']

