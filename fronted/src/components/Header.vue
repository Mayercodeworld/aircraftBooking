<script setup>

</script>

<template>
  <header class="text-gray-600 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
        </svg>
        <span class="ml-3 text-xl">Tailblocks</span>
      </a>
      <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
        <a class="mr-5 hover:text-gray-900">首页</a>
        <a class="mr-5 hover:text-gray-900">更多</a>
        <a class="mr-5 hover:text-gray-900">其他</a>
        <a class="mr-5 hover:text-gray-900">文档</a>
      </nav>
      <div class="login">
        <router-link to="/login" class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">登录
        <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
          <path d="M5 12h14M12 5l7 7-7 7"></path>
        </svg>
        </router-link>
      </div>
      
    </div>
  </header>
</template>

<style scoped>
.title-font {
  width: 10%;
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
  width: 10%;
}

</style>