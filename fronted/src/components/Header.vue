<script setup>
import {useAuthStore} from '../stores/user_store.js'
import {ref, onMounted, watch} from "vue";
import { useRouter } from 'vue-router';
import Info from './Info.vue';

const authStore = useAuthStore()
const router = useRouter();
// const token = ref('')
// const userid = ref('')
const isLoggedIn = ref(false);
const info = ref(false);
const currentpage = ref('首页')

onMounted(async () => {
  // getCookie();
  isLoggedIn.value = await authStore.CheckLogin();  // 使用 await 获取 CheckLogin 的结果
  // console.log("isLoggedIn: ", isLoggedIn.value);
  // console.log('authStore.CheckLogin() ', isLoggedIn.value);
});

watch(() => {
  if(router.currentRoute.value.path != '/' && router.currentRoute.value.path != '/about') {
    currentpage.value = '';
  }
})

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
  <header class="header body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor"
             stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
             class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
        </svg>
        <span class="ml-3 text-xl">Tailblocks</span>
      </a>
      <nav class="md:ml-auto md:mr-auto rounded-2xl border box-border bg-white h-9 leading-9 min-w-1/10 flex text-center">
        <div @click="currentpage = '首页'" class="min-w-1/2 rounded-2xl hover:bg-indigo-400 hover:text-white h-full" 
        :class="{ 'bg-indigo-500 text-white': currentpage === '首页'}">
          <router-link to="/" class="block w-full">
            首页
          </router-link>
        </div>
        <div @click="currentpage = '关于'" class="min-w-1/2 rounded-2xl hover:bg-indigo-400 hover:text-white h-full" 
        :class="{ 'bg-indigo-500 text-white': currentpage === '关于'}">
          <router-link to="/about" class="block w-full">
            关于
          </router-link>
        </div>
      </nav>
      <div class="login-info">
        <div class="login">
          <button @click="handle"
                  class="inline-flex items-center border-0 py-1 px-3 font-[800] focus:outline-none hover:outline-2 rounded  mt-4 md:mt-0">
            {{ isLoggedIn ? '退出' : '登录' }}
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
              <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
          </button>

        </div>
        <div class="info" v-if="isLoggedIn">
          <button @click="info = !info"
                  class="inline-flex items-center border-0 py-1 px-3 font-[800] hover:outline-2 rounded text-base mt-4 md:mt-0">
            个人
            <svg t="1741869836038" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3514" width="20" height="20">
              <path d="M642.8 531.8c64.3-42.6 106.9-115.4 106.9-198.1C749.7 202.6 643.1 96 512 96S274.3 202.6 274.3 333.7c0 82.7 42.6 155.6 106.9 198.1C215.8 582.9 96 727.7 96 898.3c0 16.4 13.3 29.7 29.7 29.7s29.7-13.3 29.7-29.7c0-180.2 159.9-326.9 356.6-326.9 196.6 0 356.6 146.6 356.6 326.9 0 16.4 13.3 29.7 29.7 29.7s29.7-13.3 29.7-29.7c0-170.6-119.8-315.4-285.2-366.5zM333.7 333.7c0-98.3 80-178.3 178.3-178.3s178.3 80 178.3 178.3S610.3 512 512 512s-178.3-80-178.3-178.3z" fill="#47444F" p-id="3515">
             </path>
            </svg>
          </button>
        </div>
      </div>
      

    </div>
    <transition name="slide-fade">
      <Info v-if="info" class="sidebar"/>
    </transition>
    
  </header>
</template>

<style scoped>
.title-font {
  width: 14%;
}

nav .mr-5:hover {
  font-weight: 900;
}

.login-info{
  display: flex;
  width: 14%;
}

.login-info .login {
  margin-right: 30px;
}
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.4s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
}

.sidebar {
  position: fixed;
  top: 7vh;
  right: 0;
  height: 92vh;
  box-shadow: -5px 9px 19px 0px rgba(100, 100, 111, 0.2);
  border-radius: 5px;
  transition: opacity 0.5s ease;
}
</style>