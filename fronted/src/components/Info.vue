<script setup>
import {ref} from 'vue';
import {useAuthStore} from '../stores/user_store.js';
import Cookies from "js-cookie";
import axios from "axios";
const authStore = useAuthStore();

const userInfo = ref({
  id: authStore.user_id,
  name: authStore.user_name,
  email: authStore.user_email,
  token: authStore.token,
  avatar: Cookies.get("avatar") || "/src/assets/profile_photo/profile1.png", // 默认头像
});

const showAvatarModal = ref(false);
const showSettingModal = ref(false);
const newAvatarUrl = ref('');
const newname = ref('');
const newemail = ref('');
const newpassword = ref('');

const closeAvatarModal = () => {
  showAvatarModal.value = false;
  newAvatarUrl.value = ''; // 清空输入框
};
const closeSettingModal = () => {
  showSettingModal.value = false;
  newname.value = '';
  newemail.value = '';
  newpassword.value = '';
};

const confirmAvatar = () => {
  if (newAvatarUrl.value) {
    Cookies.set('avatar', newAvatarUrl.value);
    userInfo.value.avatar = newAvatarUrl.value;
  }
  //点击确认时，如果输入框有内容，则更新头像URL，否则恢复默认头像
  else {
    userInfo.value.avatar = "/src/assets/profile_photo/profile1.png";
    Cookies.set('avatar', "");
  }
  closeAvatarModal();
};
const confirmSetting = () => {
  if (newname.value || newemail.value || newpassword.value) {
    const updatedData = {
      id: userInfo.value.id,
      name: newname.value || userInfo.value.name,
      email: newemail.value || userInfo.value.email,
      password: newpassword.value || userInfo.value.token
    };

    axios.post('http://127.0.0.1:8000/api/user/update/', updatedData)
      .then(response => {
        console.log('User information updated successfully:', response.data);
        // 更新 userInfo
        if (newname.value) {
          userInfo.value.name = newname.value;
          Cookies.set('user_name', newname.value);
        }
        if (newemail.value) {
          userInfo.value.email = newemail.value;
          Cookies.set('user_email', newemail.value);
        }
        if(newpassword.value) {
          Cookies.set('token', response.data.token);
          console.log('token updated successfully');
        }
        closeSettingModal();
      })
      .catch(error => {
        alert(error.response.data.msg);
      });
  } else {
    closeSettingModal();
  }
};
</script>

