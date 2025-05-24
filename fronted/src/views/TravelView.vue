<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';

import Spark from '@/components/Spark.vue';
import MapContainer from '@/components/MapContainer.vue';

const route = useRoute();
const id = parseInt(route.params.id, 10); // 将 id 转换为数字类型， 10代表十进制

const images_collections = ref(null);
const place=ref(null);
onMounted(() => {
  // 根据 id 加载数据
  loadDestination(id);
});

const loadDestination = (id) => {
  const staticData = [
    { id: 1, place: '三亚', image: [{ src: '/src/assets/photos/detail/sanya/1.jpg', title: '椰梦长廊' }, { src: '/src/assets/photos/detail/sanya/2.jpg', title: '鹿回头' }, { src: '/src/assets/photos/detail/sanya/3.jpg', title: '亚龙湾' }, { src: '/src/assets/photos/detail/sanya/4.jpg', title: '天涯海角' }, { src: '/src/assets/photos/detail/sanya/5.jpg', title: '鹿回头' }, { src: '/src/assets/photos/detail/sanya/6.png', title: '南海观音' }] },
    { id: 2, place: '上海', image: [{ src: '/src/assets/photos/detail/shanghai/1.jpg', title: '陆家嘴' }, { src: '/src/assets/photos/detail/shanghai/2.jpg', title: '东方明珠塔' }, { src: '/src/assets/photos/detail/shanghai/3.jpg', title: '上海夜景' }, { src: '/src/assets/photos/detail/shanghai/4.jpg', title: '夜晚立交桥' }, { src: '/src/assets/photos/detail/shanghai/5.jpg', title: '金融中心' }, { src: '/src/assets/photos/detail/shanghai/6.jpg', title: '上海魔都' }]},
    { id: 3, place: '广州', image: [{ src: '/src/assets/photos/detail/guangzhou/1.jpg', title: '珠江新城' }, { src: '/src/assets/photos/detail/guangzhou/2.jpg', title: '广州夜景' }, { src: '/src/assets/photos/detail/guangzhou/3.jpg', title: '小蛮腰' }, { src: '/src/assets/photos/detail/guangzhou/4.jpg', title: '金融中心' }, { src: '/src/assets/photos/detail/guangzhou/5.jpg', title: '广州' }, { src: '/src/assets/photos/detail/guangzhou/6.jpg', title: '广州恩宁路' }]},
    { id: 4, place: '厦门', image: [{ src: '/src/assets/photos/detail/xiamen/1.jpg', title: '厦门八市小吃街' }, { src: '/src/assets/photos/detail/xiamen/2.jpg', title: '厦门月光环' }, { src: '/src/assets/photos/detail/xiamen/3.jpg', title: '厦门世茂双子塔' }, { src: '/src/assets/photos/detail/xiamen/4.jpg', title: '厦门中山路步行街' }, { src: '/src/assets/photos/detail/xiamen/5.jpg', title: '清水宫' }, { src: '/src/assets/photos/detail/xiamen/6.jpg', title: '鼓浪屿' }]},
    { id: 5, place: '香港', image: [{ src: '/src/assets/photos/detail/hongkong/1.jpg', title: '维多利亚港' }, { src: '/src/assets/photos/detail/hongkong/2.jpg', title: '维多利亚港' }, { src: '/src/assets/photos/detail/hongkong/3.jpg', title: '叮叮车' }, { src: '/src/assets/photos/detail/hongkong/4.jpg', title: '弥敦道' }, { src: '/src/assets/photos/detail/hongkong/5.jpg', title: '金紫荆广场' }, { src: '/src/assets/photos/detail/hongkong/6.jpg', title: '香港烟火气' }]},
    { id: 6, place: '杭州', image: [{ src: '/src/assets/photos/detail/hangzhou/1.jpg', title: '杭州奥体中心' }, { src: '/src/assets/photos/detail/hangzhou/2.jpg', title: '双子塔' }, { src: '/src/assets/photos/detail/hangzhou/3.jpg', title: '三潭印月' }, { src: '/src/assets/photos/detail/hangzhou/4.jpg', title:'雷峰塔' }, { src: '/src/assets/photos/detail/hangzhou/5.jpg', title: '杭州法喜寺' }, { src: '/src/assets/photos/detail/hangzhou/6.jpg', title: '西湖' }]},
    { id: 7, place: '伦敦', image: [{ src: '/src/assets/photos/detail/london/1.jpg', title: '碎片大厦' }, { src: '/src/assets/photos/detail/london/2.jpg', title: '伦敦公共交通' }, { src: '/src/assets/photos/detail/london/3.jpg', title: '伊丽莎白塔' }, { src: '/src/assets/photos/detail/london/4.jpg', title: '特拉法加广场' }, { src: '/src/assets/photos/detail/london/5.jpg', title: '泰晤士河畔' }, { src: '/src/assets/photos/detail/london/6.jpg', title: '伦敦塔桥' }, { src: '/src/assets/photos/detail/london/7.jpg', title: '伦敦街道' }, { src: '/src/assets/photos/detail/london/8.jpg', title: '摄政街' }]},
    { id: 8, place: '纽约', image: [{ src: '/src/assets/photos/detail/newyork/1.jpg', title: '帝国大厦' }, { src: '/src/assets/photos/detail/newyork/2.jpg', title: '天际线' }, { src: '/src/assets/photos/detail/newyork/3.jpg', title:'自由塔' }, { src: '/src/assets/photos/detail/newyork/4.jpg', title: '帝国大厦' }, { src: '/src/assets/photos/detail/newyork/5.jpg', title: '曼哈顿市中心' }, { src: '/src/assets/photos/detail/newyork/6.jpg', title: '自由女神像'}]},
  ];

  const destination = staticData.find(dest => dest.id === id);
  if (destination) {
    images_collections.value = destination.image;
    place.value = destination.place;
  } else {
    console.warn('Destination not found for id:', id);
    images_collections.value = [];
    place.value = '';
  }
};

