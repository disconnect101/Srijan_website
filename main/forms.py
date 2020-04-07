from django import forms
from .models import Articles,Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'author', 'description', 'content', 'category', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('article_id', 'firstname', 'lastname', 'comment')
