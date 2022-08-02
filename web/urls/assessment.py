from django.urls import path
from web.views.assessment import AssessmentWebView

urlpatterns = [
    path('assessments/<int:pk>', AssessmentWebView.get),
    path('assessments/home', AssessmentWebView.home),
    path('assessments', AssessmentWebView.list),
]
