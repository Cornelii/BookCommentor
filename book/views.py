from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Book, Sentence
from post.models import Scope


# Create your views here.

## test
class BookView(View):

    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'book/detail.html', {'book':book})

    def post(self, request, book_id):
        book = Book()
        book.content = request.POST.get('content')
        book.title = request.POST.get('title')
        if request.POST.get('depth'):
            book.scope_depth = request.POST.get('depth')
        book.save()

        return redirect('book:book', book.id)

    def put(self, request, book_id):
        book = get_object_or_404(Book, book_id)
        book.title = request.POST.get('title')
        book.content = request.POST.get('content')
        book.save()
        return redirect('book:book', book_id)

    def delete(self, request, book_id):
        book = get_object_or_404(Book, book_id)
        book.delete()

        return redirect('book:index')


def index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})


def add_sentence(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # content = request.POST.get('content')
    # sentence = Sentence()
    # sentence.content = content
    # sentence.book = book
    # sentence.chapter = request.POST.get('chapter')
    # sentence.chapter_id = 1
    # sentence.line_id = book.line_count + 1
    # sentence.save()
    #
    # book.line_count += 1
    # book.save()
    Sentence.add_sentence(request, book)

    return redirect('book:book', book_id)


class SentenceView(View):

    def get(self, request, book_id, sentence_id):
        sentence = Sentence.objects.get(id=sentence_id)
        book = Book.objects.get(id=book_id)
        line_id = sentence.line_id
        sid = Sentence.get_line2sid(line_id, book.scope_depth)

        comments = []
        while sid > 0:
            scope = Scope.objects.filter(node_id=sid, book_id=book_id)
            if scope:
                comments += list(scope[0].comments.all())
            sid //= 2

        return render(request, 'post/detail.html', {'sentence': sentence, 'book': book, 'comments': comments})

    def post(self, request, book_id, sentence_id):
        book = get_object_or_404(Book, id=book_id)
        Sentence.add_sentence(request, book)

        return redirect('book:book', book_id)

    def put(self, request, book_id, sentence_id):
        pass

    def delete(self, request, book_id, sentence_id):
        pass


## test_code ends

