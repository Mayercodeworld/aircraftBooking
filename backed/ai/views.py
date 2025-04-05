from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import StreamingHttpResponse
from .sparkai import Spark
from .openrouterai import Qwq
from .siliconflow import SiliconFlow
@api_view(['GET', 'POST'])
def get_answer_spark(request):
    # 创建一个spark实例
    spark = Spark()
    
    if request.method == 'GET':
        query = request.GET.get('query', '你是谁')  # 默认查询为 '你是谁'
        data = {
            'data': spark.spark_response(query)
        }
        return Response(data)
    
    if request.method == 'POST':
        query = request.data.get('query', '你是谁')  # 默认查询为 '你是谁'
        data = {
            'data': spark.spark_response(query)
        }
        return Response(data)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# 前端实现流式输出
@api_view(['GET', 'POST'])
def get_answer_qwq(request):
    # 创建一个spark实例
    qwq = Qwq()
    
    if request.method == 'GET':
        query = request.GET.get('query', '你是谁')  # 默认查询为 '你是谁'
        data = {
            'data': qwq.qwq_response(query)
        }
        return Response(data)
    
    if request.method == 'POST':
        query = request.data.get('query', '你是谁')  # 默认查询为 '你是谁'
        data = {
            'data': qwq.qwq_response(query)
        }
        return Response(data)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# # 后端实现流式输出
# @api_view(['GET', 'POST'])
# def get_answer_qwq(request):
#     # 创建一个qwq实例
#     qwq = Qwq()
    
#     def event_stream():
#         if request.method == 'GET':
#             query = request.GET.get('query', '你是谁')  # 默认查询为 '你是谁'
#         elif request.method == 'POST':
#             query = request.data.get('query', '你是谁')  # 默认查询为 '你是谁'
#         else:
#             return
        
#         for chunk in qwq.qwq_response(query):
#             yield chunk

#     return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

@api_view(['GET', 'POST'])
def get_answer_siliconflow(request):
    # 创建一个spark实例
    siliconflow = SiliconFlow()
    
    if request.method == 'GET':
        query = request.GET.get('query', '你是谁')  # 默认查询为 '你是谁'
        data = {
            'data': siliconflow.get_response(query)
        }
        return Response(data)
    
    if request.method == 'POST':
        query = request.data.get('query', '你是谁')  # 默认查询为 '你是谁'
        data = {
            'data': siliconflow.get_response(query)
        }
        return Response(data)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)