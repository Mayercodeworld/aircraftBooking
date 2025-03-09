from django.http import JsonResponse
from .models import UserInfo
from rest_framework.decorators import api_view
import json
import time
import hashlib
import random
import string
#加密
def create_hash_password(password,salt):
    # 第一次哈希：对密码进行哈希处理
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    # 第二次哈希：将 salt 和第一次哈希的结果拼接后再次进行哈希处理
    hash_password = hashlib.sha256((salt + password_hash).encode()).hexdigest()
    return hash_password

#生成随机密码
def generate_random_password(length=8):
    # 定义字母和数字的集合
    characters = string.ascii_letters + string.digits
    # 随机选择字符
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@api_view(['POST', 'GET'])
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
                return JsonResponse({'code': 1, 'msg': '所有字段都是必填项'}, status=401)


            #检查姓名是否已存在
            if UserInfo.objects.filter(name=name).exists():
                return JsonResponse({'code': 1, 'msg': '姓名已存在'}, status=402)

            # 检查电子邮件是否已存在
            if UserInfo.objects.filter(email=email).exists():
                return JsonResponse({'code': 1, 'msg': '电子邮件已存在'}, status=403)
            #检查电子邮箱符合规则
            if '@' not in email:
                return JsonResponse({'code': 1, 'msg': '电子邮件格式不正确'}, status=404)
            if len(email) > 30:
                return JsonResponse({'code': 1, 'msg': '电子邮件长度不能超过30位'}, status=405)
            if len(email) < 6:
                return JsonResponse({'code': 1, 'msg': '电子邮件长度不能小于6位'}, status=406)


            # #检查密码不能太简单
            # if len(password) < 6:
            #     return JsonResponse({'code': 1, 'msg': '密码长度不能小于6位'}, status=407)
            # if password.isdigit() or password.isalpha():
            #     return JsonResponse({'code': 1, 'msg': '密码不能全是数字或字母'}, status=408)
            # if password.isupper():
            #     return JsonResponse({'code': 1, 'msg': '密码不能全是大写字母'}, status=409)
            # if password.islower():
            #     return JsonResponse({'code': 1, 'msg': '密码不能全是小写字母'}, status=410)
            # if password.isspace():
            #     return JsonResponse({'code': 1, 'msg': '密码不能全是空格'}, status=411)


            #通过时间戳来定义salt
            salt = str(int(time.time()))

            hash_password = create_hash_password(password,salt)

            # 创建新用户
            user = UserInfo(name=name, email=email, password=hash_password,salt=salt)
            user.save()

            return JsonResponse({'code': 0, 'msg': '注册成功'}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'code': 1, 'msg': '无效的JSON格式'}, status=412)
    except Exception as e:
        print(e)
        return JsonResponse({'code': 1, 'msg': '注册失败'}, status=413)

@api_view(['POST' ,'GET'])
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
            return JsonResponse({'code': 1, 'msg': '所有字段都是必填项'}, status=401)
        # 检查用户是否存在
        user = UserInfo.objects.filter(email=head_email).first()
        if user:
            # 获取存储的 salt 和 db_hash_password
            db_id = user.id
            db_salt = user.salt
            db_hash_password = user.password
            db_name = user.name
            db_email = user.email
            # 让前端传入的密码也形成hash之后的密码
            head_hash_password = create_hash_password(head_password,db_salt)

            # 比较生成的 head_hash_password 和存储的 db_hash_password
            print("head_hash_password:",head_hash_password)
            print("db: ",db_hash_password)
            if head_hash_password == db_hash_password:
                return JsonResponse({'code': 0, 'msg': '登录成功', 'id': db_id, 'token': head_hash_password, 'name': db_name, 'email': db_email}, status=200)
            else:
                return JsonResponse({'code': 1, 'msg': '密码错误'}, status=402)
        else:
            return JsonResponse({'code': 1, 'msg': '你的账号还未注册'}, status=403)

    except json.JSONDecodeError:
        return JsonResponse({'code': 1, 'msg': '无效的JSON格式'}, status=405)
    except Exception as e:
        print(e)
        return JsonResponse({'code': 1, 'msg': '登录失败'}, status=500)
