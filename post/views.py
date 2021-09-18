from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, SubComment, Scope
from book.models import Book, Sentence
from django.views import View
# Create your views here.

## test code

def index(request):
    pass


class CommentView(View):

    def get(self, request, book_id, sentence_id, comment_id):
        pass

    def post(self, request, book_id, sentence_id, comment_id):
        pass

    def put(self, request, book_id, sentence_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('post:detail', book_id, sentence_id)

    def delete(self, request, book_id, sentence_id, comment_id):
        comment = get_object_or_404(Comment, comment_id)
        for scope in comment.scopes:
            scope.comments.remove(comment)
        comment.delete()
        return redirect('post:detail', book_id, sentence_id)


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


def create_comment(request, book_id, sentence_id, first_id, last_id):
    book = Book.objects.get(id=book_id)
    depth = book.scope_depth

    comment = Comment()
    comment.content = request.POST.get('content')
    comment.first_id = first_id
    comment.last_id = last_id
    comment.save()

    first_sid = Sentence.get_line2sid(first_id, depth)
    last_sid = Sentence.get_line2sid(last_id, depth)

    while first_sid != last_sid and first_sid < last_sid:
        if first_sid > 0:
            if first_sid % 2:
                update_scope(first_sid, book, comment)
                first_sid += 1
            else:
                first_sid //= 2

        if last_sid > 0:
            if last_sid % 2:
                last_sid //= 2
            else:
                update_scope(last_id, book, comment)
                last_sid -= 1

    update_scope(first_sid, book, comment)

    return redirect('post:detail', book.id, sentence_id)


class SubCommentView(View):

    def get(self, request, book_id, sentence_id, comment_id, subcomment_id):
        pass

    def post(self, request, book_id, sentence_id, comment_id, subcomment_id):
        subcomment = SubComment()
        comment = get_object_or_404(Comment, id=comment_id)
        subcomment.content = request.POST.get('content')
        subcomment.comment = comment
        subcomment.save()

        return render(request, 'post:detail', book_id, sentence_id)


    def put(self, request, book_id, sentence_id, comment_id, subcomment_id):
        pass

    def delete(self, request, book_id, sentence_id, comment_id, subcomment_id):
        pass



## test code ends