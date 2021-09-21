from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, SubComment, Scope
from book.models import Book, Sentence
from django.views import View
from .forms import SubCommentForm
# Create your views here.

## test code

def index(request):
    pass


class CommentView(View):

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        print(method)
        if method == 'put':
            return self.put(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        else:
            return super(CommentView, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        pass

    def post(self, book_id, sentence_id, comment_id):
        pass

    def put(self, book_id, sentence_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.content = self.request.POST.get('content')
        comment.save()
        return redirect('post:detail', book_id, sentence_id)

    def delete(self, *args, **kwargs):
        comment_id = kwargs['comment_id']
        book_id = kwargs['book_id']
        sentence_id = kwargs['sentence_id']
        comment = get_object_or_404(Comment, id=comment_id)
        for scope in comment.scopes.all():
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

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '')
        if method == 'put':
            return self.put(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        else:
            return super(SubCommentView, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        sentence_id = kwargs.get('sentence_id', 0)
        comment_id = kwargs.get('comment_id', 0)
        subcomment_id = kwargs.get('subcomment_id', 0)

        sentence = get_object_or_404(Sentence, id=sentence_id)
        comment = get_object_or_404(Comment, id=comment_id)
        if subcomment_id:
            subcomment = SubComment.objects.get(id=subcomment_id)
            form = SubCommentForm(instance=subcomment)
        else:
            form = SubCommentForm()
            subcomment = SubComment()

        return render(self.request, 'post/sub_detail.html', {'form': form, 'sentence':sentence,
                                                             'comment': comment, 'subcomment': subcomment})

    def post(self, *args, **kwargs):
        comment_id = kwargs.get('comment_id', '')
        book_id = kwargs.get('book_id', '')
        sentence_id = kwargs.get('sentence_id', '')
        comment = get_object_or_404(Comment, id=comment_id)
        form = SubCommentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            subcomment = form.save(commit=False)
            subcomment.comment = comment
            subcomment.save()
            return redirect('post:subcomment', book_id, sentence_id, comment_id, subcomment.id)

        return render(self.request, 'post:detail', book_id, sentence_id)


    def put(self, book_id, sentence_id, comment_id, subcomment_id):
        pass

    def delete(self, book_id, sentence_id, comment_id, subcomment_id):
        pass



## test code ends