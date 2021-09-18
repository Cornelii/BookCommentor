from django.db import models
from book.models import Book
# Create your models here.


class Scope(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='scopes')
    node_id = models.IntegerField(db_index=True)

    @classmethod
    def update_scope(cls, sid, book, comment):
        scope = Scope.objects.filter(book=book, node_id=sid)
        if scope:
            scope[0].comments.add(comment)
        else:
            scope = Scope()
            scope.book = book
            scope.node_id = sid
            scope.save()
            scope.comments.add(comment)


class Comment(models.Model):
    content = models.TextField()
    first_id = models.IntegerField()
    last_id = models.IntegerField()
    scopes = models.ManyToManyField(Scope, related_name='comments')


class SubComment(models.Model):
    content = models.CharField(max_length=500)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='sub_comments')


