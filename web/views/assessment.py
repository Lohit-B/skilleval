from apis.views.assessment import AssessmentView as AssessmentAPI, AssessmentHomeView as AssessmentHomeAPI
from web.helpers.common import set_auth_header, handle_response, parse_api_response, next_page_url 
from django.template.response import TemplateResponse
from django.shortcuts import redirect

class AssessmentWebView():
    @handle_response
    @set_auth_header
    def list(request):
        a_api = AssessmentAPI()
        resp = a_api.list(request)
        data = parse_api_response(resp)
        if request.GET.get('size') == '1' and data.get('data'):
            return redirect('/assessments/%s' % data['data'][0]['id'])

        return TemplateResponse(request, "assessments.html", data)

    @handle_response
    @set_auth_header
    def get(request, pk):
        a_api = AssessmentAPI()
        resp = a_api.get(request, pk)
        data = parse_api_response(resp)
        return TemplateResponse(request, "assessment.html", data)

    @handle_response
    @set_auth_header 
    def home(request):
        if not request.GET.get('skill'):
            return TemplateResponse(request, "assessment_home.html", {})

        a_api = AssessmentHomeAPI()
        resp = a_api.get_home(request)
        data = parse_api_response(resp)
        return TemplateResponse(request, "skill_home.html", data)
