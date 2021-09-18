from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Sentence

# Create your views here.

## test code


def index(request):
    pass

def create_book(request):

    if request.method == 'GET':
        return render(request, 'book/create.html')
    elif request.method == 'POST':
        book = Book()
        book.content = request.POST.get('content')
        book.title = request.POST.get('title')
        print(book.title)
        print(book.content)
        book.save()

        print(f"id: {book.id} {book.title} {book.content}")

    return redirect('book:book', book.id)

def detail_book(request, book_id):
     if request.method == 'GET':
         book = Book.objects.get(id=book_id)
         return render(request, 'book/detail.html', {'book': book})
     elif request.method == 'POST':
         pass
     elif request.method == 'DELETE':
         pass


def books(request):
    books = Book.objects.all()
    return render(request, 'book/list.html', {'books': books})

def update_book(request):
    pass

def delete_book(request):
    pass

def add_sentence(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    content = request.POST.get('content')
    sentence = Sentence()
    sentence.content = content
    sentence.book = book
    sentence.chapter = request.POST.get('chapter')
    sentence.chapter_id = 1
    sentence.line_id = book.line_count + 1
    sentence.save()

    book.line_count += 1
    book.save()

    return redirect('book:book', book_id)


def update_sentence(request):
    pass

def delete_sentence(request):
    pass

def detail_sentence(request):
    pass

## test_code ends

