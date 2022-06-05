from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import User as visart_user

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(visart_user)