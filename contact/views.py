from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm
from blog.models import Post
from django.contrib import messages

# Create your views here.


class NewContact(CreateView):
    model = Contact
    template_name = "home.html"
    form_class = ContactForm
    queryset = Contact.objects.all()

    def get_context_data(self, **kwargs):
        queryset = Post.objects.order_by('?')[0]
        form_class = ContactForm

        context = {
            'object_list': queryset,
            'form': form_class
        }
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        # messages.success(self.request, 'Form submission successful')

        return super(NewContact, self).form_valid(form)
