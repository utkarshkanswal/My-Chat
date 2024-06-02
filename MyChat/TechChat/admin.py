from django.contrib import admin
from TechChat.models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['sender',"receiver","date","message"]




admin.site.register(ChatMessage,ChatMessageAdmin)
