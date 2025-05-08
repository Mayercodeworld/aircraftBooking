<script setup>
import { ref, onMounted } from 'vue';
import {useAuthStore} from '../stores/user_store.js'
import axios  from "axios";
import Cookies from 'js-cookie';
const authStore = useAuthStore();

const name = ref('');
const email = ref('');
const password = ref('');
const nameError = ref('');
const emailError = ref('');
const passwordError = ref('');

const old_name = ref('');
const old_email = ref('');
const get_new_password = ref(false);

// onMounted(() => {
// });

function validateName(value) {
    const trimmedValue = value.trim();
    if (!trimmedValue) {
        return '名字不能为空';
    }
    const chineseRegex = /^[\u4e00-\u9fa5 ]+$/;
    const englishRegex = /^[a-zA-Z ]+$/;
    if (!chineseRegex.test(trimmedValue) && !englishRegex.test(trimmedValue)) {
        return '请输入合法的中文或英文名';
    }
    if (trimmedValue.length < 2 || trimmedValue.length > 30) {
        return '名字长度应在2到30个字符之间';
    }
    return '';
}

function validateEmail(value) {
    const trimmedValue = value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!trimmedValue) {
        return '邮箱不能为空';
    }
    if (!emailRegex.test(trimmedValue)) {
        return '请输入合法的邮箱地址';
    }
    return '';
}

function validatePassword(value) {
    const trimmedValue = value.trim();
    if (!trimmedValue) {
        return '密码不能为空';
    }
    if (trimmedValue.length < 8) {
        return '密码至少需要8个字符';
    }

    // 检查是否为常见弱密码
    const weakPasswords = ['123456', '12345678', 'password', 'admin123', 'qwerty'];
    if (weakPasswords.includes(trimmedValue.toLowerCase())) {
        return '密码过于简单';
    }

    const hasUpper = /[A-Z]/.test(trimmedValue);
    const hasLower = /[a-z]/.test(trimmedValue);
    const hasNumber = /\d/.test(trimmedValue);
    const hasSpecial = /[^A-Za-z0-9]/.test(trimmedValue);
    const categories = [hasUpper, hasLower, hasNumber, hasSpecial].filter(Boolean).length;
    if (categories < 3) {
        return '密码需包含至少三种字符类型（大写/小写/数字/特殊字符）';
    }
    return '';
}

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
  // 仅在注册模式下校验所有字段
  if (authStore.isRegisterMode) {
    nameError.value = validateName(name.value);
    emailError.value = validateEmail(email.value);
    passwordError.value = validatePassword(password.value);

    // 如果有任意错误，不提交表单
    if (nameError.value || emailError.value || passwordError.value) {
      alert('请确保所有输入格式正确')
      return;
    }
  }
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
          // 你使用 window.location.href = '/' 进行页面跳转时，浏览器会加载新的页面，这会导致Pinia的状态被重置
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
      <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">{{ authStore.isRegisterMode ? '注册新账户' : '登录你的账户' }}</h2>
    </div>
    
    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <!-- 名字输入框 -->
        <div v-if="authStore.isRegisterMode">
          <label for="name" class="block text-sm font-medium text-gray-900">名字</label>
          <div class="mt-2">
            <input 
              type="text" 
              name="name" 
              id="name" 
              autocomplete="name" 
              required  
              v-model="name"
              @input="nameError = validateName(name)" 
              class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm" 
              placeholder="请输入你的名字"/>
            <span v-if="nameError" class="text-red-500 text-sm">{{ nameError }}</span>
          </div>
        </div>
        <!-- 邮箱输入框 -->
        <div>
          <label for="email" class="block text-sm/6 font-medium text-gray-900">电子邮件</label>
          <div class="mt-2">
            <input 
              type="email" 
              name="email" 
              id="email" 
              autocomplete="email" 
              required 
              v-model="email" 
              @input="emailError = validateEmail(email)"
              class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" 
              placeholder="请输入你的电子邮件"/>
            <span v-if="emailError" class="text-red-500 text-sm">{{ emailError }}</span>
          </div>
        </div>
        <!-- 密码输入框 -->
        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm/6 font-medium text-gray-900" >密码</label>
            <button type="button" @click="get_new_password = true">
              <a href="#" v-if="!authStore.isRegisterMode" class="font-semibold text-indigo-600 hover:text-indigo-500">忘记密码?</a>
            </button>
          </div>
          <div class="mt-2">
            <input 
              type="password" 
              name="password" 
              id="password" 
              autocomplete="current-password" 
              required 
              v-model="password" 
              @input="passwordError = validatePassword(password)"
              class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" 
              placeholder="请输入你的密码"/>
            <span v-if="passwordError && authStore.isRegisterMode" class="text-red-500 text-sm">{{ passwordError }}</span>
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