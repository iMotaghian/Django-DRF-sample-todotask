from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    searching_fields = ('email',)
    ordering = ('email',)
    # user show only
    fieldsets = (
        ('Authentication', {
            'fields': ('email', 'password'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser'),
        }),
        ('Group Permissions', {
            'fields': ('groups','user_permissions'),
        }),
        ('Important date', {
            'fields': ('last_login',),
        }),
    )
    # add new user fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )

admin.site.register(User, CustomUserAdmin)