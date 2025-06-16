from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import WaitListSubscriptionSerializer
from .utils import send_waitlist_email

# Create your views here.

class HealthCheckAPIView(APIView):
    def get(self, request):
        return Response(
            {"status": "healthy", "message": "WaitList API is running"},
            status=status.HTTP_200_OK
        )

class JoinWaitlistAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WaitListSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_waitlist_email(user.name, user.email)
            return Response(serializer.data, status=status.HTTP_200_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
