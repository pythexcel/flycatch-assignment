from django.contrib import admin
from .models import CustomUser

from django.contrib import admin
from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from django.utils import timezone

class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'last_login', 'active_users']

    def email(self, obj):
        return obj.get_email()

    def last_login(self, obj):
        return obj.last_login

    def active_users(self, obj):
        if obj.last_login:
            delta = timezone.now() - obj.last_login
            if delta.total_seconds() < settings.SESSION_COOKIE_AGE:
                return True
        return False

    def get_queryset(self, request):
        User = get_user_model()
        active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
        user_id_list = []
        for session in active_sessions:
            data = session.get_decoded()
            user_id_list.append(data.get('_auth_user_id', None))
        return User.objects.filter(id__in=user_id_list)

    active_users.boolean = True


admin.site.register(CustomUser, ActiveUserAdmin)
