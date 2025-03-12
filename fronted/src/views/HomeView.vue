<script setup>
import { ref , onMounted } from 'vue';
import Search from '@/components/Search.vue';
// import {useAuthStore} from '../stores/user_store.js'
// const authStore = useAuthStore()
// const isLoggedIn = ref(false);
const destinations = ref([
  { id: 1, name: '三亚', country: '中国', image: 'https://dimg04.c-ctrip.com/images/100t0u000000j7i4o06A5_R_10000_1200.jpg'},
  { id: 2, name: '上海', country: '中国', image: 'https://cdn.pixabay.com/photo/2015/04/20/10/20/shanghai-730892_1280.jpg'},
  { id: 3, name: '广州', country: '中国', image: 'https://cdn.pixabay.com/photo/2017/06/30/08/49/city-2457602_1280.jpg'},
  { id: 4, name: '厦门', country: '中国', image: 'https://youimg1.c-ctrip.com/target/010251200087d87rsC522_D_1600_10000.jpg?proc=autoorient' },
  { id: 5, name: '香港', country: '中国', image: 'https://cdn.pixabay.com/photo/2018/09/30/13/18/hong-kong-3713491_1280.jpg'},
  { id: 6, name: '杭州', country: '中国', image: 'https://img.shetu66.com/2023/07/18/1689647215360950.png?x-oss-process=image/resize,h_800/watermark,image_d2F0ZXJtYXJrL2JhY2tncm91cDAxLnBuZw==,g_se,x_0,y_10/watermark,text_6K6-5Zu-572RIOe8luWPtzo1Njg3NDQzMzExNTQ5NTMxMzE=,type_ZmFuZ3poZW5naGVpdGk,color_FFFFFF,size_12,g_se,x_15,y_16'},
  { id: 7, name: '伦敦', country: '英国', image: 'https://cdn.pixabay.com/photo/2016/11/15/08/20/big-ben-1825569_1280.jpg'},
  { id: 8, name: '纽约', country: '美国', image: 'https://cdn.easyfrontend.com/pictures/search1_8.png'},
]);

// onMounted(async () => {
//   isLoggedIn.value = await authStore.CheckLogin();  // 使用 await 获取 CheckLogin 的结果
//   if(isLoggedIn.value)
//   {
//     // 发送axios请求，给orders.views.py,这个里面response获取到，response应该是一个列表，因为不知道有多少个飞机即将起飞。
//     // for循环遍历
//     // 尊敬的{name}{女生/先生}，您的{ flight no }航班，将在{arrival time}出发，请于{arrival time}前往机场取票，如果超时，后果自负。
//   }
//
// });

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