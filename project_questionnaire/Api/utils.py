import json
from django.http.response import HttpResponse


def method_not_allowed():
    return HttpResponse(json.dumps({'msg': '方法不支持'}), status=405, content_type='application/json')


def params_error(errors):
    return HttpResponse(json.dumps(errors), status=422, content_type='application/json')


def not_authenticated():
    return HttpResponse(json.dumps({'msg': '未登录'}), status=401, content_type='application/json')


def permission_denied():
    return HttpResponse(json.dumps({'msg': '没有权限'}), status=402, content_type='application/json')


def json_response(data):
    return HttpResponse(json.dumps(data), status=200, content_type='application/json')
