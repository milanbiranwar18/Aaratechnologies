# Create your views here.
import json
import logging
from user.utils import SessionAuth, SessionAuthentication, JWT
from django.contrib.auth import logout, login
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView


from user.serializer import RegistrationSerializer, LoginSerializer

logging.basicConfig(filename="django.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Registration(APIView):
    """
    Class for user Registration
    """

    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Registered Successfully", "data": serializer.data, "status": 201})
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)


class Login(APIView):
    """
    Class for user login
    """

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            login(request, serializer.context.get("user"))
            user = serializer.context.get("user")
            token = JWT().encode(data={"user_id": user.id})
            return Response({"message": "Login Successfully", "token":token, "status": 201})

        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)


class Logout(APIView):
    """
    Class for user logout
    """

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"Message": "Logout Successfully", "status": 200})
        return Response({"Message": "User already logout"})

