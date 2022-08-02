from urllib.parse import urlparse
from django.http.request import QueryDict
from django.shortcuts import redirect
from web.helpers.exceptions import *

def next_page_url(request, inc=1):
    url = request.build_absolute_uri()
    url_obj = urlparse(url)
    query = url_obj.query

    qdict = QueryDict(query, mutable=True)
    qdict.__setitem__('page', int(request.GET.get('page') or 1) + inc)
    updated_query = qdict.urlencode()
    url_obj = url_obj._replace(query=updated_query)
    
    return url_obj.geturl()

def include_page_info(data_list, data_obj, request, size=10):
    size = request.GET.get('size', 10)
    if len(data_list) >= int(size):
        data_obj['next_page'] = next_page_url(request)
    if int(request.GET.get('page') or 1) > 1:
        data_obj['prev_page'] = next_page_url(request, -1)

def set_auth_status(f):
    def wrapper(*args, **kwargs):
        request = args[0]
        cookies = request.META.get("HTTP_COOKIE")
        if not cookies:
            return f(*args, **kwargs)

        kv_str_arr = cookies.split(';')
        kv_array = [kv.strip().split("=") for kv in kv_str_arr]
        jwt = None
        for kv in kv_array:
            if kv[0]=='jwt': jwt = kv[1]

        if jwt=='null' or not jwt:
            return f(*args, **kwargs)

        request.META['HTTP_AUTHORIZATION'] = jwt
        request.__setattr__('is_loggedin', True)
        return f(*args, **kwargs)

    return wrapper
    
def set_auth_header(f):
    def wrapper(*args, **kwargs):
        request = args[0]
        url = request.build_absolute_uri()
        cookies = request.META.get("HTTP_COOKIE")
        if not cookies:
            return redirect('/users/signin?redirect=%s' % url)

        kv_str_arr = cookies.split(';')
        kv_array = [kv.strip().split("=") for kv in kv_str_arr]
        jwt = None
        for kv in kv_array:
            if kv[0]=='jwt': jwt = kv[1]

        if jwt=='null' or not jwt:
            return redirect('/users/signin?redirect=%s' % url)

        request.META['HTTP_AUTHORIZATION'] = jwt
        request.__setattr__('is_loggedin', True)
        return f(*args, **kwargs)

    return wrapper
    

def handle_response(func):
    def wrapper(*a, **kw):
        try:
            return func(*a, **kw)
        except JWTTokenExpired as ej:
            return redirect('/users/signin')
        except Exception as e2:
            raise e2

    return wrapper
    
def parse_api_response(resp):
    data = resp.data
    if resp.status_code < 300:
        return data

    if data and data.get('code') == "AUTH_REQUIRED":
        raise JWTTokenExpired()

    raise Exception(data)
