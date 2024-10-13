from auth_service.models import IdentityModel
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class APICreateIdentityView(APIView):
    def post(self, request: Request) -> Response:
        username = request.data.get('email')
        password = request.data.get('password')

        if IdentityModel.objects.filter(username=username).exists():
            return Response(
                {'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST
            )

        user = IdentityModel.objects.create(
            username=username,
            email=username,
            password=make_password(password)
        )

        return Response(
            {'message': 'User created successfully'}, status=status.HTTP_201_CREATED
        )
    