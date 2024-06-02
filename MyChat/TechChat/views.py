from django.shortcuts import render
from rest_framework import viewsets
from TechChat.serializers import MessageSerializer
from TechChat.models import ChatMessage
from django.db.models import OuterRef, Subquery
from django.db.models import Q
from UserManagement.models import User,Profile
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse

class MyInbox(viewsets.ModelViewSet):
    serializer_class=MessageSerializer
    # permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user_id=self.kwargs["user_id"]
        messages=ChatMessage.objects.filter(
            id__in=Subquery(
                User.objects.filter(
                    Q(sender__receiver=user_id)|
                    Q(receiver__sender=user_id)
                ).distinct().annotate(
                    last_msg=Subquery(
                        ChatMessage.objects.filter(
                             Q(sender=OuterRef('id'),receiver=user_id) |
                            Q(receiver=OuterRef('id'),sender=user_id)
                        ).order_by('-id')[:1].values_list('id',flat=True) 
                    )
                ).values_list('last_msg', flat=True).order_by("-id")
            )
        ).order_by("-id")
        return messages




