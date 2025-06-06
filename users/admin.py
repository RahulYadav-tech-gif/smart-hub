from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

# Inline Profile Editing within User
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

# Extend User Admin
class CustomUserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Unregister the original User admin and re-register
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
