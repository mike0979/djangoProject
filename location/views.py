from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from location import models
from django.http import JsonResponse, HttpResponse
import json
import datetime
# Create your views here.

@require_http_methods(['POST', 'GET', 'PUT', 'DELETE'])
def station_operate(request, id=None):
    if id == None:
        if request.method == "GET":
            line_id = request.GET.get('line')
            if line_id == None:
                res = models.TblStation.objects.all().values()
                return JsonResponse(list(res), safe=False)
            else:
                res = models.TblStation.objects.filter(line_id=line_id).values()
                return JsonResponse(list(res), safe=False)
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
            res = models.TblLocation.objects.create(user_type=1, code=code, name=name, parent_id=line_id, location_type_id=2000, description=description, create_time=datetime.datetime.now())
            types = models.TblLocationType.objects.filter(parent_id=2000)
            for type in types:
                models.TblLocation.objects.create(user_type=1, code=type.code, name=type.name, location_type_id=type.id, parent_id=res.id)
            models.TblStation.objects.create(id=res.id, user_type=1, code=code, name=name, name_en=name_en, description=description, line_id=line_id, position=position, cross_station_ids=cross, diagram=diagram, create_time=datetime.datetime.now())
            return JsonResponse({'id' : res.id})
    else:
        if request.method == "GET":
            res = models.TblStation.objects.filter(id=id).values()
            return JsonResponse(list(res), safe=False)
        elif request.method == "PUT":
            json_data = json.loads(request.body)
            code = json_data.get('code')
            name = json_data.get('name')
            description = json_data.get('description')
            name_en = json_data.get('name_en')
            position = json_data.get('position')
            line_id = json_data.get('line_id')
            cross = json_data.get('cross_station_ids')
            diagram = json_data.get('three_dime_diagram')
            models.TblStation.objects.filter(id).update(code=code, name=name, name_en=name_en, description=description, line_id=line_id, position=position, cross_station_ids=cross, diagram=diagram)
        else:
            models.TblStation.objects.filter(id=id).delete()
            models.TblLocation.objects.filter(parent_id=id).delete()
            models.TblLocation.objects.filter(id=id).delete()
            return HttpResponse(status=200)

@require_http_methods(["POST","GET","PUT","DELETE"])
def line_operate(request, id=None):
    if id == None:
        if request.method == "GET":
            res = models.TblLine.objects.all().values()
            return JsonResponse(list(res), safe=False)
        elif request.method == "POST":
            json_data = json.loads(request.body)
            code = json_data.get('code')
            name = json_data.get('name')
            description = json_data.get('description')
            name_en = json_data.get('name_en')
            back_image = json_data.get('back_image')
            res = models.TblLocation.objects.create(user_type=1, code=code, name=name, location_type_id=1000, description=description)
            models.TblLine.objects.create(id=res.id, user_type=1, code=code, name=name, name_en=name_en, description=description, back_image=back_image, create_time=datetime.datetime.now())
            return JsonResponse({'id' : res.id})
    else:
        if request.method == "GET":
            res = models.TblLine.objects.filter(id=id).values()
            return JsonResponse(list(res), safe=False)
        elif request.method == "PUT":
            json_data = json.loads(request.body)
            code = json_data.get('code')
            name = json_data.get('name')
            description = json_data.get('description')
            name_en = json_data.get('name_en')
            back_image = json_data.get('back_image')
            models.TblLine.objects.filter(id).update(code=code, name=name, name_en=name_en, description=description, back_image=back_image, update_time=datetime.datetime.now())
        else:
            models.TblLine.objects.filter(id=id).delete()
            models.TblLocation.objects.filter(parent_id=id).delete()
            models.TblLocation.objects.filter(id=id).delete()
            return HttpResponse(status=200)

@require_http_methods(["GET"])
def get_locations(request):
    res = models.TblLocation.objects.all().values()
    return JsonResponse(list(res), safe=False)

@require_http_methods(["GET"])
def get_location_types(request):
    res = models.TblLocationType.objects.all().values()
    return JsonResponse(list(res), safe=False)