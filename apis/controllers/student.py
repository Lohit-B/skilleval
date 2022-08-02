from apis.models import User, Grade
from apis.serializers.user import UserSerializer
from apis.helpers.utility import prepare_response
from apis.helpers.exceptions import BadRequest, Forbidden

def list_students(filters, user):
    page = filters.get('page', 1)
    size = filters.get('size', 10)
    limit = int(size)
    offset = (int(page)-1)*limit

    users = User.objects.filter(is_deleted=False, parent=user)
    grade_id = filters.get('grade')
    if grade:
        users = users.filter(grade__id=grade_id)

    users = users.order_by('-created_on')[offset:offset+limit]

    resp = []
    resp['students'] = UserSerializer(users, many=True).data

    grades = Grade.objects.filter(is_deleted=False)
    resp['grades'] = GradeSerializer(grades, many=True).data

    return prepare_response(resp)
    
def list_grades():
    grades = Grade.objects.filter(is_deleted=False)
    resp = GradeSerializer(grades, many=True).data
    return prepare_response(resp)
