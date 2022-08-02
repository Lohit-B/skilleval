from rest_framework.response import Response
import traceback
from apis.helpers.exceptions import BaseException, BadRequest, JWTTokenExpired
from apis.controllers.user import get_user_by_id 

from apis.helpers.utility import decode_jwt

def handleResponse(func):
    def wrapper(*a, **kw):
        try:
            resp, status = func(*a, **kw)
            return Response(data=resp, status=status or 200, content_type='json')
        except JWTTokenExpired as ej:
            traceback.print_exc()
            return Response(status=ej.getStatusCode(), data={'message':str(ej), 'code':"AUTH_REQUIRED"})
        except BaseException as e:
            traceback.print_exc()
            return Response(status=e.getStatusCode(), data={'message':str(e)})
        except Exception as e2:
            traceback.print_exc()
            return Response(status=500, data={'message':str(e2)})

    return wrapper

def checkAuthentication(func):
    def wrapper(*a, **kw):
        request = a[1]
        user = _getUserDataFromJWT(request)
        request.__setattr__('user', user or None)
        return func(*a, **kw)

    return wrapper

def checkAuthenticationOrError(func):
    def wrapper(*a, **kw):
        request = a[1]
        user = _getUserDataFromJWT(request)
        if not user:
            raise JWTTokenExpired()
        
        request.__setattr__('user', user)
        return func(*a, **kw)

    return wrapper

def _getUserDataFromJWT(request):
    auth_token = request.META.get('HTTP_AUTHORIZATION')
    if not auth_token:
        return None
    try:
        payload = decode_jwt(auth_token)
        user_id = payload.get('user_id')
        if user_id:
            user = get_user_by_id(user_id)
            return user

    except Exception as e:
        raise JWTTokenExpired(str(e))

    return None

