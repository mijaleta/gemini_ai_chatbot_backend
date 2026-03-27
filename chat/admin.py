from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_message', 'ai_reply', 'timestamp')
    search_fields = ('user_message', 'ai_reply')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',)
