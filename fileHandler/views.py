from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, FileResponse, JsonResponse
import os
import re
# Create your views here.

@require_http_methods(["POST"])
def upload(request):
    for file_obj in request.FILES.values():
        f = open('resource/' + file_obj.name, 'wb')  # 将客户端上传的文件保存在服务器上，一定要用wb二进制方式写入，否则文件会乱码
        for line in file_obj.chunks():  # 通过chunks分片上传存储在服务器内存中,以64k为一组，循环写入到服务器中
            f.write(line)
        f.close()
    return HttpResponse('yes')

@require_http_methods(["GET"])
def download(request, file_name):
    file_path = os.path.join('resource/', file_name)
    if not os.path.exists(file_path):
        return HttpResponse(status=404)
    file_size = os.path.getsize(file_path)
    range_header = request.META.get('HTTP_RANGE', '').strip()
    if 'HTTP_RANGE' in request.META:
        range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
        if range_match:
            range_start = int(range_match.group(1))
            range_end = int(range_match.group(2)) if range_match.group(2) else file_size - 1
        else:
            return HttpResponse(status=416)
        block_size = 1024 * 8
        with open(file_path, 'rb') as f:
            f.seek(range_start)
            block_size = min(block_size, range_end - range_start + 1)

            response = HttpResponse(
                f.read(block_size),
                status=206,
                content_type='application/octet-stream',
            )
            response['Content-Range'] = f'bytes {range_start}-{range_start + block_size - 1}/{file_size}'
            response['Accept-Ranges'] = 'bytes'
            response['Content-Length'] = str(block_size)
    else:
        response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response

# temporary function,it will be delete later
@require_http_methods(["POST"])
def upload_resource(request):
    data = {
        "id": 1,
        "name": 600,
        "description": 'op_level',
        "path": 'id',
        "size": 'account',
        "md5": 'name',
        "type": 'description',
        "resolution": 1,
        "duration": 'op_level',
        "update_time": 'update_time'
    }
    return JsonResponse(data)