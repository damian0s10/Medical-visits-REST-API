from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from visits.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name', 'email', 'is_patient', 'is_doctor')
        extra_kwargs = {
            'password':{'write_only': True},
        }     

    def create(self, validated_data):

        user = User.objects.create_user(
                username = validated_data['username'],     
                password = validated_data['password'],
                email = validated_data['email'],
                is_patient = True if 'is_patient' in validated_data and validated_data['is_patient']==True else False,
                is_doctor = True if 'is_doctor' in validated_data and validated_data['is_doctor']==True else False
                )

        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)