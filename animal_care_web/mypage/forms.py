from django import forms
from .models import Dog

# 강아지 정보를 위한 ModelForm
class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age']  # 강아지 모델에 정의된 필드 이름들
