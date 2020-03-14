from django import forms
from .models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'author', 'description', 'content', 'category', 'image')