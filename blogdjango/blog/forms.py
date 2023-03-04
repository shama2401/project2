from django import forms
from .models import *

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'category_id']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-text'}),
            'content' : forms.Textarea(attrs={'class' : 'form-text'}),
            'image' : forms.FileInput(attrs={'class' : 'form-text'}),
            'category_id' : forms.Select(attrs={'class' : 'form-text'}),
        }