from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,error_messages={'blank':'username field may not be blank','required': 'Enter Valid username'})
    password = serializers.CharField(required=True,error_messages={'blank':'password field may not be blank','required': 'Enter Correct Password'})
