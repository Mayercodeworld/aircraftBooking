<script setup>
import {useAuthStore} from '../stores/user_store.js'
import {ref, onMounted} from "vue";
import Info from './Info.vue';

const authStore = useAuthStore()

// const token = ref('')
// const userid = ref('')
const isLoggedIn = ref(false);
const info = ref(false);

onMounted(async () => {
  // getCookie();
  isLoggedIn.value = await authStore.CheckLogin();  // 使用 await 获取 CheckLogin 的结果
  // console.log("isLoggedIn: ", isLoggedIn.value);
  // console.log('authStore.CheckLogin() ', isLoggedIn.value);
});

// const getCookie = () => {
//   token.value = authStore.getToken()
//   userid.value = authStore.getUserId()
//   // console.log("token: ",token.value);
//   // console.log("userid: ",userid.value);
// }

// const CookieLogIn = async () => {
//   const isLoggedIn = await authStore.CheckLogin();
//   if (isLoggedIn.value) {
//     // 登录成功，可以在这里更新 UI 或进行其他操作
//   } else {
//     // 登录失败，可以在这里更新 UI 或进行其他操作
//   }
// }

const handle = async () => {
  if (!isLoggedIn.value) {
    window.location.href = '/login';
  } else {
    authStore.clearCookies();
    isLoggedIn.value = false;
    // console.log("已经登录，可以选择退出");
    window.location.href = '/';
  }
};

</script>

<template>
  <header class="header text-gray-600 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor"
             stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
             class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
        </svg>
        <span class="ml-3 text-xl">Tailblocks</span>
      </a>
      <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">

        <router-link to="/" class="mr-5 hover:text-gray-900">首页</router-link>
        <a class="mr-5 hover:text-gray-900">更多</a>
        <a class="mr-5 hover:text-gray-900">其他</a>
        <a class="mr-5 hover:text-gray-900">文档</a>
      </nav>
      <div class="login">
        <button @click="handle"
                class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">
          {{ isLoggedIn ? '退出' : '登录' }}
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
               stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
          </svg>
        </button>

      </div>
      <div class="info" v-if="isLoggedIn">
        <button @click="info = !info"
                class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">
          个人
          <svg t="1741403815208" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4018" width="18" height="20">
            <path d="M586.945923 513.581008c55.067176-27.962865 92.91211-85.125773 92.91211-150.998039 0-93.338828-75.937506-169.276335-169.277358-169.276335s-169.275311 75.937506-169.275311 169.276335c0 65.872267 37.844933 123.034151 92.911086 150.998039-95.652524 32.016181-164.778904 122.45496-164.778904 228.743728 0 11.31572 9.17394 20.491707 20.491707 20.491707s20.491707-9.174963 20.491707-20.491707c0-110.36869 89.791026-200.160739 200.160739-200.160739S710.741413 631.956046 710.741413 742.324736c0 11.31572 9.17394 20.491707 20.491707 20.491707s20.491707-9.174963 20.491707-20.491707C751.723803 636.035968 682.598446 545.598212 586.945923 513.581008zM382.287753 362.582969c0-70.742181 57.552787-128.293945 128.292921-128.293945 70.742181 0 128.293945 57.552787 128.293945 128.293945 0 70.741157-57.552787 128.292921-128.293945 128.292921C439.84054 490.876913 382.287753 433.324126 382.287753 362.582969z" fill="#272636" p-id="4019"></path><path d="M827.871087 196.127889C743.498468 111.757317 631.320573 65.290005 512 65.290005S280.500509 111.756293 196.128913 196.127889C111.756293 280.501532 65.291029 392.678404 65.291029 511.998977s46.465265 231.499491 130.837884 315.872111 196.550515 130.837884 315.871087 130.837884 231.498468-46.465265 315.871087-130.837884S958.708971 631.319549 958.708971 511.998977 912.243707 280.500509 827.871087 196.127889zM512 917.726581c-223.718271 0-405.726581-182.007287-405.726581-405.727605 0-223.718271 182.00831-405.726581 405.726581-405.726581s405.726581 182.007287 405.726581 405.726581C917.726581 735.719294 735.718271 917.726581 512 917.726581z" fill="#272636" p-id="4020">
            </path>
          </svg>
        </button>
      </div>

    </div>
    <Info v-if="info" class="sidebar"/>
  </header>
</template>

<style scoped>
.title-font {
  width: 14%;
}

nav {
  width: 300px;
  height: 36px;
  background-color: #fff;
  box-sizing: border-box;
  border-radius: 16px;
  border-bottom: 1.3px solid #000;
}

nav .mr-5 {
  margin-left: 20px;
}

nav .mr-5:hover {
  font-weight: 900;
}

nav .active {
  background-color: #e5e7eb;
}

.login {
  width: 7%;
}

.info {
  width: 7%;
}

.sidebar {
  position: fixed;
  top: 8vh;
  right: 0;
  height: 92vh;
  box-shadow: -5px 9px 19px 0px rgba(100, 100, 111, 0.2);
  border-radius: 5px;
  opacity: 1;
  transition: opacity 0.5s ease;
}
</style>