<template>
  <aside class="flex flex-col w-64 h-screen px-4 py-8 overflow-y-auto bg-gray-100  border-r rtl:border-r-0 rtl:border-l">

    <div  class="flex items-center px-4 -mx-2">
      <button @click="showAvatarModal = true" style="cursor: pointer;">
        <img class="object-cover mx-2 rounded-full h-15 w-15" :src="userInfo.avatar" alt="avatar" />
      </button>
      <span class="mx-2 font-medium text-black dark:text-gray-200">{{ userInfo.name }}</span>
    </div>

    <div class="flex flex-col justify-between flex-1 mt-6">
      <nav>
        <div class="flex items-center px-4 py-2 mt-5 text-black transition-colors duration-300 transform rounded-md hover:bg-white">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M19 11H5M19 11C20.1046 11 21 11.8954 21 13V19C21 20.1046 20.1046 21 19 21H5C3.89543 21 3 20.1046 3 19V13C3 11.8954 3.89543 11 5 11M19 11V9C19 7.89543 18.1046 7 17 7M5 11V9C5 7.89543 5.89543 7 7 7M7 7V5C7 3.89543 7.89543 3 9 3H15C16.1046 3 17 3.89543 17 5V7M7 7H17"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          <span class="mx-4 font-medium">id: {{ userInfo.id }}</span>
        </div>

        <div class="flex items-center px-4 py-2 mt-5 text-black transition-colors duration-300 transform rounded-md hover:bg-white" href="#">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 7C16 9.20914 14.2091 11 12 11C9.79086 11 8 9.20914 8 7C8 4.79086 9.79086 3 12 3C14.2091 3 16 4.79086 16 7Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M12 14C8.13401 14 5 17.134 5 21H19C19 17.134 15.866 14 12 14Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          <span class="mx-4 font-medium">{{ userInfo.email }}</span>
        </div>

        <router-link to="/mystickets" class="flex items-center px-4 py-2 mt-5 text-black transition-colors duration-300 transform rounded-md hover:bg-white" href="#">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 5V7M15 11V13M15 17V19M5 5C3.89543 5 3 5.89543 3 7V10C4.10457 10 5 10.8954 5 12C5 13.1046 4.10457 14 3 14V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V14C19.8954 14 19 13.1046 19 12C19 10.8954 19.8954 10 21 10V7C21 5.89543 20.1046 5 19 5H5Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          <span class="mx-4 font-medium">我的出行</span>
        </router-link>

        <a @click="showSettingModal = true" class="flex items-center px-4 py-2 mt-5 text-black transition-colors duration-300 transform rounded-md hover:bg-white" href="#">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.3246 4.31731C10.751 2.5609 13.249 2.5609 13.6754 4.31731C13.9508 5.45193 15.2507 5.99038 16.2478 5.38285C17.7913 4.44239 19.5576 6.2087 18.6172 7.75218C18.0096 8.74925 18.5481 10.0492 19.6827 10.3246C21.4391 10.751 21.4391 13.249 19.6827 13.6754C18.5481 13.9508 18.0096 15.2507 18.6172 16.2478C19.5576 17.7913 17.7913 19.5576 16.2478 18.6172C15.2507 18.0096 13.9508 18.5481 13.6754 19.6827C13.249 21.4391 10.751 21.4391 10.3246 19.6827C10.0492 18.5481 8.74926 18.0096 7.75219 18.6172C6.2087 19.5576 4.44239 17.7913 5.38285 16.2478C5.99038 15.2507 5.45193 13.9508 4.31731 13.6754C2.5609 13.249 2.5609 10.751 4.31731 10.3246C5.45193 10.0492 5.99037 8.74926 5.38285 7.75218C4.44239 6.2087 6.2087 4.44239 7.75219 5.38285C8.74926 5.99037 10.0492 5.45193 10.3246 4.31731Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M15 12C15 13.6569 13.6569 15 12 15C10.3431 15 9 13.6569 9 12C9 10.3431 10.3431 9 12 9C13.6569 9 15 10.3431 15 12Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          <span class="mx-4 font-medium">设置</span>
        </a>

        <hr class="my-6 border-gray-200 dark:border-gray-600" />
      </nav>
    </div>

    <!-- 模态框 -->
    <div v-if="showAvatarModal" class="modal-overlay" @click="closeAvatarModal">
      <div class="modal-content" @click.stop>
        <h2 class="mb-4">更换头像</h2>
        <input v-model="newAvatarUrl" type="text" class="w-full py-2 px-4 mb-4 text-gray-700 bg-white border rounded-md dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring" placeholder="输入图片地址" />
        <div class="flex justify-end">
          <button @click="confirmAvatar" class="mr-2 px-4 py-2 text-white bg-blue-500 rounded-md hover:bg-blue-600">确认</button>
          <button @click="closeAvatarModal" class="px-4 py-2 text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300">取消</button>
        </div>
      </div>
    </div>

    <!-- 模态框 -->
    <div v-if="showSettingModal" class="modal-overlay" @click="closeSettingModal">
      <div class="modal-content" @click.stop>
        <h2 class="mb-4">更换名字</h2>
        <input v-model="newname" type="text" class="w-full py-2 px-4 mb-4 text-gray-700 bg-white border rounded-md dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring" :placeholder="userInfo.name" />
        <h2 class="mb-4">更换邮箱</h2>
        <input v-model="newemail" type="text" class="w-full py-2 px-4 mb-4 text-gray-700 bg-white border rounded-md dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring" :placeholder="userInfo.email" />
        <h2 class="mb-4">更换密码</h2>
        <input v-model="newpassword" type="password" class="w-full py-2 px-4 mb-4 text-gray-700 bg-white border rounded-md dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring" placeholder="******" />
        <div class="flex justify-end">
          <button @click="confirmSetting" class="mr-2 px-4 py-2 text-white bg-blue-500 rounded-md hover:bg-blue-600">确认</button>
          <button @click="closeSettingModal" class="px-4 py-2 text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300">取消</button>
        </div>
      </div>
    </div>
  </aside>
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