@api_view(['GET'])
def get_user_token(request, user_id):
    try:
        user = UserInfo.objects.get(id=user_id)
        return JsonResponse({'password': user.password}, status=200)
    except UserInfo.DoesNotExist:
        return JsonResponse({'code': 1, 'msg': '用户不存在'}, status=404)
    except Exception as e:
        print(e)
        return JsonResponse({'code': 1, 'msg': '获取用户信息失败'}, status=500)


@api_view(['POST'])
def update_user_info(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('id')  # 假设前端传递了用户ID
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if not user_id:
            return JsonResponse({'code': 1, 'msg': '缺少用户ID'}, status=400)

        # #检查密码难度
        # if len(password) < 6:
        #     return JsonResponse({'code': 1, 'msg': '密码长度不能小于6位'}, status=407)
        # if password.isdigit() or password.isalpha():
        #     return JsonResponse({'code': 1, 'msg': '密码不能全是数字或字母'}, status=408)
        # if password.isupper():
        #     return JsonResponse({'code': 1, 'msg': '密码不能全是大写字母'}, status=409)
        # if password.islower():
        #     return JsonResponse({'code': 1, 'msg': '密码不能全是小写字母'}, status=410)
        # if password.isspace():
        #     return JsonResponse({'code': 1, 'msg': '密码不能全是空格'}, status=411)

        # 检查姓名是否已存在
        if UserInfo.objects.filter(name=name).exists() and UserInfo.objects.get(id=user_id).name != name:
            return JsonResponse({'code': 1, 'msg': '姓名已存在'}, status=402)
        # 检查电子邮件是否已存在
        if UserInfo.objects.filter(email=email).exists() and UserInfo.objects.get(id=user_id).email != email:
            return JsonResponse({'code': 1, 'msg': '电子邮件已存在'}, status=403)
        # 检查电子邮箱符合规则
        if '@' not in email:
            return JsonResponse({'code': 1, 'msg': '电子邮件格式不正确'}, status=404)
        if len(email) > 30:
            return JsonResponse({'code': 1, 'msg': '电子邮件长度不能超过30位'}, status=405)
        if len(email) < 6:
            return JsonResponse({'code': 1, 'msg': '电子邮件长度不能小于6位'}, status=406)

        # 获取用户对象
        try:
            user = UserInfo.objects.get(id=user_id)
        except UserInfo.DoesNotExist:
            return JsonResponse({'code': 1, 'msg': '用户不存在'}, status=408)

        salt = user.salt
        hash_password = create_hash_password(password, salt)


        # 更新用户信息
        user.name = name
        user.email = email

        #如果密码和密码相同，则不更新密码
        if hash_password == user.password:
            return JsonResponse({'code': 1, 'msg': '密码相同，不需要更改'}, status=407)
        else:
            # 通过时间戳来定义salt
            salt = str(int(time.time()))
            user.password = create_hash_password(password, salt)
            user.salt = salt
            print("密码更新了", user.password)
        user.save()

        return JsonResponse({'code': 0, 'msg': '更新成功', 'token': salt}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'code': 1, 'msg': '无效的JSON格式'}, status=412)
    except Exception as e:
        print(e)
        return JsonResponse({'code': 1, 'msg': '更新失败'}, status=500)


@api_view(['POST'])
def forget_password(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        name = data.get('name')
        print("走到了这里")
        #检查姓名是否存在
        if not UserInfo.objects.filter(name=name).exists():
            return JsonResponse({'code': 1, 'msg': '用户不存在'}, status=410)
        #姓名存在，看电子邮箱是否一致
        if UserInfo.objects.filter(name=name).exists() and UserInfo.objects.get(name=name).email != email:
            return JsonResponse({'code': 1, 'msg': '电子邮箱不匹配'}, status=405)
        #一致，就生成一个8位数的随机密码
        random_password = generate_random_password()
        salt = str(int(time.time()))
        hash_password = create_hash_password(random_password, salt)
        #把salt 和 hash_password 存到数据库中
        user = UserInfo.objects.get(name=name)
        user.password = hash_password
        user.salt = salt
        user.save()
        #返回随机密码
        return JsonResponse({'code': 0, 'msg': '已生成随机密码', 'password': random_password}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({'code': 1, 'msg': '无效的JSON格式'}, status=412)
    except UserInfo.DoesNotExist:
        return JsonResponse({'code': 1, 'msg': '用户不存在'}, status=404)
    except Exception as e:
        print(f"An error occurred: {e}")
        return JsonResponse({'code': 1, 'msg': '密码重置失败'}, status=500)