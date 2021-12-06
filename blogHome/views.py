from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView

from blogHome.models import Post


# function to process search results
def get_queryset(request):  # new
    query = request.GET.get('q', default="")
    object_list = Post.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )
    return object_list


# function to paginate
def paginate(request, book):
    posts = book
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts


# function to paginate for search results
def paginate_search_results(request, results):
    posts = results
    page = request.GET.get('page')

    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts


def post_list(request):
    book = Post.objects.all()
    posts = paginate(request, book)
    return render(request, 'post_list.html', {'posts': posts})


def islamic_books(request):
    books = Post.objects.filter(category="islamic")
    posts = paginate(request, books)
    return render(request, 'islamic_books.html', {'posts': posts})


def urdu_novels(request):
    books = Post.objects.filter(category="urdu")
    posts = paginate(request, books)
    return render(request, 'urdu_novels.html', {'posts': posts})


def educational_books(request):
    books = Post.objects.filter(category="educational")
    posts = paginate(request, books)
    return render(request, 'educational_books.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})


def search_results(request):
    results = get_queryset(request)
    posts = paginate_search_results(request, results)
    return render(request, 'search_results.html', {'posts': posts})
