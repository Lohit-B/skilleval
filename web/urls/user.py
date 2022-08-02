from django.urls import path
from web.views.user import UserWebView

urlpatterns = [
    path('users/signin', UserWebView.signin)
]
