from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)
class HomeListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    ordering = ['-date_posted']

class HomeDetailView(DetailView):
    model = Post
    template_name = 'blog/details.html'
    context_object_name = 'post'

class HomeCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content']
    template_name = 'blog/post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class HomeUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    #context_object_name = 'post'
    template_name = 'blog/update.html'

    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False

class HomeDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post 
    template_name = 'blog/delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False





def about(request):
    context = {
        'title': "About",
    }
    return render(request, 'blog/about.html', context)
