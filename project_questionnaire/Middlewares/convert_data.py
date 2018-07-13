import json

from django.utils.deprecation import MiddlewareMixin
from django.http.multipartparser import MultiPartParser

from Api.utils import params_error


class MethodConvertMiddleware(MiddlewareMixin):
    '''
    自定义method方法
    '''

    def process_request(self, request):
        method = request.method
        if 'application/json' in request.content_type:
            # 把客户端上传的json数据转化成python字典
            try:
                data = json.loads(request.body.decode())
                files = None
            except Exception as e:
                return params_error({
                    'body': '请求数据类型不正确'
                })
        elif 'multipart/form-data' in request.content_type:
            # 把客户端已formdata上传的数据进行解析,通常客户端会把上传的文件也放在formdata中,
            # 所以下面的解析会把上传的文件也解析出来
            data, files = MultiPartParser(
                request.META, request, request.upload_handlers).parse()
        else:
            data = request.GET
            files = None

        if 'HTTP_X_METHOD' in request.META:
            method = request.META['HTTP_X_METHOD'].upper()
            setattr(request, 'method', method)

        if files:
            setattr(request, '{method}_FILES'.format(method=method), files)
        setattr(request, method, data)