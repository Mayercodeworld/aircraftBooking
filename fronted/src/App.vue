<script setup>
import {  RouterView, useRouter } from 'vue-router'
import { ref, onMounted, onUnmounted } from 'vue';
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';

var show = ref(true);
const scrolled = ref(false);
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

const handleScroll = () => {
  scrolled.value = window.scrollY > 90;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<template>
  <Header v-if="show" :class="{ 'header-scrolled': scrolled }"/>
  <RouterView />
  <Footer v-if="show" />
</template>

<style scoped>
header {
  position: fixed;
  height: 8vh;
  width: 100%;
  background-color: rgba(255, 255, 255, 0);
  transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  z-index: 100;
}

header.header-scrolled {
  background-color: rgba(255, 255, 255, 0.9);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>