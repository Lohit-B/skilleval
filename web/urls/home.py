from django.urls import path
from web.views.home import HomeWebView

urlpatterns = [
    path('', HomeWebView.home)
]
