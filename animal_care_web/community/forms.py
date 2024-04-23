from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '사진 첨부'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 10})

        }