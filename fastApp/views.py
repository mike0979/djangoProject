from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_method_params(request):
    if request.method == 'GET':
        params = request.GET.lists()
        res = {
            'code': 0,
            'msg': "获取请求的参数",
            'data': dict(params)
        }
        return JsonResponse(res)

@require_http_methods(["POST"])
def login(request):
    if request.method == 'POST':
        params = request.GET.lists()
        res = {
            'code': 0,
            'msg': "获取请求的参数",
            'data': dict(params)
        }
        return JsonResponse(res)