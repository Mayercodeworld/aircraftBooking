<script setup>
import { ref } from 'vue';
import { formData } from '@/stores/formdata';
import { useRouter } from 'vue-router';
const router = useRouter(); 
const showModal = ref(false); 

const searchFlights = () => {
    if (!formData.from || !formData.to) {
        showModal.value = true; 
        document.body.style.overflow = 'hidden';
        return;
    }
    
    router.push('/tickets');
    showModal.value = false; 
    document.body.style.overflow = 'auto';
};

const closeModal = () => {
    showModal.value = false;
    document.body.style.overflow = 'auto'; 
};
</script>

<template>
    <section
        class="ezy__travel1 light py-20 md:p-[100px] bg-[#0b1727] text-white relative z-1 bg-cover bg-no-repeat bg-center flex justify-center items-end overflow-hidden">
        <div class="container px-4 mx-auto">
            <div class="grid grid-cols-12">
                <div class="col-span-12">
                    <div class="grid grid-cols-12 gap-4 relative">
                        <div
                            class="col-span-12 lg:col-span-10 lg:col-start-2 xl:col-span-8 xl:col-start-3 text-center mb-4">
                            <h2 class="font-bold text-[39px] lg:text-[80px] mb-4">Your Journey Begins</h2>
                            <div class="grid grid-cols-12">
                                <div class="col-span-12 lg:col-span-10 lg:col-start-2 xl:col-span-8 xl:col-start-3">
                                    <p class="text-[18px] leading-[32px] opacity-70 text-center">
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
                                        posuere ipsum molestie sem
                                        volutpat, non imperdiet leo porttitor. Nullam tortor nibh, dictum
                                        vitae porttitor eu,
                                        pharetra nec tellus.
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div
                            class="absolute -bottom-[65px] lg:bottom-0 lg:top-1/2 left-1/2 lg:left-0 lg:right-0 transform -translate-x-1/2 lg:translate-x-0 lg:-translate-y-1/2 flex justify-between opacity-60">
                            <button
                                class="h-[60px] w-[60px] rounded-full border border-white hover:border-blue-500 text-white hover:text-blue-500 transition ease-in-out duration-500 flex justify-center items-center cursor-pointer mr-4 lg:mr-0">
                                <span class="text-xl"><</span>
                            </button>
                            <button
                                class="h-[60px] w-[60px] rounded-full border border-white hover:border-blue-500 text-white hover:text-blue-500 transition ease-in-out duration-500 flex justify-center items-center cursor-pointer">
                                <span class="text-xl">></span>
                            </button>
                        </div>
                    </div>

                </div>
            </div>

            <!-- search bar -->
            <div class="grid grid-cols-12 gap-4 mt-20 md:mt-40 bg-white text-black px-4 rounded-md">
                <div class="col-span-12">
                    <div class="p-[24px]">
                        <form class="grid grid-cols-2 gap-4 md:grid-cols-7" @submit.prevent="searchFlights">
                            <!-- from -->
                            <div class="col-span-1 flex justify-center items-center">
                                <input v-model="formData.from" type="text"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                                    placeholder="出发地" />
                                <i class="text-black fas fa-sync ml-2"></i>
                            </div>
                            <!-- to -->
                            <div class="col-span-1">
                                <input v-model="formData.to" type="text"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                                    placeholder="目的地" />
                            </div>
                            <!-- depart -->
                            <div class="col-span-1">
                                <input v-model="formData.depart" type="date"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                                    placeholder="depart" />
                            </div>
                            <!--  way -->
                            <div class="col-span-1">
                                <select v-model="formData.inputWay"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                                    placeholder="方式">
                                    <option selected>直达</option>
                                    <option>转机</option>
                                </select>
                            </div>
                            <!-- passengers -->
                            <div class="col-span-1">
                                <select v-model="formData.passengers"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                                    placeholder="人数">
                                    <option selected>1人</option>
                                    <option>2人</option>
                                    <option>3人</option>
                                </select>
                            </div>

                            <!-- type -->
                            <div class="col-span-1">
                                <select v-model="formData.type"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                                    placeholder="航班类型">
                                    <option selected>经济</option>
                                    <option>商务</option>
                                </select>
                            </div>
                            <!-- button -->
                            <div class="col-span-2 md:col-span-1">
                                <button type="submit"
                                    class="search-btn text-white min-h-[48px] w-full text-[15px] py-[5px] px-[30px] bg-blue-600 hover:opacity-90 rounded-md">查询
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 模态框 -->
    <div v-if="showModal" class="modal-overlay" @click="closeModal">
        <div class="modal" @click.stop>
            <div class="flex w-full max-w-sm overflow-hidden bg-white rounded-lg shadow-md dark:bg-gray-800">
                <div class="flex items-center justify-center w-12 bg-yellow-400">
                    <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM21.6667 28.3333H18.3334V25H21.6667V28.3333ZM21.6667 21.6666H18.3334V11.6666H21.6667V21.6666Z" />
                    </svg>
                </div>

                <div class="px-4 py-2 -mx-3">
                    <div class="mx-3">
                        <span class="font-semibold text-yellow-400 dark:text-yellow-300">Warning</span>
                        <p class="text-sm text-gray-600 dark:text-gray-200">
                            Please enter both departure and arrival locations.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
.ezy__travel1 {
    height: 100vh;
    background-image: url('../assets/photos/header35-img.png');
}

a.search-btn {
    text-align: center;
    line-height: 40px;
    display: block;
}

.modal-overlay {
    position: fixed;
    padding-top: 15px;
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