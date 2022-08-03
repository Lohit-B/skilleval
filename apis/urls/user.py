from django.urls import path
from apis.views.user import UserView
from apis.views.student import StudentView

signin = UserView.as_view(
    {
        'post':'signin'
    }
)
profile= UserView.as_view(
    {
        'get':'profile'
    }
)
students = StudentView.as_view(
    {
        'get':'list',
        'put':'update',
        'post':'create',
    }
)
report = StudentView.as_view(
    {
        'get':'report',
    }
)

urlpatterns = [
    path('users/signin', signin),
    path('users/profile', profile),
    path('students', students),
    path('students/<int:pk>/reports', report),
]

