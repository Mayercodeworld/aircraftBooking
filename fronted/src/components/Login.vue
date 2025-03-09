<script setup>
import { ref, onMounted } from 'vue';
import {useAuthStore} from '../stores/user_store.js'
import axios  from "axios";
import Cookies from 'js-cookie';
const authStore = useAuthStore();

const name = ref('');
const email = ref('');
const password = ref('');


const old_name = ref('');
const old_email = ref('');
const get_new_password = ref(false);

onMounted(() => {
});

const toggleMode = () => {
  authStore.toggleRegisterMode();
};

const ClearForm = () => {
  name.value = '';
  email.value = '';
  password.value = '';
};
const confirmPassword = () => {
  console.log('old_name:', old_name.value);
  console.log('old_email:', old_email.value);
    if(old_name.value  && old_email.value)
    {
      let request = {
        name : old_name.value,
        email: old_email.value,
      };
      axios.post('http://127.0.0.1:8000/api/user/forget/', request)
        .then(response => {
          if (response.data.code === 0) {
          alert('重置的密码: ' + response.data.password);
          } else {
            alert(response.data.data.error);
          }
        })
        .catch(error => {
        if (error.response) {
          alert(error.response.data.msg);
        } else if (error.request) {
          alert('请求已发出，但没有收到响应');
        } else {
          alert('一些设置请求时发生错误');
        }
        console.error('请求失败:', error);
      });
    }
    closeModal();
};
const closeModal = () => {
  // 关闭模态框的逻辑
  old_name.value = '';
  old_email.value = '';
  get_new_password.value = false;
};

const handleSubmit = (event) => {
  event.preventDefault();  // 阻止表单的默认提交行为
  // 注册逻辑
  if (authStore.isRegisterMode) {
    let request = {
      name: name.value,
      email: email.value,
      password: password.value,
    };
    // console.log(request);
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
          //  alert(`请求错误: ${error.response.data.data()}`);
           alert(error.response.data.msg);
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
  if(authStore.isRegisterMode === false){
    event.preventDefault();  // 阻止表单的默认提交行为
    let request = {
      email: email.value,
      token:authStore.getToken(),
      password: password.value,
    };
    axios.post('http://127.0.0.1:8000/api/login/', request)
      .then(response => {
        if (response.data.code === 0) {
          alert('登录成功');
          // token应该存放在浏览器的cookie中
          Cookies.set('token', response.data.token);
          Cookies.set('user_id', response.data.id);
          Cookies.set('user_name', response.data.name);
          Cookies.set('user_email', response.data.email);
          ClearForm();
          window.location.href = '/';
        } else {
          console.log("出现了一些错误");
        }
      })
    .catch(error => {
      if (error.response) {
        // 请求已发出但服务器响应的状态码不在 2xx 范围内
      alert(error.response.data.msg);
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
        <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">{{ authStore.isRegisterMode ? 'Register for an account' : 'Sign in to your account' }}</h2>
      </div>

      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" action="#" method="POST">

          <div v-if="authStore.isRegisterMode">
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
              <button type="button" @click="get_new_password = true">
                <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">忘记密码?</a>
              </button>
            </div>
            <div class="mt-2">
              <input type="password" name="password" id="password" autocomplete="current-password" required v-model="password" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" placeholder="请输入你的密码"/>
            </div>
          </div>

          <div>
            <button type="submit" @click="handleSubmit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">{{ authStore.isRegisterMode ? '注册' : '登录' }}</button>
          </div>
        </form>

        <p class="mt-10 text-center text-sm/6 text-gray-500">
          {{ authStore.isRegisterMode ? '拥有账号  ' : '没有账号?' }}
        <button @click="toggleMode" class="font-semibold text-indigo-600 hover:text-indigo-500">
          {{ authStore.isRegisterMode ? '登录' : '注册' }}
        </button>
        </p>
      </div>

      <!-- 模态框 -->
    <div v-if="get_new_password" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <h2 class="mb-4">输入原来的名字</h2>
        <input v-model="old_name" type="text" class="w-full py-2 px-4 mb-4 text-gray-700 bg-white border rounded-md dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring" />
        <h2 class="mb-4">输入原来的邮箱</h2>
        <input v-model="old_email" type="text" class="w-full py-2 px-4 mb-4 text-gray-700 bg-white border rounded-md dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring" />
          <div class="flex justify-end">
          <button @click="confirmPassword" class="mr-2 px-4 py-2 text-white bg-blue-500 rounded-md hover:bg-blue-600">确认</button>
          <button @click="closeModal" class="px-4 py-2 text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300">取消</button>
        </div>
      </div>
    </div>
    </div>
  </template>

  <style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  max-width: 90%; /* 最大宽度为90% */
  width: 500px; /* 固定宽度 */
}
  </style>