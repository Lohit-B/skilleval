from apis.models import User, Grade
from apis.serializers.user import UserSerializer, GradeSerializer
from apis.helpers.utility import prepare_response
from apis.helpers.exceptions import BadRequest, Forbidden
from apis.controllers.user import get_user_by_id
from apis.controllers.assessment import get_reports_for_category
from apis.models.assessment import ASSESSMENT_CATEGORY


def list_students(filters, user):
    page = filters.get('page', 1)
    size = filters.get('size', 10)
    limit = int(size)
    offset = (int(page)-1)*limit

    users = User.objects.filter(is_deleted=False, parent=user, is_student=True)
    grade_id = filters.get('grade')
    if grade_id:
        users = users.filter(grade__id=grade_id)

    users = users.order_by('-created_on')[offset:offset+limit]

    resp = {}
    resp['students'] = UserSerializer(users, many=True).data

    grades = Grade.objects.filter(is_deleted=False)
    resp['grades'] = GradeSerializer(grades, many=True).data
    if grade_id:
        for grd in resp['grades']:
            if str(grd['id']) == str(grade_id):
                grd['selected'] = True
                break

    return prepare_response(resp)
    
def list_grades():
    grades = Grade.objects.filter(is_deleted=False)
    resp = GradeSerializer(grades, many=True).data
    return prepare_response(resp)

def get_reports(student_id, filters, user):
    student_user = get_user_by_id(student_id)
    if user != student_user and user != student_user.parent:
        raise Forbidden()

    category = filters.get('category')

    resp = {}
    resp['categories'] = []
    for tpl in ASSESSMENT_CATEGORY:
        resp['categories'].append({
            'category':tpl[1],
            'category_code':tpl[0],
            'is_selected':category == tpl[0]
        })

        if category==tpl[0]:
            resp['category'] = tpl[1]
            resp['category_code'] = tpl[0]

    if not category:
        return prepare_response(resp)

    report = get_reports_for_category(category, student_user)
    resp['reports'] = report

    return prepare_response(resp)
