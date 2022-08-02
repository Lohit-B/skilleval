from apis.views.user import StudentView as StudentAPI
from web.helpers.common import set_auth_header, handle_response, parse_api_response, next_page_url, include_page_info

from django.template.response import TemplateResponse

class StudentWebView():
    @handle_response
    @set_auth_header
    def list(request):
        s_api = StudentAPI()
        resp = s_api.list(request)
        data = parse_api_response(resp)
        include_page_info(data['data']['students'], data, request)
        return TemplateResponse(request, "student_list.html", data)

