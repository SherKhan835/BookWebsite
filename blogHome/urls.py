from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blogHome'),
    path('urdu_novels', views.urdu_novels, name='urdu_novels'),
    path('islamic_books', views.islamic_books, name='islamic_books'),
    path('educational_books', views.educational_books, name='educational_books'),
    path('search_results', views.search_results, name='search_results'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
]
