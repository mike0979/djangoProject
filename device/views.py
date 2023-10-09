from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from device import models
from location.models import TblLocation
from django.http import JsonResponse, HttpResponse
from django.db.models import OuterRef, Subquery
import json
# Create your views here.

@require_http_methods(["POST","GET","PUT","DELETE"])
def device_operate(request, id=None):
    if id == None:
        if request.method == "POST":
            json_data = json.loads(request.body)
            code = json_data.get('code')
            name = json_data.get('name')
            description = json_data.get('description')
            line_id = json_data.get('line_id')
            host_device_id = json_data.get('host_device_id')
            device_type = json_data.get('device_type')
            location_id = json_data.get('location_id')
            station_id = json_data.get('station_id')
            life_cycle = json_data.get('life_cycle')
            ip = json_data.get('ip')
            mac = json_data.get('mac')
            resolution = json_data.get('resolution')
            service_time = json_data.get('service_time')
            power_device = json_data.get('power_device')
            power_num = json_data.get('power_num')
            line_type = json_data.get('line_type')
            device_type = models.TblDeviceType.objects.get(id=device_type)
            res = models.TblDevice.objects.create(user_id=2, user_type=1, code=code, name=name, description=description, line_id=line_id, host_device_id=host_device_id, device_type=device_type, location_id=location_id, station_id=station_id, life_cycle=life_cycle, ip=ip, mac=mac, resolution=resolution, service_time=service_time, power_device=power_device, power_num=power_num, line_type=line_type)
            return JsonResponse({'id' : res.id})
        elif request.method == "GET":
            subquery = TblLocation.objects.filter(id=OuterRef('location_id'))
            res = models.TblDevice.objects.annotate(location_type_id=Subquery(subquery.values('location_type_id'))).values()

            data = {
                "page_num": 1,
                "page_size": 10,
                "total": len(res),
                "data": list(res)
            }
            return JsonResponse(data)
    else:
        if request.method == "GET":
            pass
        elif request.method == "PUT":
            pass
        elif request.method == "DELETE":
            models.TblDevice.objects.filter(id=device_id).delete()
            return HttpResponse(status=200)

@require_http_methods(["GET"])
def get_device_types(request):
    res = models.TblDeviceType.objects.all().values()
    return JsonResponse(list(res), safe=False)