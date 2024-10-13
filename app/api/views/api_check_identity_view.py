from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

class APICheckIdentityView(APIView):
    def post(self, request: Request) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response(
                {'message': 'User authenticated. Able to login'}, status=status.HTTP_200_OK
            )
        
        return Response(
            {'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED
        )
    