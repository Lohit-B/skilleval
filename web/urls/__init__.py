from .user import urlpatterns as u_urls
from .student import urlpatterns as s_urls
from .assessment import urlpatterns as a_urls

urlpatterns = u_urls+s_urls+a_urls

