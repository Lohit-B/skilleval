from apis.models import User
from django.conf import settings
import jwt

from datetime import timedelta, datetime

def prepare_response(data, session=None):
    resp = {}
    resp['data'] = data
    if session:
        resp['ag_session'] = {'name':session.ag_name}
    return resp

def generate_jwt(data):
    now = datetime.now()
    exp_time = now + timedelta(days=7)
    secret = settings.JWT['secret']
    algo = settings.JWT['algorithm']
    data['exp'] = exp_time
    data['iat'] = int(now.timestamp())
    return jwt.encode(data, secret, algorithm=algo)

def decode_jwt(token):
    secret = settings.JWT['secret']
    algo = settings.JWT['algorithm']
    payload = jwt.decode(token, secret, algorithms=algo)
    return payload

