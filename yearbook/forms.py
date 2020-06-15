from django import forms
from .models import YearbookData

class YearbookDataForm(forms.ModelForm):
    class Meta:
        model = YearbookData
        fields = ('year', 'regno', 'name', 'branch', 'aboutme', 'wdysy', 'yfm', 'links', 'souvenir', 'photo', 'coverphoto')