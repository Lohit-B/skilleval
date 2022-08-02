from rest_framework import viewsets
from apis.helpers.decorators import handleResponse, checkAuthenticationOrError, checkAuthentication

from apis.controllers import assessment as assessment_controller

class AssessmentView(viewsets.ModelViewSet):
    @handleResponse
    @checkAuthenticationOrError
    def get(self, request, pk):
        resp = assessment_controller.get_assessment(pk, request.user)
        return resp, 200

    @handleResponse
    @checkAuthenticationOrError
    def list(self, request):
        resp = assessment_controller.list_assessments(request.GET, request.user)
        return resp, 200

class AssessmentHomeView(viewsets.ModelViewSet):
    @handleResponse
    @checkAuthenticationOrError
    def get_home(self, request):
        resp = assessment_controller.get_home(request.GET, request.user)
        return resp, 200

class PerformanceView(viewsets.ModelViewSet):
    @handleResponse
    @checkAuthenticationOrError
    def list(self, request):
        resp = assessment_controller.find_performance(request.GET, request.user)
        return resp, 200

    @handleResponse
    @checkAuthenticationOrError
    def create(self, request):
        data = {**request.data}
        resp = assessment_controller.save_performance(data, request.user)
        return resp, 201

