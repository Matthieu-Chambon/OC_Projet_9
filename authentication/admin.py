from django.contrib import admin

from authentication.models import User, UserFollows


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username',)
    search_fields = ('username',)
    list_filter = ('is_active',)
    ordering = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login',)
        }),
    )


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):

    list_display = ('user', 'followed_user')
    search_fields = ('user__username', 'followed_user__username')
    list_filter = ('user', 'followed_user')
    ordering = ('user', 'followed_user')
    fieldsets = (
        (None, {
            'fields': ('user', 'followed_user')
        }),
    )
