from django.db import models
from UserManagement.models import User,Profile


class ChatMessage(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="user")
    sender=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="sender")
    receiver=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="receiver")

    message = models.CharField(max_length=1000)

    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Message"

    def __str__(self):
        return f"{self.sender} - {self.receiver}"
    
    @property
    def sender_profile(self):
        sender_profile = Profile.objects.get(user=self.sender)
        return sender_profile
    
    @property
    def receiver_profile(self):
        reciever_profile = Profile.objects.get(user=self.receiver)
        return reciever_profile