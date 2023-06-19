from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from device import models
from django.http import JsonResponse
from django.forms import model_to_dict
import json
# Create your views here.

@require_http_methods(["POST", "GET"])
def device_operate(request):
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
        res = models.TblDevice.objects.all()
        json_list = []
        for i in res:
            json_dict = model_to_dict(i)
            json_list.append(json_dict)
        data = {
            "page_num": 1,
            "page_size": 10,
            "total": len(res),
            "data": json_list
        }
        return JsonResponse(data)

@require_http_methods(["GET"])
def get_device_detail(request):
    pass

@require_http_methods(["GET"])
def get_device_types(request):
    res = models.TblDeviceType.objects.all()
    json_list = []
    for i in res:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
    return JsonResponse(json_list, safe=False)

@require_http_methods(["GET"])
def get_devices(request):
    res = models.TblDevice.objects.all()
    json_list = []
    for i in res:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
    data = {
        "page_num": 1,
        "page_size": 10,
        "total": len(res),
        "data": json_list
    }
    return JsonResponse(data)