const currentIndex = ref(0); // 当前显示的第一张图片的索引

// 使用 computed 确保 images 是响应式的，默认图片的加载
const images = computed(() => images_collections.value || [
  { src: '/src', title: 'Image 1' },
  { src: '', title: 'Image 2' },
  { src: '', title: 'Image 3' },
]);

// 计算当前显示的三个图片
const currentImages = computed(() => {
  return [
    images.value[(currentIndex.value + 0) % images.value.length],
    images.value[(currentIndex.value + 1) % images.value.length],
    images.value[(currentIndex.value + 2) % images.value.length]
  ];
});

// 切换到上一张图片
const prevImage = () => {
  currentIndex.value = (currentIndex.value - 1 + images.value.length) % images.value.length;
};

// 切换到下一张图片
const nextImage = () => {
  currentIndex.value = (currentIndex.value + 1) % images.value.length;
};
</script>

<template>
  <section class="ezy__blog11 max-h-[500px] relative light py-14 md:py-24 text-stone-800 bg-white dark:bg-[#0b1727] dark:text-white overflow-hidden">
    <div class="absolute top-0 z-0 h-screen w-screen bg-white bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.3),rgba(255,255,255,0))]"></div>
    <div class="container px-8 md:px-24 m-auto">
      <div class="grid grid-cols-12">

        <div class="col-span-12">
          <div class="relative mt-12">
            <!-- 显示当前三张图片 -->
            <div class="grid grid-cols-6 gap-x-6">
              <div v-for="(image, index) in currentImages" :key="index" class="col-span-6 md:col-span-3 lg:col-span-2">
                <div class="rounded-lg overflow-hidden">
                  <div class="relative">
                    <img :src="image.src" alt="" class="w-full" />
                    <div class="absolute bottom-0 flex flex-col justify-center items-center w-full text-white px-12 pb-6 text-center">
                      <h4 class="text-[22px] font-medium">{{ image.title }}</h4>
                      <!-- <h5 class="text-[22px] font-medium text-blue-600 my-3">£20</h5> -->
                      <!-- <a href="#" class="bg-transparent hover:bg-blue-600 border border-blue-600 hover:text-white py-2 rounded transition text-blue-600 px-9 mb-3">Add To Cart</a> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 左右按钮 -->
            <button
              @click="prevImage"
              class="w-12 h-12 text-[22px] bg-blue-600 bg-opacity-70 hover:bg-opacity-100 text-white rounded-full absolute top-2/4 -left-6 -translate-y-1/2 transition">
              <
            </button>
            <button
              @click="nextImage"
              class="w-12 h-12 text-[22px] bg-blue-600 bg-opacity-70 hover:bg-opacity-100 text-white rounded-full absolute top-2/4 -right-6 -translate-y-1/2 transition">
              >
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
  <div class="more">
    <Spark :place="place"></Spark>
    <MapContainer :place="place"></MapContainer>
  </div>

</template>

<style scoped>
.grid-cols-6 {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1rem;
}

.col-span-6 {
  grid-column: span 6;
}

.md\:col-span-3 {
  @media (min-width: 768px) {
    grid-column: span 3;
  }
}

.lg\:col-span-2 {
  @media (min-width: 1024px) {
    grid-column: span 2;
  }
}

.transition-transform {
  transition: transform 0.3s ease-in-out;
}

.transform {
  transform: translateX(0);
}

.-translate-x-full {
  transform: translateX(-100%);
}

.translate-x-full {
  transform: translateX(100%);
}

.more {
  display: flex;
  margin: 0 auto;
  width: 85%;
  align-items: center;
  justify-content: space-between;
}
</style>
