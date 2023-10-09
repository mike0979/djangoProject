from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from opm import models
from django.core import serializers
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

@require_http_methods(["POST", "GET"])
def opm_operate(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        level_id = json_data.get('level_id')
        react = json_data.get('react')
        content = json_data.get('content')
        start_time = json_data.get('start_time')
        end_time = json_data.get('end_time')
        station_obj = json_data.get('station_obj')
        device_obj = json_data.get('device_obj')
        train_obj = json_data.get('train_obj')
        interval = json_data.get('interval')
        period = json_data.get('period')
        begin_time = json_data.get('begin_time')
        stop_time = json_data.get('stop_time')
        real_begin_time = json_data.get('real_begin_time')
        real_end_time = json_data.get('real_end_time')
        title = json_data.get('title')
        opm_level = models.TblOperationMsgLevel.objects.get(id=level_id)
        res = models.TblOperationMsg.objects.create(level_id=level_id, react=react, description=content, start_time = start_time, end_time=end_time, interval=interval, period=period, begin_time=begin_time, stop_time=stop_time, real_begin_time=real_begin_time, real_end_time=real_end_time, title=title, display_region=opm_level.display_region, play_mode=opm_level.play_mode)
        return JsonResponse({'id' : res.id})
    elif request.method == "GET":
        res = models.TblOperationMsg.objects.all().values()
        data = {
            "page_num": 1,
            "page_size": 10,
            "total": len(res),
            "data": list(res)
        }
        return JsonResponse(data)

@require_http_methods(["GET"])
def get_opm_detail(request, opm_id):
    res = models.TblOperationMsg.objects.get(id=opm_id)
    json_data = serializers.serialize('json', res)
    return HttpResponse(json_data, content_type="application/json")

@require_http_methods(["GET"])
def opm_publish(request, opm_id):
    res = models.TblOperationMsg.filter(id=opm_id).update(status=1)

@require_http_methods(["GET"])
def get_opm_level(request):
    res = models.TblOperationMsgLevel.objects.all().values()
    return JsonResponse(list(res), safe=False)

@require_http_methods(["GET"])
def get_opm(request):
    res = models.TblOperationMsg.objects.all().values()
    data = {
        "page_num": 1,
        "page_size": 10,
        "total": len(res),
        "data": list(res)
    }
    return JsonResponse(data)

@require_http_methods(["GET", "POST"])
def opm_template_operate(request):
    if request.method == "GET":
        res = models.TblOperationMsgTemplate.objects.all().values()
        data = {
            "page_num": 1,
            "page_size": 10,
            "total": len(res),
            "data": list(res)
        }
        return JsonResponse(data)
    else:
        pass

def get_opm_template(request, id):
    return None