from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    line_count = models.IntegerField(default=0)
    chapter_count = models.IntegerField(default=0)
    scope_depth = models.IntegerField(default=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sentence(models.Model):

    content = models.TextField()
    chapter = models.CharField(max_length=200, blank=True, null=True)
    chapter_id = models.IntegerField(null=True)
    line_id = models.IntegerField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='sentences')


