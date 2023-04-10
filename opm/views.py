from django.shortcuts import render

# Create your views here.

from django.views.decorators.http import require_http_methods
from opm import models
from django.core import serializers
from django.http import JsonResponse, HttpResponse
import json

@require_http_methods(["POST", "GET"])
def opm_operate(request):
    if request.method == "GET":
        res = models.TblOperationMsg.objects.all()
        json_data = serializers.serialize('json', res)
        return HttpResponse(json_data, content_type="application/json")
    elif request.method == "POST":
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

        res = models.TblOperationMsg.objects.create(level_id=level_id, react=react, content = content, start_time = start_time, end_time=end_time, interval=interval, period=period, begin_time=begin_time, stop_time=stop_time, real_begin_time=real_begin_time, real_end_time=real_end_time, title=title)
        return JsonResponse({'id' : res.id})

@require_http_methods(["GET"])
def get_opm_detail(request, opm_id):
    res = models.TblOperationMsg.objects.get(id=opm_id)
    json_data = serializers.serialize('json', res)
    return HttpResponse(json_data, content_type="application/json")

@require_http_methods(["GET"])
def opm_publish(request, opm_id):
    res = models.TblOperationMsg.filter(id=opm_id).update(status=1)