from itertools import count
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView):
    model =  Post
    ordering = '-pk' #최신 포스트부터 보여주기

    def get_context_data(self, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.object.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

