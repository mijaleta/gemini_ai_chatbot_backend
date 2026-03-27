import os
from google import genai
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
            user_message = request.data.get("user_message")
            
            # Initialize the client
            client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

            try:
                # UPDATE THIS LINE: Add '-preview'
                response = client.models.generate_content(
                    model="gemini-3-flash-preview", 
                    contents=user_message
                )
                ai_reply = response.text

            except Exception as e:
                # This will now catch and print the specific error to your terminal
                print(f"Gemini API Error: {e}")
                ai_reply = "I'm having trouble connecting to my brain right now."

            # Save to database
            message = Message.objects.create(user_message=user_message, ai_reply=ai_reply)
            serializer = self.get_serializer(message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)