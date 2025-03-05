<!-- Search.vue -->
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();

const formData = ref({
    from: '',
    to: '',
    depart: '',
    inputWay: 'One Way',
    passengers: '1 Passenger',
    type: 'Business'
});

const searchFlights = () => {
    // 将表单数据作为查询参数传递给 TicketView.vue
    router.push({ path: '/tickets', query: { ...formData.value } });
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
                                    placeholder="From" />
                                <i class="text-black fas fa-sync ml-2"></i>
                            </div>
                            <!-- to -->
                            <div class="col-span-1">
                                <input v-model="formData.to" type="text"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                                    placeholder="To" />
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
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500">
                                    <option selected>One Way</option>
                                    <option>Multiple Way</option>
                                </select>
                            </div>
                            <!-- passengers -->
                            <div class="col-span-1">
                                <select v-model="formData.passengers"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500">
                                    <option selected>1 Passenger</option>
                                    <option>2 Passengers</option>
                                    <option>3 Passengers</option>
                                    <option>4 Passengers</option>
                                    <option>5 Passengers</option>
                                </select>
                            </div>

                            <!-- type -->
                            <div class="col-span-1">
                                <select v-model="formData.type"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500">
                                    <option selected>Business</option>
                                    <option>Economy</option>
                                    <option>1st Class</option>
                                </select>
                            </div>
                            <!-- button -->
                            <div class="col-span-2 md:col-span-1">
                                <button type="submit"
                                    class="search-btn text-white min-h-[48px] w-full text-[15px] py-[5px] px-[30px] bg-blue-600 hover:opacity-90 rounded-md">Search
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
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
</style>