from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from location import models
from django.http import JsonResponse
from django.forms import model_to_dict
import json
# Create your views here.

@require_http_methods(["POST", "GET"])
def station_operate(request):
    if request.method == "GET":
        res = models.TblLine.objects.all()
        json_list = []
        for i in res:
            json_dict = model_to_dict(i)
            json_list.append(json_dict)
        return JsonResponse(json_list, safe=False)
    elif request.method == "POST":
        json_data = json.loads(request.body)
        code = json_data.get('code')
        name = json_data.get('name')
        description = json_data.get('description')
        name_en = json_data.get('name_en')
        position = json_data.get('position')
        line_id = json_data.get('line_id')
        cross = json_data.get('cross_station_ids')
        diagram = json_data.get('three_dime_diagram')
        res = models.TblLocation.objects.create(user_type=1, code=code, name=name, parent_id=line_id, location_type_id=2000, description=description)
        types = models.TblLocationType.objects.filter(parent_id=2000)
        for type in types:
            models.TblLocation.objects.create(user_type=1, code=type.code, name=type.name, location_type_id=type.id,parent_id=res.id)
        models.TblStation.objects.create(id=res, user_type=1, code=code, name=name, name_en=name_en, description=description, position=position, cross_station_ids=cross, diagram=diagram)
        return JsonResponse({'id' : res.id})

@require_http_methods(["POST", "GET"])
def line_operate(request):
    if request.method == "GET":
        res = models.TblLine.objects.all()
        json_list = []
        for i in res:
            json_dict = model_to_dict(i)
            json_list.append(json_dict)
        return JsonResponse(json_list, safe=False)
    elif request.method == "POST":
        json_data = json.loads(request.body)
        code = json_data.get('code')
        name = json_data.get('name')
        description = json_data.get('description')
        name_en = json_data.get('name_en')
        back_image = json_data.get('back_image')
        res = models.TblLocation.objects.create(user_type=1, code=code, name=name, location_type_id=1000, description=description)
        models.TblLine.objects.create(id=res, user_type=1, code=code, name=name, name_en=name_en, description=description, back_image=back_image)
        return JsonResponse({'id' : res.id})

@require_http_methods(["POST", "GET"])
def get_locations(request):
    res = models.TblLocation.objects.all()
    json_list = []
    for i in res:
        json_dict = model_to_dict(i)
        json_dict['location_type_id'] = json_dict['location_type']
        json_dict['parent_id'] = json_dict['parent']
        json_list.append(json_dict)
    return JsonResponse(json_list, safe=False)

@require_http_methods(["POST", "GET"])
def get_location_types(request):
    res = models.TblLocationType.objects.all()
    json_list = []
    for i in res:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
    return JsonResponse(json_list, safe=False)