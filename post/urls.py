from django.urls import path
from . import views
from book.views import SentenceView
from .views import CommentView, SubCommentView

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/<int:sentence_id>/', SentenceView.as_view(), name='detail'),
    path('<int:book_id>/<int:sentence_id>/<int:first_id>/<int:last_id>/', views.create_comment, name='create_comment'),
    path('<int:book_id>/<int:sentence_id>/<int:comment_id>/', CommentView.as_view(), name='comment'),
    path('<int:book_id>/<int:sentence_id>/<int:comment_id>/<int:dummy_id>/<int:subcomment_id>/',
         SubCommentView.as_view(), name='subcomment'),

]