from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import CustomUser

# Register your models here.


class UserAdmin(UserAdmin):
    pass


admin.site.register(CustomUser, UserAdmin)
