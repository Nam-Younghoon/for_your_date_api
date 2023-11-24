from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nickname, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        elif not nickname:
            raise ValueError('Users must have a nickname')
        
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, nickname, password, **kwargs):
        superuser = self.create_user(
            email = self.normalize_email(email),
            nickname = nickname,
            password = password,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.is_admin = True
        superuser.save()
        return superuser