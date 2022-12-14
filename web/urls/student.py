from django.urls import path
from web.views.student import StudentWebView

urlpatterns = [
    path('students', StudentWebView.list),
    path('students/<int:pk>/reports', StudentWebView.report),
]
