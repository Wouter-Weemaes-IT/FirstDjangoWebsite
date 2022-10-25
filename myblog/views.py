from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .form import PostForm,EditForm
# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    form_class = PostForm
    template_name = 'home.html'


class ArticDetailView(DetailView):
    model = Post
    form_class = PostForm
    template_name = 'articDetails.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'

