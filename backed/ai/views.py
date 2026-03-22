from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import StreamingHttpResponse
from .sparkai import Spark
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