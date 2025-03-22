from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.generate_confirmation_code()
        return user

class ConfirmEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=6)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.get(email=email)

        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect credentials')

        if not user.is_active:
            raise serializers.ValidationError('User not confirmed')

        return {
            'refresh': RefreshToken.for_user(user).refresh,
            'access': RefreshToken.for_user(user).access
        }

