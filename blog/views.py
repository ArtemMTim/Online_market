from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post


class ContactsView(TemplateView):
    template_name = "blog/contacts.html"

class PostDetailView(DetailView):
    model = Post
    def get_object(self, queryset=None):
        # Update view counter
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object



class PostCreateView(CreateView):
    model = Post
    fields = ("title", "text", "image", "published")
    success_url = reverse_lazy('blog:post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "text", "image", "published")
    success_url = reverse_lazy('blog:post_list')
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


# Create your views here.
