from django import forms

from .models import Post

from tinymce.widgets import TinyMCE



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author','article_type', 'preview','preview_image','content']
        # widgets = {
        #     'content' : TinyMCE(attrs={'cols': 80, 'rows': 30,'class': 'form-control'}),
        # }

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     # if not "Andrew" in title:
    #     #     raise forms.ValidationError("Must contain Andrew")
    #     return title
