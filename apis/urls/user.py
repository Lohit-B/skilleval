from django.urls import path
from apis.views.user import UserView, StudentView

signin = UserView.as_view(
    {
        'post':'signin'
    }
)
students = StudentView.as_view(
    {
        'get':'list',
        'put':'update',
        'post':'create',
    }
)

urlpatterns = [
    path('users/login', signin),
    path('students', students),
]

