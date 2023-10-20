from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from opm import models
from django.http import JsonResponse, HttpResponse
import json
from ws.consumers import send_message_to_client
import datetime
# Create your views here.

@require_http_methods(["POST", "GET", "PUT", "DELETE"])
def opm_operate(request, id=None):
    if id == None:
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
            res = models.TblOperationMsg.objects.create(level_id=level_id, react=react, description=content,
                                                        start_time=start_time, end_time=end_time, interval=interval,
                                                        period=period, begin_time=begin_time, stop_time=stop_time,
                                                        real_begin_time=real_begin_time, real_end_time=real_end_time,
                                                        title=title, display_region=opm_level.display_region,
                                                        play_mode=opm_level.play_mode, update_time=datetime.datetime.now())
            for device_id in device_obj:
                models.TblOperationMsgDeviceRel.objects.create(device_id=device_id, type=0, operation_msg_id=res.id,
                                                               result=1)
            for train_id in train_obj:
                models.TblOperationMsgDeviceRel.objects.create(device_id=train_id, type=1, operation_msg_id=res.id,
                                                               result=1)
            return JsonResponse({'id': res.id})
        elif request.method == "GET":
            page_num = request.GET.get('page_num')
            page_size = request.GET.get('page_size')
            res = models.TblOperationMsg.objects.all().values()
            data = {
                "page_num": page_num,
                "page_size": page_size,
                "total": len(res),
                "data": list(res)
            }
            return JsonResponse(data)
    else:
        if request.method == "GET":
            res = models.TblOperationMsg.objects.filter(id=id).values()
            return JsonResponse(list(res), safe=False)
        elif request.method == "DELETE":
            models.TblOperationMsgDeviceRel.objects.filter(operation_msg_id=id).delete()
            models.TblOperationMsg.objects.filter(id=id).delete()
            return HttpResponse(status=200)

@require_http_methods(["POST"])
def opm_publish(request, opm_id):
    res = models.TblLine.objects.filter(tbldevice__tbloperationmsgdevicerel__operation_msg_id=opm_id).values('code').distinct()
    # query2 = models.TblLine.objects.filter(train__operationmsgdevicerel__operation_msg_id=opm_id).values('code').distinct()
    # res = query1.union(query2)
    models.TblOperationMsg.objects.filter(id=opm_id).update(status=1, update_time=datetime.datetime.now())
    # 调用函数发送消息
    for item in list(res):
        send_message_to_client(item['code'], {
            "code": 1009,
            "id": opm_id,
            "operate_type": 1
        })
    return HttpResponse(status=200)

@require_http_methods(["GET"])
def get_opm_level(request):
    res = models.TblOperationMsgLevel.objects.all().values()
    return JsonResponse(list(res), safe=False)

@require_http_methods(["GET", "POST"])
def opm_template_operate(request):
    if request.method == "GET":
        page_num = request.GET.get('page_num')
        page_size = request.GET.get('page_size')
        res = models.TblOperationMsgTemplate.objects.all().values()
        data = {
            "page_num": page_num,
            "page_size": page_size,
            "total": len(res),
            "data": list(res)
        }
        return JsonResponse(data)
    else:
        pass

def get_opm_template(request, id):
    return None
