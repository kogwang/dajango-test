import json


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse


@api_view(http_method_names=['GET','POST'])
def login1(request):
    if request.method == 'GET':
        userName = request.GET.get('userName')
        password = request.GET.get('password')
        if userName == 'xiaowang' and password=='123456':
            data = {
                'msg':'登录成功',
                'code':200
            }
            return HttpResponse(json.dumps(data,ensure_ascii=False),content_type="application/json,charset=utf-8")
        else:
            data = {
                'msg':'登录失败',
                'code':0
            }
            return JsonResponse(data)



