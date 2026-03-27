# models.py
from django.db import models

class Message(models.Model):
    user_message = models.TextField()
    ai_reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)