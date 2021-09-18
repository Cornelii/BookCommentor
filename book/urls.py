from django.urls import path
from . import views
app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('<int:book_id>/', views.detail_book, name='book'),
    path('<int:book_id>/<int:sentence_id>/', views.detail_sentence, name='sentence'),
    path('create/', views.create_book, name='create'),
    path('<int:book_id>/add', views.add_sentence, name='add'),
]