from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/<int:sentence_id>/', views.detail, name='detail'),
    path('<int:book_id>/<int:first_id>/<int:last_id>/', views.create_comment, name='create_comment'),
]