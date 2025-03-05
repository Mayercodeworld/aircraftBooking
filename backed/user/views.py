from django.http import JsonResponse
from .models import UserInfo
import json
def register(request):
    try:
        if request.method == 'GET':
            print('禁止发送get请求')
            error_msg = {
                'code': 1,
                'msg': '禁止发送get请求',
            }
            return JsonResponse(error_msg, status=400)

        if request.method == 'POST':
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            print(name, email, password)

            # 这里可以添加验证逻辑，例如检查字段是否为空
            if not name or not email or not password:
                return JsonResponse({'code': 1, 'msg': '所有字段都是必填项'}, status=400)

            # 检查电子邮件是否已存在
            if UserInfo.objects.filter(email=email).exists():
                return JsonResponse({'code': 1, 'msg': '电子邮件已存在'}, status=400)

            # 创建新用户
            user = UserInfo(name=name, email=email, password=password)
            user.save()

            return JsonResponse({'code': 0, 'msg': '注册成功'}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'code': 1, 'msg': '无效的JSON格式'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'code': 1, 'msg': '注册失败'}, status=500)


def login(request):
    try:
        if request.method == 'GET':
            print('禁止发送get请求')
            error_msg = {
                'code': 1,
                'msg': '禁止发送get请求',
            }
            return JsonResponse(error_msg, status=400)

        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        print(email, password)

        # 这里可以添加验证逻辑，例如检查字段是否为空
        if not email or not password:
            return JsonResponse({'code': 1, 'msg': '所有字段都是必填项'}, status=400)

        # 检查用户是否存在
        user = UserInfo.objects.filter(email=email, password=password).first()
        if user:
            return JsonResponse({'code': 0, 'msg': '登录成功'}, status=200)
        else:
            return JsonResponse({'code': 1, 'msg': '电子邮件或密码错误'}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'code': 1, 'msg': '无效的JSON格式'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'code': 1, 'msg': '登录失败'}, status=500)