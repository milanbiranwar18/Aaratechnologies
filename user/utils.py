from rest_framework.authentication import SessionAuthentication
import logging
import jwt
from aara_project import settings
from user.models import User
from rest_framework.response import Response


class SessionAuth(SessionAuthentication):
    def enforce_csrf(self, request):
        return


logging.basicConfig(filename="utils.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class JWT:
    """
    Class for JWT
    """
    def encode(self, data):
        try:
            if not isinstance(data, dict):
                return Response({"Message":"Data should be a dictionary"})
            if 'exp' not in data.keys():
                data.update({'exp': settings.JWT_EXP})
            return jwt.encode(data, 'secret', algorithm='HS256')
        except Exception as e:
            logging.error(e)
