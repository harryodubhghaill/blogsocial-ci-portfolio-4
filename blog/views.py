from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'post_list.html'
    paginate_by = 12
