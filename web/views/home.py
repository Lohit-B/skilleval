from apis.views.user import UserView as UserAPI
from web.helpers.common import set_auth_header, handle_response, parse_api_response, next_page_url, include_page_info

from django.template.response import TemplateResponse
from django.shortcuts import redirect

class HomeWebView():
    @handle_response
    @set_auth_header
    def home(request):
        p_api = UserAPI()
        resp = p_api.profile(request)
        data = parse_api_response(resp)
        if request.user.is_institute:
            return redirect('/students')
        
        return redirect('/assessments/home')

