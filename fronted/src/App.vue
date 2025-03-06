<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref, onMounted, onUnmounted } from 'vue';
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';



var show = ref(true);
const headerTop = ref('-98px');
const router = useRouter();

router.beforeEach((to, from, next) => {
  if (to.path === '/login') {
    show.value = false;
  } else {
    show.value = true;
  }
  next();
});


const handleScroll = () => {
  const scrollThreshold = 100;
  headerTop.value = window.scrollY > scrollThreshold ? '0px' : '-98px';
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<template>
  <Header v-if="show" :style="{ top: headerTop }" />
  <!-- <SideBar /> -->
  <RouterView />
  <Footer v-if="show" />
</template>

<style scoped>
header {
  position: fixed;
  height: 8vh;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.7);
  transition: all 0.3s ease-in-out; /* 添加过渡效果 */
  z-index: 100;
}
</style>
