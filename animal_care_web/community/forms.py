from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'movie_title': forms.TextInput(attrs={'placeholder': '리뷰할 영화 제목'}),
            'review_title': forms.TextInput(attrs={'placeholder': '리뷰 제목'}),
            'content': forms.Textarea(attrs={'placeholder': '리뷰 내용'})

        }