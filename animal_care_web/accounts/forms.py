from typing import Any
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


# accounts/forms.py
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1')
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = "아이디(ID)"
        self.fields['username'].help_text = "문자, 숫자 및 @/./+/-/_만 가능합니다."
        self.fields['password1'].label = "비밀번호(Password)"
        self.fields['password1'].help_text = ""
        
        del self.fields['password2']


# accounts/forms.py
class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)

        # 각 필드의 레이블을 한국어로 변경
        self.fields['username'].label = "아이디(ID)"
        self.fields['email'].label = "이메일(Email)"
        self.fields['first_name'].label = "이름(first_name)"
        self.fields['last_name'].label = "성(last_name)"
        self.fields['password'].label = ""

        self.fields['username'].help_text = "변경할 아이디를 입력해주세요!"
        self.fields['password'].help_text = "<a href='/accounts/change_password/{}'>비밀번호 변경하기</a>".format(self.user_id)

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']