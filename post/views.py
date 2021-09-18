from django.shortcuts import render, redirect
from .models import Comment, SubComment, Scope
from book.models import Book, Sentence
# Create your views here.

## test code

def index(request):
    pass


def detail(request, book_id, sentence_id):
    sentence = Sentence.objects.get(id=sentence_id)
    book = Book.objects.get(id=book_id)
    line_id = sentence.line_id
    sid = get_line2scope_id(line_id, book.scope_depth)

    comments = []
    while sid > 0:
        scope = Scope.objects.filter(node_id=sid, book_id=book_id)
        if scope:
            comments += list(scope[0].comments.all())
        sid //= 2
    print(comments)

    return render(request, 'post/detail.html', {'sentence': sentence, 'book': book, 'comments': comments})


def get_line2scope_id(line_id, depth):
    return (1 << depth) - 1 + line_id


def update_scope(sid, book, comment):
    scope = Scope.objects.filter(book=book, node_id=sid)
    if scope:
        scope[0].comments.add(comment)
    else:
        scope = Scope()
        scope.book = book
        scope.node_id = sid
        scope.save()
        scope.comments.add(comment)


def create_comment(request, book_id, first_id, last_id):
    book = Book.objects.get(id=book_id)
    depth = book.scope_depth

    comment = Comment()
    comment.content = request.POST.get('content')
    comment.first_id = first_id
    comment.last_id = last_id
    comment.save()

    first_sid = get_line2scope_id(first_id, depth)
    last_sid = get_line2scope_id(last_id, depth)

    while first_sid != last_sid and first_sid < last_sid:
        if first_sid > 0:
            if first_sid % 2:
                update_scope(first_sid, book, comment)
            else:
                first_sid //= 2

        if last_sid > 0:
            if last_sid % 2:
                last_sid //= 2
            else:
                update_scope(last_id, book, comment)

    update_scope(first_sid, book, comment)

    return redirect('post:detail', book.id, first_id)


def update_comment(request):
    pass

def delete_comment(request):
    pass

def comments(request):
    pass

def create_sub_comment(request):
    pass

def update_sub_comment(request):
    pass

def delete_sub_comment(request):
    pass

def sub_comments(request):
    pass

## test code ends