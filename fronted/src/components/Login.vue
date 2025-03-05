<script setup>
import { ref, onMounted } from 'vue';
import axios  from "axios";

const isRegisterMode = ref(false);

const name = ref('');
const email = ref('');
const password = ref('');

// let csrfToken = ref('');

onMounted(() => {
  isRegisterMode.value = false;
});

const toggleMode = () => {
  isRegisterMode.value = !isRegisterMode.value;
};

const ClearForm = () => {
  name.value = '';
  email.value = '';
  password.value = '';
};

const handleSubmit = (event) => {
  event.preventDefault();  // 阻止表单的默认提交行为
  // 注册逻辑
  if (isRegisterMode.value) {
    let request = {
      name: name.value,
      email: email.value,
      password: password.value,
    };
    console.log(request);
    axios.post('http://127.0.0.1:8000/api/register/', request)
       .then(response => {
         if (response.data.code === 0) {
           alert('注册成功');
           ClearForm();
           window.location.href = '/login';
         } else {
           alert(response.data.data.error);
         }
       })
       .catch(error => {
         if (error.response) {
           // 请求已发出但服务器响应的状态码不在 2xx 范围内
           alert(`请求错误: ${error.response.data.data()}`);
         } else if (error.request) {
           // 请求已发出但没有收到响应
           alert('请求已发出，但没有收到响应');
         } else {
           // 一些设置请求时发生错误
           alert('一些设置请求时发生错误');
         }
         console.error('请求失败:', error);
       });
  }

  // 处理登录逻辑
  if(isRegisterMode.value === false){
    event.preventDefault();  // 阻止表单的默认提交行为
    let request = {
      email: email.value,
      password: password.value,
    };
    axios.post('http://127.0.0.1:8000/api/login/', request)
      .then(response => {
        if (response.data.code === 0) {
          alert('登录成功');
          ClearForm();
          window.location.href = '/';
        } else {
          alert(response.data.data.error);
        }
      })
    .catch(error => {
      if (error.response) {
        // 请求已发出但服务器响应的状态码不在 2xx 范围内
        alert(`请求错误: ${error.response.data.data()}`);
      } else if (error.request) {
        // 请求已发出但没有收到响应
        alert('请求已发出，但没有收到响应');
      } else {
        // 一些设置请求时发生错误
        alert('一些设置请求时发生错误');
      }
      console.error('请求失败:', error);
    });
  }
};


</script>

<template>
    <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company" />
        <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">{{ isRegisterMode ? 'Register for an account' : 'Sign in to your account' }}</h2>
      </div>

      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" action="#" method="POST">

          <div v-if="isRegisterMode">
          <label for="name" class="block text-sm font-medium text-gray-900">名字</label>
          <div class="mt-2">
                                                                                <!-- 使用v-model绑定到name变量   -->
            <input type="text" name="name" id="name" autocomplete="name" required  v-model="name" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm" placeholder="请输入你的名字"/>
          </div>
        </div>

          <div>
            <label for="email" class="block text-sm/6 font-medium text-gray-900">电子邮件</label>
            <div class="mt-2">
              <input type="email" name="email" id="email" autocomplete="email" required v-model="email" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" placeholder="请输入你的电子邮件"/>
            </div>
          </div>

          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm/6 font-medium text-gray-900" >密码</label>
              <div class="text-sm">
                <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">忘记密码?</a>
              </div>
            </div>
            <div class="mt-2">
              <input type="password" name="password" id="password" autocomplete="current-password" required v-model="password" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" placeholder="请输入你的密码"/>
            </div>
          </div>

          <div>
            <button type="submit" @click="handleSubmit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">{{ isRegisterMode ? '注册' : '登录' }}</button>
          </div>
        </form>

        <p class="mt-10 text-center text-sm/6 text-gray-500">
          {{ isRegisterMode ? '拥有账号  ' : '没有账号?' }}
        <button @click="toggleMode" class="font-semibold text-indigo-600 hover:text-indigo-500">
          {{ isRegisterMode ? '登录' : '注册' }}
        </button>
        </p>
      </div>
    </div>
  </template>

  <style scoped>

  </style>
