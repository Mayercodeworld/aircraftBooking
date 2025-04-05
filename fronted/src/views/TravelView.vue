<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import Spark from '@/components/Spark.vue';

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
    { id: 1, place: '三亚', image: [{ src: 'https://pic.52112.com/2020/04/13/JPG-200413_328/gCaPae4zjp_small.jpg', title: 'Image 1' }, { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },{src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3'}, { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },{ src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }] },
    { id: 2, place: '上海', image: [{ src: 'https://b.zol-img.com.cn/sjbizhi/images/11/1080x1920/1592967802496.jpg', title: 'Image 1' }, { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },{src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3'}, { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },{ src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }] },
    { id: 3, place: '广州', image: [{ src: 'https://b.zol-img.com.cn/sjbizhi/images/11/1080x1920/1592967802496.jpg', title: 'Image 1' }, { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },{src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3'}, { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },{ src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }] },
    { id: 4, place: '厦门', image: [{ src: 'https://b.zol-img.com.cn/sjbizhi/images/11/1080x1920/1592967802496.jpg', title: 'Image 1' }, { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },{src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3'}, { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },{ src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }] },
    { id: 5, place: '香港', image: [{ src: 'https://b.zol-img.com.cn/sjbizhi/images/11/1080x1920/1592967802496.jpg', title: 'Image 1' }, { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },{src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3'}, { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },{ src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }] },
    { id: 6, place: '杭州', image: [{ src: 'https://b.zol-img.com.cn/sjbizhi/images/11/1080x1920/1592967802496.jpg', title: 'Image 1' }, { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },{src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3'}, { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },{ src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }] },
    { id: 7, place: '伦敦', image: [{ src: 'https://b.zol-img.com.cn/sjbizhi/images/11/1080x1920/1592967802496.jpg', title: 'Image 1' }, { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },{src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3'}, { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },{ src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }] },
    { id: 8, place: '纽约', image: [{ src: 'https://b.zol-img.com.cn/sjbizhi/images/11/1080x1920/1592967802496.jpg', title: 'Image 1' }, { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },{src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3'}, { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },{ src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }] }
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

// 使用 computed 确保 images 是响应式的
const images = computed(() => images_collections.value || [
  { src: 'https://img1.qunarzz.com/travel/d5/1606/78/f159a24f7a0672f7.jpg?color=#2b79bf', title: 'Image 1' },
  { src: 'https://dimg04.c-ctrip.com/images/100g10000000pf92gD939_R_1600_10000.jpg', title: 'Image 2' },
  { src: 'https://img.keaitupian.cn/uploads/2021/09/15/br4mlga54st.jpg', title: 'Image 3' },
  { src: 'https://dimg04.c-ctrip.com/images/100c0e0000006zxz0B249_R_1600_10000.jpg', title: 'Image 4' },
  { src: 'https://dimg04.c-ctrip.com/images/0100r12000f6tbgy71A1D_C_1600_1200.jpg', title: 'Image 5' }
]);

console.log("id:", id);
console.log("images_collections:", images_collections.value);
console.log("images:", images.value);

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
    <div class="container px-8 md:px-24">
      <div class="grid grid-cols-12">

        <div class="col-span-12">
          <div class="relative mt-12">
            <!-- 显示当前三张图片 -->
            <div class="grid grid-cols-6 gap-x-6">
              <div v-for="(image, index) in currentImages" :key="index" class="col-span-6 md:col-span-3 lg:col-span-2">
                <div class="rounded-lg overflow-hidden">
                  <div class="relative">
                    <img :src="image.src" alt="" class="w-full" />
                    <!-- <div class="absolute bottom-0 flex flex-col justify-center items-center w-full text-white px-12 pb-6 text-center">
                      <h4 class="text-[22px] font-medium">{{ image.title }}</h4>
                      <h5 class="text-[22px] font-medium text-blue-600 my-3">£20</h5>
                      <a href="#" class="bg-transparent hover:bg-blue-600 border border-blue-600 hover:text-white py-2 rounded transition text-blue-600 px-9 mb-3">Add To Cart</a>
                      <p class="text-base opacity-80">PDF Format</p>
                    </div> -->
                  </div>
                </div>
              </div>
            </div>

            <!-- 左右按钮 -->
            <button
              @click="prevImage"
              class="w-12 h-12 text-[22px] bg-blue-600 bg-opacity-70 hover:bg-opacity-100 text-white rounded-full absolute top-2/4 -left-6 -translate-y-1/2 transition"
            >
              <
            </button>
            <button
              @click="nextImage"
              class="w-12 h-12 text-[22px] bg-blue-600 bg-opacity-70 hover:bg-opacity-100 text-white rounded-full absolute top-2/4 -right-6 -translate-y-1/2 transition"
            >
              >
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
  <Spark :place="place"></Spark>
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
</style>
