from djongo import models
from core.models import BaseMongoModel

class ChatSession(BaseMongoModel):
    session_id = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=17)
    platform = models.CharField(max_length=20)
    language = models.CharField(max_length=2, default='en')
    is_active = models.BooleanField(default=True)
    total_messages = models.IntegerField(default=0)
    
    class Meta:
        collection_name = 'chat_sessions'

class ChatMessage(BaseMongoModel):
    session_id = models.CharField(max_length=100)
    message_type = models.CharField(max_length=10)
    content = models.TextField()
    intent = models.CharField(max_length=100, blank=True)
    confidence_score = models.FloatField(null=True, blank=True)
    
    class Meta:
        collection_name = 'chat_messages'