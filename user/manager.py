from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be true')

        return self.create_user(
            email=email,
            password=password,
            **other_fields
        )
    
    
    def create_user(self, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user