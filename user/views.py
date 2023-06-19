from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import json
from user import models
from django.core import serializers

# Create your views here.

@require_http_methods(["POST"])
def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        account = json_data.get('account')
        res = models.TblUser.objects.get(account=account)
        op_level = res.op_level
        description = res.description
        name = res.name
        id = res.id
        update_time = res.update_time.strftime('%Y%m%d %H%M%S')
        role_ids = models.TblUserRoleRel.objects.filter(user_id=id).values('role_id')
        functions = list(models.TblRoleFunctionRel.objects.filter(role_id__in=role_ids).values_list('function_id', flat=True))
        locations = list(models.TblRoleLocationRel.objects.filter(role_id__in=role_ids).values_list('location_id', flat=True))
        data = {
            "token": '69B3E86AEB5C278B5758B6F705E041C6',
            "expired_in": 600,
            "server_level": op_level,
            "id": id,
            "account": account,
            "name": name,
            "description": description,
            "status": 1,
            "op_level": op_level,
            "update_time": update_time,
            "functions": functions,
            "locations": locations,
            "devices": [
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

@require_http_methods(["GET"])
def logout(request):
    return HttpResponse(status=200)