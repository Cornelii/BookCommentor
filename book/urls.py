from django.urls import path
from . import views
from .views import BookView, SentenceView
from django.views.generic.base import TemplateView
app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', BookView.as_view(), name='book'),
    path('<int:book_id>/<int:sentence_id>/', SentenceView.as_view(), name='sentence'),
    path('create/', TemplateView.as_view(template_name='book/create.html'), name='create'),
]