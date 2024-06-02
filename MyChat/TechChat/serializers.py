from rest_framework import serializers
from TechChat.models import ChatMessage
from UserManagement.serializers import ProfileSerializer

class MessageSerializer(serializers.ModelSerializer):
    receiver_profile = ProfileSerializer(read_only=True)
    sender_profile = ProfileSerializer(read_only=True)

    class Meta:
        model=ChatMessage
        fields=['id','sender','receiver','receiver_profile','sender_profile','message','is_read','date']
    
    def __init__(self,*args,**kwargs):
        super(MessageSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        if request and request.method=='GET':
            self.Meta.depth=2