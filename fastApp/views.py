from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import json
from fastApp import models
from django.core import serializers

@require_http_methods(["POST"])
def login(request):
    if request.method == 'POST':
        res = json.loads(request.body)
        data = {
            "token": "69B3E86AEB5C278B5758B6F705E041C6",
            "expired_in": 60,
            "server_level": 0,
            "id": 1,
            "account": "admin",
            "name": "管理员",
            "description": "",
            "status": 1,
            "op_level": 1,
            "update_time": "20160510 121030",
            "functions": [
                1, 2
            ],
            "locations": [
                1
            ],
            "devices": [
                2, 3, 4
            ]}
        return JsonResponse(data)

@require_http_methods(["POST", "GET"])
def user_operate(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        account = json_data.get('account')
        name = json_data.get('name')
        description = json_data.get('description')
        password = json_data.get('password')
        status = json_data.get('status')
        op_level = json_data.get('op_level')
        roles = json_data.get('roles')
        res = models.TblUser.objects.create(account = account, name = name, description = description, password = password, status = status, op_level = op_level, password_wrong_num = 0, flag = 0)
        for role in roles:
            models.TblUserRoleRel.objects.create(user_id=res.id, role_id=role)
        return JsonResponse({'id' : res.id})
    if request.method == 'GET':
        res = models.TblUser.objects.all()
        json_data = serializers.serialize('json', res)
        return HttpResponse(json_data, content_type="application/json")