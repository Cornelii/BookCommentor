from django.db import models
from django.db.models.deletion import CASCADE
from book.models import Book

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length = 20)
    group_book = models.ManyToManyField(Book, related_name='mygroups', null=True)
    leader = models.ForeignKey(User, on_delete=models.PROTECT)
    members = models.ManyToManyField(User, related_name="mygroups", null=True)

    # Group에 가입한 User 목록
    # group = Group.objects.all().first()
    # group_members = group.members.all()

    # User가 가입한 Group 목록
    # user = User.objects.all().first()
    # mygroup = user.mygroups.all()