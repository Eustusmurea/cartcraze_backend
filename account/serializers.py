from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2']

    def validate(self, data):
        if data["password"] != data.get("password2"):
                raise serializers.ValidationError({"password":"Passwords must match."})
        if len(data["password"]) < 8:
            raise serializers.ValidationError({"password":"Password must be at least 8 characters."})
        return data
    

    def create(self, validated_data):
        """Create user and hash password correctly."""
        validated_data.pop("password2")  # Remove password2 from validated data
        password = validated_data.pop("password")  # Extract password

        user = User(**validated_data)  # Create user instance
        user.set_password(password)  # Hash password before saving
        user.save()

        return user
    
    def update(self, instance, validated_data):
        """Update user and handle password changes."""
        password = validated_data.pop("password", None)  # Extract password if provided
        password2 = validated_data.pop("password2", None)

        if password:
            if password != password2:
                raise serializers.ValidationError({"password": "Passwords must match."})
            if len(password) < 8:
                raise serializers.ValidationError({"password": "Password must be at least 8 characters."})
            instance.set_password(password)  # Hash password if it's being updated

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

class LoginSerializer(TokenObtainPairSerializer):
     @classmethod
     def get_token(cls, user):
          token = super().get_token(user)
          token['username'] = user.username
          
          return token
     
     def validate(self, attrs):
          data = super().validate(attrs)
          data['Message'] = 'You have successfully logged in.'
          return data
     
class LogoutSerializer(serializers.Serializer):
    RefreshToken = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['RefreshToken']

        return attrs
    
    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            raise serializers.ValidationError('Token is invalid or expired.')
        
        