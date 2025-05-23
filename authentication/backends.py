import jwt
from rest_framework import authentication,exceptions
from django.conf import settings
from django.contrib.auth.models import User
class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request).split()
        if not auth_data or len(auth_data) != 2:
            return None       
        prefix,token=auth_data.decode('utf-8').split()
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            user= User.objects.get(username=payload['username'])
            return (user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Token expired')
        
        return super().authenticate(request) 