from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import LoginSerializer, LogoutSerializer, UserSerializer


class RegisterUserView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            data = {}  # Initialize data dictionary here
            data['token'] = {
                'refresh': str(token),
                'access': str(token.access_token),
            }
            data['Message'] = 'User has been registered successfully.'
            return Response(data, status=status.HTTP_201_CREATED)  # Return the correct data
        else:
            return Response({
                    "message": "Registration failed. Please check the errors.",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(TokenObtainPairView):
    serializer_class = LoginSerializer


class LogoutUserView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(
            {"message": "You have been logged out successfully."}, status=status.HTTP_200_OK)
