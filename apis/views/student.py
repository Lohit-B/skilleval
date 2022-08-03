from rest_framework import viewsets
from apis.helpers.decorators import handleResponse, checkAuthenticationOrError, checkAuthentication

from apis.controllers import user as user_controller
from apis.controllers import student as student_controller

class StudentView(viewsets.ModelViewSet):
    @handleResponse
    @checkAuthenticationOrError
    def list(self, request):
        resp = student_controller.list_students(request.GET, request.user)
        return resp, 200

    @handleResponse
    @checkAuthenticationOrError
    def create(self, request):
        data = {**request.data}
        resp = user_controller.create_bulk_students(data, request.user)
        return resp, 201

    @handleResponse
    @checkAuthenticationOrError
    def update(self, request):
        data = {**request.data}
        resp = user_controller.update_student(data, request.user)
        return resp, 202

    @handleResponse
    @checkAuthenticationOrError
    def report(self, request, pk):
        resp = student_controller.get_reports(pk, request.GET, request.user)
        return resp, 200
