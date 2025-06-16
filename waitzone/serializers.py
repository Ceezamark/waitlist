from rest_framework import serializers
from .models import WaitListSubscription

class WaitListSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitListSubscription
        fields = '__all__'
