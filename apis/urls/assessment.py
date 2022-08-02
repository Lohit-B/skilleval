from django.urls import path
from apis.views.assessment import AssessmentHomeView, AssessmentView, PerformanceView

assessment_home = AssessmentHomeView.as_view(
    {
        'get':'get_home'
    }
)
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
    path('assessments/home', assessment_home),
    path('assessments', assessments),
    path('performances', performances),
]

