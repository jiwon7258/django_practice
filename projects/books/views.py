from typing import List
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Book, Author, Publisher


# Create your views here.

# TemplateView
class BooksModelView(TemplateView):
    # 클래스 변수를 오버라이드
    # 뷰 함수와 연결할 html 파일을 지정
    template_name = "books/index.html"

    # html에 넘겨줄 context 변수를 설정하는 함수
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_list"] = ["Book", "Author", "Publisher"]
        return context


# ListView
class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


# DetailView
class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher