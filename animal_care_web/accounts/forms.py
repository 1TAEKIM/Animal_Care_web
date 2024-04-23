from typing import Any
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


# accounts/forms.py
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


# accounts/forms.py
class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.user_id = kwargs.pop('user_id', None)

        super().__init__(*args, **kwargs)

        self.fields['password'].help_text = "<a href='/accounts/change_password/{}'>비밀번호 변경하기</a>".format(self.user_id)
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['username']