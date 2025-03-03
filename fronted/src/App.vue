<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref, watch } from 'vue';
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';

var show = ref(true);

const router = useRouter();

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
  <Header v-if="show" />
  <!-- <SideBar /> -->
  <RouterView />
  <Footer v-if="show" />
</template>

<style scoped>

</style>