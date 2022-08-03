from rest_framework import viewsets
from apis.helpers.decorators import handleResponse, checkAuthenticationOrError, checkAuthentication

from apis.controllers import user as user_controller

class UserView(viewsets.ModelViewSet):
    @handleResponse
    def signin(self, request):
        data = {**request.data}
        resp = user_controller.login(data['username'], data['password'])
        return resp, 200

    @handleResponse
    @checkAuthenticationOrError
    def profile(self, request):
        resp = user_controller.get_profile(request.user)
        return resp, 200

