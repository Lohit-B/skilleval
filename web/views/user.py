from apis.views.user import UserView as UserAPI
from web.helpers.common import set_auth_header, handle_response, parse_api_response, next_page_url

from django.template.response import TemplateResponse

class UserWebView():
    @handle_response
    def signin(request):
        return TemplateResponse(request, "login.html")

