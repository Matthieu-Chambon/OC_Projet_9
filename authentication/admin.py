from django.contrib import admin

from .models import User
from reviews.models import Ticket, Review

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

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = ('title', 'user', 'time_created')
    search_fields = ('title', 'description')
    list_filter = ('user',)
    ordering = ('-time_created',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'user', 'image')
        }),
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('ticket', 'user', 'rating', 'time_created')
    search_fields = ('ticket__title', 'user__username', 'headline')
    list_filter = ('ticket', 'user')
    ordering = ('-time_created',)
    fieldsets = (
        (None, {
            'fields': ('ticket', 'user', 'rating', 'headline', 'body')
        }),
    )