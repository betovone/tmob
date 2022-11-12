from rest_framework import serializers

from .models import Redirect

class RedirectSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=Redirect.LONG_KEY)
    url = serializers.CharField(max_length=Redirect.LONG_URL)


