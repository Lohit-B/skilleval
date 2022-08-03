from apis.models import User, Grade
from apis.serializers.user import UserSerializer, GradeSerializer
from apis.helpers.utility import prepare_response, generate_jwt
from apis.helpers.exceptions import BadRequest, Forbidden
import string
import random
N = 7

def get_profile(user):
    return prepare_response(UserSerializer(user).data)

def get_user_by_id(user_id):
    return User.objects.filter(id=user_id, is_deleted=False).first()

def get_user_by_username(username):
    user_id = username.split('_')[1]
    return User.objects.filter(id=user_id, is_deleted=False).first()

def login(username, password):
    user_id = username.split('_')[1]
    user = User.objects.filter(id=user_id, is_deleted=False)
    if not user:
        raise BadRequest("Use Doesn't Exist")

    user = user.first()
    if user.password != password:
        raise BadRequest("Invalid Credentials")

    data = {'user_id':user.id}
    jwt = generate_jwt(data)
    resp = {'auth_token':jwt}
    return prepare_response(resp)

def create_bulk_students(data, user):
    if not user.is_institute:
        raise Forbidden()

    grade_id = data['grade']
    grade = Grade.objects.get(id=grade_id)

    count  = int(data.get('count', 1))
    total_accounts = []
    for i in range(count):
        total_accounts.append(User(
            password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N)),
            is_student = True,
            parent = user,
            grade = grade
        ))

    accounts = User.objects.bulk_create(total_accounts)

    data = UserSerializer(accounts, many=True).data
    return prepare_response(data)

def update_student(data, user):
    to_update = user
    username = data.get('username')
    if username:
        to_update = get_user_by_username(username)

    if to_update != user and to_update.parent != user:
        raise Forbidden()

    if data.get('first_name'):to_update.first_name = data.get('first_name')
    if data.get('last_name'):to_update.last_name = data.get('last_name')
    if data.get('password'):to_update.password= data.get('password')

    to_update.save()
    return prepare_response(UserSerializer(to_update).data)

