from django.urls import path
from apis.views.assessment import AssessmentView, PerformanceView

assessment = AssessmentView.as_view(
    {
        'get':'get'
    }
)
assessments = AssessmentView.as_view(
    {
        'get':'list'
    }
)
performances = PerformanceView.as_view(
    {
        'get':'list',
        'post':'create',
    }
)

urlpatterns = [
    path('assessments/<int:pk>', assessment),
    path('assessments', assessments),
    path('performances', performances),
]

