from django.urls import path
from waitzone.views import JoinWaitlistAPIView, HealthCheckAPIView

urlpatterns = [
    path('', HealthCheckAPIView.as_view(), name='health-check'),
    path('join/', JoinWaitlistAPIView.as_view(), name='join-waitlist'),
]
