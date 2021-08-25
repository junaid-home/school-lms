from django.contrib import admin
from .models import Child, User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_name', 'first_name', 'last_name', 'grade')
    list_filter = ('email', 'user_name', 'role',
                   'grade', 'is_active', 'is_staff')
    ordering = ('-created_date',)
    list_display = ('email', 'user_name', 'first_name', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'user_name',
         'first_name', 'last_name', 'image', 'grade')}),
        ('Permissions', {'fields': ('role', 'is_staff',
         'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'user_name',
         'first_name', 'last_name', 'password1', 'password2', 'image', 'grade')}),
        ('Permissions', {
         'fields': ('role', 'is_staff', 'is_active', 'is_superuser')}),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Child)
admin.site.unregister(Group)
