<!-- src/views/Travel.vue -->
<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const id = parseInt(route.params.id, 10); // 将 id 转换为数字类型

const destination = ref(null);

onMounted(() => {
  // 根据 id 加载数据
  loadDestination(id);
});

const loadDestination = (id) => {
  // 这里可以替换为从 API 获取数据的逻辑
  // 假设我们有一个静态的数据列表
  const destinations = ref([
    { id: 1, name: 'Toledo', country: 'United State', image: 'https://cdn.easyfrontend.com/pictures/search1_1.png', price: 325, description: 'Description of Toledo' },
    { id: 2, name: 'Noonu Atoll', country: 'United State', image: 'https://cdn.easyfrontend.com/pictures/search1_2.png', price: 325, description: 'Description of Noonu Atoll' },
    { id: 3, name: 'Toledo', country: 'United State', image: 'https://cdn.easyfrontend.com/pictures/search1_3.png', price: 325, description: 'Description of Toledo' },
    { id: 4, name: 'Kaafu Atoll', country: 'United State', image: 'https://cdn.easyfrontend.com/pictures/search1_4.png', price: 325, description: 'Description of Kaafu Atoll' },
    { id: 5, name: 'Barcelona', country: 'Spain', image: 'https://cdn.easyfrontend.com/pictures/search1_5.png', price: 325, description: 'Description of Barcelona' },
    { id: 6, name: 'Hiroshima', country: 'Japan', image: 'https://cdn.easyfrontend.com/pictures/search1_6.png', price: 325, description: 'Description of Hiroshima' },
    { id: 7, name: 'Tibidabo', country: 'Barcelona', image: 'https://cdn.easyfrontend.com/pictures/search1_7.png', price: 325, description: 'Description of Tibidabo' },
    { id: 8, name: 'Brussels', country: 'Belgium', image: 'https://cdn.easyfrontend.com/pictures/search1_8.png', price: 325, description: 'Description of Brussels' },
  ]);

  destination.value = destinations.value.find(dest => dest.id === id);
};
</script>

<template>
  <div v-if="destination">
    <h1>{{ destination.name }}</h1>
    <p>{{ destination.country }}</p>
    <p>Price: ${{ destination.price }}</p>
    <p>{{ destination.description }}</p>
  </div>
  <div v-else>
    <p>Destination not found</p>
  </div>
</template>

<style scoped>
/* 添加样式 */
</style>