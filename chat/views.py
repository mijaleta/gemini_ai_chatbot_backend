# views.py
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
import requests
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
import requests
import os

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        user_message = request.data.get("user_message")

        GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
        GEMINI_URL = os.environ.get("GEMINI_API_URL")  # get URL from .env

        # Call Gemini API
        response = requests.post(
            GEMINI_URL,
            headers={"Authorization": f"Bearer {GEMINI_KEY}"},
            json={"prompt": user_message}
        )

        ai_reply = response.json().get("output_text", "Sorry, no reply")

        # Save to database
        message = Message.objects.create(user_message=user_message, ai_reply=ai_reply)
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)