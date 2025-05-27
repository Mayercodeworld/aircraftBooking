<script setup>
import { ref , onMounted } from 'vue';
import Search from '@/components/Search.vue';
import Cookies from "js-cookie";
import axios from "axios";
import {useAuthStore} from '../stores/user_store.js'
// import sanya from '../assets/photos/首页/三亚.jpg'


const authStore = useAuthStore()
const isLoggedIn = ref(false);
const fly = ref(false)
const destinations = ref([
  { id: 1, name: '三亚', country: '中国', image: '/src/assets/photos/firstpage/sanya.jpg'},
  { id: 2, name: '上海', country: '中国', image: '/src/assets/photos/firstpage/shanghai.jpg'},
  { id: 3, name: '广州', country: '中国', image: '/src/assets/photos/firstpage/guangzhou.jpg'},
  { id: 4, name: '厦门', country: '中国', image: '/src/assets/photos/firstpage/xiamen.jpg' },
  { id: 5, name: '香港', country: '中国', image: '/src/assets/photos/firstpage/hongkong.jpg'},
  { id: 6, name: '杭州', country: '中国', image: '/src/assets/photos/firstpage/hangzhou.png'},
  { id: 7, name: '伦敦', country: '英国', image: '/src/assets/photos/firstpage/london.jpg'},
  { id: 8, name: '纽约', country: '美国', image: '/src/assets/photos/firstpage/newyork.jpg'},
]);

//取票提醒
// 定义一个响应式变量来存储订单数据
const orders = ref([]);
// 定义一个数组来存储即将起飞的航班信息
const upcomingFlights = ref([]);
onMounted(async () => {
  // 切换界面之后，初始显示顶部
  window.scrollTo({
    top: 0,
  });
  isLoggedIn.value = await authStore.CheckLogin();  // 使用 await 获取 CheckLogin 的结果
  if(isLoggedIn.value) {
    get_user_tickets();
  }
});


const get_user_tickets = () => {
  const user_id = Cookies.get('user_id');
  if (user_id) {
    axios.get(`http://127.0.0.1:8000/api/user/${user_id}/tickets/`).then(res => {
      console.log(res.data);
      // 将返回的数据赋值给 orders 变量
      orders.value = res.data;
      console.log("Orders:", orders.value);
      // 获取当前时间
      const now = new Date();
      console.log("Current Time:", now);
      // 清空 upcomingFlights 数组
      upcomingFlights.value = [];

      // 遍历订单列表
      for (let i = 0; i < orders.value.length; i++) {
        if(orders.value[i].status === '已取消') {
          continue;
        }
        const order = orders.value[i];
        const departureTime = new Date(order.flight.departure_time);
        console.log("Flight Departure Time:", departureTime);
        // 计算时间差（毫秒）
        const timeDifference = departureTime - now;
        console.log("Time Difference:", timeDifference);
        // 三小时的毫秒数
        const threeHoursInMilliseconds = 3 * 60 * 60 * 1000;

        // 如果时间差小于三小时,必须大于0
        if (timeDifference >= 0 && timeDifference < threeHoursInMilliseconds) {
          // 将相关信息添加到 upcomingFlights 数组中
          upcomingFlights.value.push({
            name: order.name,
            gender: order.gender,
            flight_no: order.flight.flight_no,
            departure_time: order.flight.departure_time
          });
        }
      }
      // 如果 upcomingFlights 数组不为空，则将 fly 设置为 true
      if (upcomingFlights.value.length > 0) {
        fly.value = true;
        console.log("fly: ", fly.value);
      }

      console.log("Upcoming Flights:", upcomingFlights.value[0]);
    }).catch(error => {
      console.error("There was an error fetching the user tickets!", error);
    });
  }
};
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
    <section
      class="ezy__travel1 light py-20 md:p-[100px]  text-white relative z-11 bg-cover bg-no-repeat bg-center flex justify-center items-end">
      <video autoplay muted playsinline>
          <source src="../assets/videos/video1.mp4" type="video/mp4">
          您的浏览器不支持 video 标签。
      </video>  
      <div class="container mx-auto">
            <div class="grid grid-cols-12 md:mb-50">
                <div class="col-span-12">
                    <div class="grid grid-cols-12 gap-4 relative">
                        <div
                            class="col-span-12 lg:col-span-10 lg:col-start-2 xl:col-span-8 xl:col-start-3 text-center mb-4">
                            <h2 class="font-bold text-[39px] lg:text-[80px] mb-4">云端之梦，一触即达</h2>
                            <div class="grid grid-cols-12">
                                <div class="col-span-12 lg:col-span-10 lg:col-start-2 xl:col-span-8 xl:col-start-3">
                                    <p class="text-[18px] leading-[32px] opacity-70 text-center">
                                        踏遍千山万水，收集世间温柔
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <Search />
          </div>
    </section>
    
    <section
        class="ezy__travel3 light py-14 md:py-24 bg-white dark:bg-[#2E2F41] text-zinc-900 dark:text-white relative overflow-hidden z-1">
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
            <div v-for="(destination, index) in destinations" :key="index" class="box col-span-12 md:col-span-6 lg:col-span-3 px-1" >
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
    <!-- 模态框 -->
    <div v-if="fly" class="modal-overlay fixed inset-0 flex justify-center z-50">
      <div class="modal-content relative w-[500px] h-[250px] bg-white rounded-lg shadow-xl p-6">
        <!-- 关闭按钮 -->
        <button @click="fly = false" class="absolute top-3 right-3 text-gray-400 hover:text-gray-600 focus:outline-none">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
        <!-- 标题 -->
        <h2 class="text-2xl font-bold mb-4 text-gray-800">即将起飞的航班提醒</h2>
        <!-- 内容 -->
        <div v-for="(flight, index) in upcomingFlights" :key="index" class="mb-4">
          <p class="text-lg font-semibold text-gray-700 mb-2">
            <span class="mr-2"><svg class="inline w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"></path></svg></span>
            尊敬的 {{ flight.name }} {{ flight.gender === '男' ? '先生' : '女士' }}，
          </p>
          <p class="text-gray-600 mb-2">
            <span class="mr-2"><svg class="inline w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg></span>
            您的航班 {{ flight.flight_no }} 将在 {{ flight.departure_time.slice(0, 10) }} 出发。
          </p>
          <p class="text-gray-600 mb-2">
            <span class="mr-2"><svg class="inline w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></span>
            请于 {{ flight.departure_time.slice(0, 10) }} 前前往机场取票，如果超时，后果自负。
          </p>
        </div>
        <!-- 关闭按钮 -->
        <button @click="fly = false" class="w-full px-4 py-2 text-center text-white transition-colors duration-200 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-lg hover:from-blue-600 hover:to-indigo-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          关闭
        </button>
      </div>
    </div>
</template>

<style scoped>
.ezy__travel1 {
    height: 100vh;
    background-image: none; /* 移除背景图片 */
    background-size: cover;
    background-position: center;
    position: relative;
}

.ezy__travel1 video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover; /* 使视频覆盖整个容器 */
    z-index: -1; /* 确保视频在内容后面 */
}

/* 确保图片容器具有 overflow: hidden 样式 */
.box {
  /* background-color: #404156; */
  /* overflow: hidden; */
}

/* 使用 object-fit: cover 来控制图片的显示方式 */
.box .relative img {
  /* object-fit: cover; */
  width: 100%;
  height: 440px;
}

/* 模态框样式 */
.modal-overlay {
    position: fixed;
    padding-top: 100px;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    z-index: 1000;
}
</style>
