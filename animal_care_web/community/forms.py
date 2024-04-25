from django import forms
from .models import Post, Comment


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
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': ''
        }

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 3}),
        }
