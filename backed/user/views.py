from django.http import JsonResponse
from .models import UserInfo
import json
import time
import hashlib

def create_hash_password(password,salt):
    # 第一次哈希：对密码进行哈希处理
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    # 第二次哈希：将 salt 和第一次哈希的结果拼接后再次进行哈希处理
    hash_password = hashlib.sha256((salt + password_hash).encode()).hexdigest()
    return hash_password

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

            # 这里可以添加验证逻辑，例如检查字段是否为空
            if not name or not email or not password:
                return JsonResponse({'code': 1, 'msg': '所有字段都是必填项'}, status=400)

            # 检查电子邮件是否已存在
            if UserInfo.objects.filter(email=email).exists():
                return JsonResponse({'code': 1, 'msg': '电子邮件已存在'}, status=400)

            #通过时间戳来定义salt
            salt = str(int(time.time()))

            hash_password = create_hash_password(password,salt)

            # 创建新用户
            user = UserInfo(name=name, email=email, password=hash_password,salt=salt)
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

        head_data = json.loads(request.body)
        head_email = head_data.get('email')
        head_password = head_data.get('password')

        # 这里可以添加验证逻辑，例如检查字段是否为空
        if not head_email or not head_password:
            return JsonResponse({'code': 1, 'msg': '所有字段都是必填项'}, status=400)
        # 检查用户是否存在
        user = UserInfo.objects.filter(email=head_email).first()
        if user:
            # 获取存储的 salt 和 db_hash_password
            db_id = user.id
            db_salt = user.salt
            db_hash_password = user.password
            # 让前端传入的密码也形成hash之后的密码
            head_hash_password = create_hash_password(head_password,db_salt)

            # 比较生成的 head_hash_password 和存储的 db_hash_password
            if head_hash_password == db_hash_password:
                return JsonResponse({'code': 0, 'msg': '登录成功', 'id': db_id, 'token': head_hash_password}, status=200)
            else:
                return JsonResponse({'code': 1, 'msg': '电子邮件或密码错误'}, status=400)
        else:
            return JsonResponse({'code': 1, 'msg': '电子邮件或密码错误'}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'code': 1, 'msg': '无效的JSON格式'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'code': 1, 'msg': '登录失败'}, status=500)

def get_user_token(request, user_id):
    try:
        user = UserInfo.objects.get(id=user_id)
        return JsonResponse({'password': user.password}, status=200)
    except UserInfo.DoesNotExist:
        return JsonResponse({'code': 1, 'msg': '用户不存在'}, status=404)
    except Exception as e:
        print(e)
        return JsonResponse({'code': 1, 'msg': '获取用户信息失败'}, status=500)