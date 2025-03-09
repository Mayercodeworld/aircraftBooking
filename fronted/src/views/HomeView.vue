<script setup>
import { ref } from 'vue';
import Search from '@/components/Search.vue';
const destinations = ref([
  { id: 1, name: 'Toledo', country: 'United State', image: 'https://cdn.easyfrontend.com/pictures/search1_1.png', price: 325 },
  { id: 2, name: 'Noonu Atoll', country: 'United State', image: 'https://cdn.easyfrontend.com/pictures/search1_2.png', price: 325 },
  { id: 3, name: 'Toledo', country: 'United State', image: 'https://cdn.easyfrontend.com/pictures/search1_3.png', price: 325 },
  { id: 4, name: 'Kaafu Atoll', country: 'United State', image: 'https://cdn.easyfrontend.com/pictures/search1_4.png', price: 325 },
  { id: 5, name: 'Barcelona', country: 'Spain', image: 'https://cdn.easyfrontend.com/pictures/search1_5.png', price: 325 },
  { id: 6, name: 'Hiroshima', country: 'Japan', image: 'https://cdn.easyfrontend.com/pictures/search1_6.png', price: 325 },
  { id: 7, name: 'Tibidabo', country: 'Barcelona', image: 'https://cdn.easyfrontend.com/pictures/search1_7.png', price: 325 },
  { id: 8, name: 'Brussels', country: 'Belgium', image: 'https://cdn.easyfrontend.com/pictures/search1_8.png', price: 325 },
]);
</script>

<template>
    <Search />
    <section
        class="ezy__travel3 light py-14 md:py-24 bg-white dark:bg-[#2E2F41] text-zinc-900 dark:text-white relative overflow-hidden z-10">
        <div class="container px-4 mx-auto">
            <div class="grid grid-cols-12 justify-center mb-4 md:mb-5">
                <div class="col-span-12 lg:col-span-6 lg:col-start-4 text-center">
                    <h2 class="font-bold leading-none text-3xl md:text-[55px] mb-4">Popular Destination</h2>
                    <div class="grid grid-cols-12">
                        <div class="col-span-10 col-start-2">
                            <p class="text-[17px] leading-[30px] opacity-60 mb-0">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla posuere ipsum molestie
                                sem
                                volutpat, non
                                imperdiet leo porttitor. Nullam tortor nibh, dictum vitae porttitor eu, pharetra nec
                                tellus.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
          <div class="grid grid-cols-12 gap-4">
            <!-- item -->
            <div class="col-span-12 md:col-span-6 lg:col-span-3 px-1" v-for="(destination, index) in destinations" :key="index">
              <router-link :to="{ name: 'Travel', params: { id: destination.id } }">
                <div class="dark:bg-[#404156] shadow-lg border-none rounded-none mt-4">
                  <div class="relative">
                    <img :src="destination.image" alt="" class="w-full h-auto" />
                    <div class="absolute top-4 right-4 bg-[#414257] text-white px-3 py-2">
                      <h6 class="mb-0 font-normal">From ${{ destination.price }}</h6>
                    </div>
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



</style>