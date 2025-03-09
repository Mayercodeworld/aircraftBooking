<script setup>
import { ref } from 'vue';
import Search from '@/components/Search.vue';

const destinations = ref([
  { id: 1, name: '三亚', country: '中国', image: 'https://dimg04.c-ctrip.com/images/100t0u000000j7i4o06A5_R_10000_1200.jpg' },
  { id: 2, name: '上海', country: '中国', image: 'https://cdn.pixabay.com/photo/2015/04/20/10/20/shanghai-730892_1280.jpg'},
  { id: 3, name: '广州', country: '中国', image: 'https://cdn.easyfrontend.com/pictures/search1_3.png'},
  { id: 4, name: '厦门', country: '中国', image: 'https://cdn.easyfrontend.com/pictures/search1_4.png' },
  { id: 5, name: '香港', country: '中国', image: 'https://cdn.easyfrontend.com/pictures/search1_5.png'},
  { id: 6, name: '杭州', country: '中国', image: 'https://cdn.easyfrontend.com/pictures/search1_6.png'},
  { id: 7, name: '伦敦', country: '英国', image: 'https://cdn.easyfrontend.com/pictures/search1_7.png'},
  { id: 8, name: '华盛顿', country: '美国', image: 'https://cdn.easyfrontend.com/pictures/search1_8.png'},
]);
</script>

<template>
    <Search />
    <section
        class="ezy__travel3 light py-14 md:py-24 bg-white dark:bg-[#2E2F41] text-zinc-900 dark:text-white relative overflow-hidden z-10">
        <div class="container px-4 mx-auto">
            <div class="grid grid-cols-12 justify-center mb-4 md:mb-5">
                <div class="col-span-12 lg:col-span-6 lg:col-start-4 text-center">
                    <h2 class="font-bold leading-none text-3xl md:text-[55px] mb-4">翱翔云端，梦启航程</h2>
                    <div class="grid grid-cols-12">
                        <div class="col-span-10 col-start-2">
                            <p class="text-[17px] leading-[30px] opacity-60 mb-0">
                              行走于世界的画卷，让心灵去远行。每一次旅行，都是与美好不期而遇的约定。探索未知，拥抱多样，让生活因旅程而精彩。
                              出发吧，让世界成为你的舞台，旅行，让生活绽放无限可能！
                            </p>
                        </div>
                    </div>
                </div>
            </div>
          <div class="grid grid-cols-12 gap-4">
            <!-- item -->
            <div class="box col-span-12 md:col-span-6 lg:col-span-3 px-1" v-for="(destination, index) in destinations" :key="index">
              <router-link :to="{ name: 'Travel', params: { id: destination.id } }">
                <div class="dark:bg-[#404156] shadow-lg border-none rounded-none mt-4">
                  <div class="relative">
                    <img :src="destination.image" alt="" class="w-full h-auto" />
                  </div>
                  <div class="p-4">
                    <h5 class="font-medium text-[20px] mb-1">{{ destination.name }}</h5>
                    <p class="text-[14px] opacity-50 mb-0">{{ destination.country }}</p>
                  </div>
                </div>
              </router-link>
            </div>
          </div>
        </div>
    </section>
</template>

<style scoped>
/* 确保图片容器具有 overflow: hidden 样式 */
.box {
  /* background-color: #404156; */
  overflow: hidden;
}

/* 使用 object-fit: cover 来控制图片的显示方式 */
.box .relative img {
  /* object-fit: cover; */
  width: 100%;
  height: 460px;
}


</style>