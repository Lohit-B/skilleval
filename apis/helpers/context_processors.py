from apis.serializers.user import UserSerializer
from apis.models import User
from django.contrib.auth.models import AnonymousUser

def user_serialize(request):
    if request.user and isinstance(request.user, User) and not isinstance(request.user, AnonymousUser):
        request.__setattr__('user', UserSerializer(request.user).data)
        request.__setattr__('is_loggedin', True)
    else:
        request.__setattr__('is_loggedin', False)

    return request
