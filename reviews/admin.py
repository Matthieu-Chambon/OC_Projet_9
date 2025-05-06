from django.contrib import admin
from reviews.models import Ticket, Review


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = ('title', 'user', 'time_created')
    search_fields = ('title', 'description')
    list_filter = ('user',)
    ordering = ('-time_created',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'user', 'image', 'answered')
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('id', 'ticket', 'user', 'rating', 'time_created')
    search_fields = ('ticket__title', 'user__username', 'headline')
    list_filter = ('ticket', 'user')
    ordering = ('-time_created',)
    fieldsets = (
        (None, {
            'fields': ('ticket', 'user', 'rating', 'headline', 'body')
        }),
    )
