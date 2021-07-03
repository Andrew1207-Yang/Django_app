from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.urls import reverse
from .forms import ArticleForm

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog_create.html" #--> create view template
    form_class = ArticleForm #--> create form.py and define a form, then import it
    queryset = Post.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BlogCreateView, self).form_valid(form)


class BlogListView(ListView):
    model = Post
    template_name = "blog_list.html" #--> create list template
    queryset = Post.objects.all()


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_details.html" #--> create detail template

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Post, id=id_)

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("pk")
        queryset = Post.objects.exclude(id=id_).order_by('?')[:3]
        object = get_object_or_404(Post, id=id_)
        context = {
            "object_list": queryset,
            "object":object

        }
        return context


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog_update.html" #--> create update template
    form_class = ArticleForm #--> create form.py and define a form, then import it
    
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Post, pk = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BlogUpdateView, self).form_valid(form)


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_delete.html" #--> create delete template

    queryset = Post.objects.all()  # looks for <blog>/<modelname>_list.html
    
    def get_object(self):
        id_ = self.kwargs.get("pk")       
        return get_object_or_404(Post, pk = id_)

    def get_success_url(self):
        return reverse("blog:default_list") #--> name of a path



