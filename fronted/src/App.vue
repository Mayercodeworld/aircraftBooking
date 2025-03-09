<script setup>
import {  RouterView, useRouter } from 'vue-router'
import { ref, onMounted, onUnmounted } from 'vue';
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';

var show = ref(true);
const router = useRouter();

// 检测路由进入login时，置show为false
router.beforeEach((to, from, next) => {
  if (to.path === '/login') {
    show.value = false;
  } else {
    show.value = true;
  }
  next();
});
</script>

<template>
  <Header v-if="show"  />
  <RouterView />
  <Footer v-if="show" />
</template>

<style scoped>
header {
  position: fixed;
  height: 8vh;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.4);
  z-index: 100;
}
</style>