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
        if data["password"] != data.get["password2"]:
                raise serializers.ValidationError({"password":"Passwords must match."})
        if len(data["password"]) < 8:
            raise serializers.ValidationError({"password":"Password must be at least 8 characters."})
        return data
    
def create(self, validated_data):
    validated_data.pop('password2')
    password = validated_data.pop('password')
    user = User(**validated_data)
    user.set_password(password)
    user.save()
    return user

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
        
        