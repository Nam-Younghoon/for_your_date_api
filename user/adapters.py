from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class CustomAccountAdapter(DefaultAccountAdapter):
    
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data

        # 추가 저장 필드: nickname
        nickname = data.get("nickname")
        if nickname:
            user.nickname = nickname

        # 부모 클래스의 save_user 호출
        user = super().save_user(request, user, form, False)

        # 저장 여부에 따라 user를 저장
        if commit:
            user.save()

        return user
        
    