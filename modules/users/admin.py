from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'full_name',)
    list_filter = ('is_active', 'is_staff',)
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'full_name', 'is_active', 'is_staff')
    fieldsets = (
        ('Credentials', {'fields': ('email', 'username', 'full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)
