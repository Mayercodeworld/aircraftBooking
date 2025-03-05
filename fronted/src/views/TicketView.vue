<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const flightsData = ref([]);
const loading = ref(true);

// 监听路由变化，当查询参数变化时重新发送请求
watch(() => route.query, async (newQuery) => {
    await fetchFlights(newQuery);
}, { immediate: true });

async function fetchFlights(queryParams) {
    try {
        const response = await axios.post('http://localhost:8000/back/flights/', queryParams);
        flightsData.value = response.data;
    } catch (error) {
        console.error('Error fetching flights:', error);
    } finally {
        loading.value = false;
    }
}

// function toggleModal(btnId, modalId) {
//             const button = document.getElementById(btnId);
//             const modal = document.getElementById(modalId);

//             button.addEventListener("click", () => {
//                 modal.classList.toggle("hidden");
//             });
//         }

// document.addEventListener("DOMContentLoaded", () => {
//     const buttonsAndModals = [
//         { btnId: "travel4BTN", modalId: "travel4Modal" },
//         { btnId: "travel4BTN2", modalId: "travel4Modal2" },
//         { btnId: "travel4BTN3", modalId: "travel4Modal3" },
//         { btnId: "travel4BTN4", modalId: "travel4Modal4" },
//     ]
//     buttonsAndModals.forEach(({ btnId, modalId }) => {
//         toggleModal(btnId, modalId);
//     });
// });
</script>
<template>
    <section
        class="ezy__travel4 light bg-white dark:bg-[#404156] text-zinc-900 dark:text-white py-10 md:py-[80px] flex flex-col justify-center items-center overflow-hidden">
        <div class="container px-4 md:px-20 mx-auto">
            <!-- header portion -->
            <div class="grid grid-cols-12">
                <div class="col-span-12">
                    <div
                        class="grid grid-cols-12 text-white bg-[#404156] dark:bg-[#282836] p-4 lg:p-[48px] rounded-md border-none">
                        <div class="col-span-12 sm:col-span-8 flex p-4">
                            <div
                                class="text-[#28303B] dark:text-white bg-white dark:bg-[#404156] w-[65px] h-[65px] text-[24px] flex items-center justify-center rounded-full mr-4">
                                <i class="fas fa-paper-plane"></i>
                            </div>
                            <div>
                                <h3 class="text-[28px] font-medium mb-1 sm:mb-2 leading-none">Los Angeles-Istanbul</h3>
                                <p class="mb-0 opacity-75 font-normal">JUN 04,SAT | 2TRAVELLERS</p>
                            </div>
                        </div>
                        <div class="col-span-12 sm:col-span-4 flex items-center justify-center sm:justify-end">
                            <button
                                class="h-[46px] py-[8px] px-[25px] text-white bg-blue-600 border border-blue-600 hover:opacity-90 rounded-md font-bold mt-8 sm:mt-0">Change</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- body portion -->
            <div class="grid grid-cols-12 gap-4 mt-10 ">
                <!-- filter -->
                <div class="col-span-12 lg:col-span-3 md:pl-0 bg-[#F6F6F6] dark:bg-transparent">
                    <div class="h-full rounded-md border border-[#E1E6EA] dark:border-[#555669] pb-4">
                        <div class="text-white bg-[#404156] dark:bg-[#282836] rounded p-8 text-center">
                            <h3 class="text-[28px] leading-[1px] font-medium mb-0">FILTERS</h3>
                        </div>

                        <form action="">
                            <!-- price range -->
                            <div>
                                <a id="travel4BTN"
                                    class="p-3 lg:p-6 w-full text-start flex justify-between items-center focus:shadow-none"
                                    href="#!">
                                    <h5 class="mb-0 font-medium text-[20px] text-[#28303B] dark:text-white">Price Range
                                    </h5>
                                    <span class="fas fa-chevron-down"></span>
                                </a>
                                <div id="travel4Modal">
                                    <div class="px-3 lg:px-4 lg:pb-4 mt-3">
                                        <div class="mb-2">
                                            <label class="font-bold mb-2 opacity-75">Min
                                                Price($200)</label>
                                            <input type="range"
                                                class="h-2 w-full bg-[#DEE2E6] appearance-none rounded-sm" />
                                        </div>
                                        <div class="mb-2">
                                            <label class="font-bold mb-2 opacity-75">Max Price($2000)</label>
                                            <input type="range"
                                                class="h-2 w-full bg-[#DEE2E6] appearance-none rounded-sm" />
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- depart time -->
                            <div>
                                <a id="travel4BTN2"
                                    class="p-3 lg:p-6 w-full text-start flex justify-between items-center focus:shadow-none"
                                    href="#!">
                                    <h5 class="mb-0 font-medium text-[20px] text-[#28303B] dark:text-white">Depart Time
                                    </h5>
                                    <span class="fas fa-chevron-down"></span>
                                </a>
                                <div id="travel4Modal2">
                                    <div class="px-3 lg:px-4 lg:pb-4 mt-4">
                                        <button
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none">
                                            <i class="fas fa-cloud-sun mr-6"></i>Before 6 am
                                        </button>
                                        <button
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2">
                                            <i class="fas fa-cloud-moon mr-6"></i>Before 6 am
                                        </button>
                                        <button
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2">
                                            <i class="fas fa-cloud mr-6"></i>Before 6 am
                                        </button>
                                        <button
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2">
                                            <i class="fas fa-sun mr-6"></i>Before 6 am
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- stops -->
                            <div>
                                <a id="travel4BTN3"
                                    class="p-3 lg:p-6 w-full text-start flex justify-between items-center focus:shadow-none"
                                    href="#!">
                                    <h5 class="mb-0 font-medium text-[20px] text-[#28303B] dark:text-white">Stops</h5>
                                    <span class="fas fa-chevron-down"></span>
                                </a>
                                <div id="travel4Modal3">
                                    <div class="px-3 lg:px-4 lg:pb-4 mt-4">
                                        <div class="grid grid-cols-12 gap-4">
                                            <div class="col-span-4">
                                                <button
                                                    class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none">0</button>
                                            </div>
                                            <div class="col-span-4">
                                                <button
                                                    class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none">1</button>
                                            </div>
                                            <div class="col-span-4">
                                                <button
                                                    class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none">2+</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- airlines -->
                            <div>
                                <a id="travel4BTN4"
                                    class="p-3 lg:p-6 w-full text-start flex justify-between items-center focus:shadow-none"
                                    href="#!">
                                    <h5 class="mb-0 font-medium text-[20px] text-[#28303B] dark:text-white">Airlines
                                    </h5>
                                    <span class="fas fa-chevron-down peer"></span>
                                </a>
                                <div id="travel4Modal4">
                                    <div class="px-3 lg:px-4 lg:pb-4 mt-2">
                                        <div>
                                            <div>
                                                <input class="w-[16px] h-[16px] cursor-pointer mr-6 rounded-sm"
                                                    type="checkbox" value="" />
                                                <label class="opacity-80"> Aeroflot
                                                </label>
                                            </div>
                                            <div class="mt-3">
                                                <input class="w-[16px] h-[16px] cursor-pointer mr-6 rounded-sm"
                                                    type="checkbox" value="" checked />
                                                <label class="opacity-80"> Aeroflot
                                                </label>
                                            </div>
                                            <div class="mt-3">
                                                <input class="w-[16px] h-[16px] cursor-pointer mr-6 rounded-sm"
                                                    type="checkbox" value="" />
                                                <label class="opacity-80"> Aeroflot
                                                </label>
                                            </div>
                                            <div class="mt-3">
                                                <input class="w-[16px] h-[16px] cursor-pointer mr-6 rounded-sm"
                                                    type="checkbox" value="" />
                                                <label class="opacity-80"> Aeroflot
                                                </label>
                                            </div>
                                            <div class="mt-3">
                                                <input class="w-[16px] h-[16px] cursor-pointer mr-6 rounded-sm"
                                                    type="checkbox" value="" />
                                                <label class="opacity-80"> Aeroflot
                                                </label>
                                            </div>
                                            <div class="mt-3">
                                                <input class="w-[16px] h-[16px] cursor-pointer mr-6 rounded-sm"
                                                    type="checkbox" value="" />
                                                <label class="opacity-80"> Aeroflot
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="px-4 mt-4">
                                <button
                                    class="text-white h-[46px] font-medium py-[8px] px-[25px] bg-blue-600 hover:opacity-90 rounded w-full">Reset
                                    All Filters</button>
                            </div>
                        </form>
                    </div>
                </div>

                <!-- results -->
                <div class="col-span-12 lg:col-span-9 mt-4 lg:mt-0">
                    <!-- filters -->
                    <div class="grid grid-cols-12 gap-4">
                        <div class="col-span-12 sm:col-span-6">
                            <h4 class="mb-0 font-medium text-[24px] text-[#28303B] dark:text-white">{{ flightsData.length }} 条结果</h4>
                        </div>
                        <div class="col-span-12 sm:col-span-6">
                            <form action="" class="flex items-center sm:justify-end">
                                <h5 class="font-normal mb-0 mr-6 text-nowrap text-[20px] w-1/2">筛选：</h5>
                                <select
                                    class="text-[#20283B] dark:text-white bg-[#F6F6F6] dark:bg-[#404156] border border-[#ffffff1c] py-[6px] pr-[36px] pl-[12px] focus:outline-2 focus:outline-blue-500 focus:border-blue-500 w-full">
                                    <option selected>成人价</option>
                                    <option value="1">学生价</option>
                                </select>
                            </form>
                        </div>
                    </div>

                    <div>
                        <!-- item -->
                        <div v-for="(flight, index) in flightsData" :key="index" class="grid grid-cols-12 mt-4">
                            
                            <div class="col-span-12 lg:col-span-10 lg:pr-0">
                                <div
                                    class="bg-[#F6F6F6] dark:bg-transparent border border-[#E1E6EA] dark:border-[#555669] rounded-md grid grid-cols-12 gap-4 items-center h-full p-2">
                                    <!-- airlines name -->
                                    <div class="col-span-6 sm:col-span-3">
                                        <div class="flex items-center">
                                            <div class="p-3">
                                                <img src="https://cdn.easyfrontend.com/pictures/airlines_logo1.png"
                                                    alt="" class="w-full h-auto" width="47" />
                                            </div>
                                            <div>
                                                <h4 class="font-medium mb-0 text-[16px] opacity-75">
                                                    {{ flight.airline }} <br />
                                                    {{ flight.flight_no }}
                                                </h4>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- time -->
                                    <div class="text-center col-span-6 sm:col-span-3">
                                        <h4 class="text-[28px] md:text-[32px] font-medium">{{ flight.departure_hour }}:{{ flight.departure_minute }}</h4>
                                        <p class="mb-1 mt-2 opacity-50">{{flight.arrival_month}}月{{ flight.arrival_day }}日, {{ flight.arrival_weekday_name }}</p>
                                        <p class="mb-0 opacity-100 font-bold text-[16px]">{{ flight.departure_city }}</p>
                                    </div>
                                    <!-- stops -->
                                    <div class="text-center col-span-6 sm:col-span-3">
                                        <p class="mb-0 opacity-50">31h 10m</p>
                                        <hr
                                            class="relative h-[2px] bg-slate-400 overflow-visible opacity-100 dark:opacity-50 before:content-[''] before:absolute before:top-1/2 before:-translate-y-1/2 before:left-0 before:bg-slate-400 dark:before:bg-gray-300 before:w-2 before:h-2 before:rounded-full after:content-[''] after:absolute after:top-1/2 after:-translate-y-1/2 after:right-0 after:bg-slate-400 dark:after:bg-gray-300 after:w-2 after:h-2 after:rounded-full my-2" />
                                        <p class="mb-0 opacity-50">2 Stops</p>
                                    </div>

                                    <!-- time -->
                                    <div class="text-center col-span-6 sm:col-span-3">
                                        <h4 class="text-[28px] md:text-[32px] font-medium">{{ flight.arrival_hour }}:{{ flight.arrival_minute }}</h4>
                                        <p class="mb-1 mt-2 opacity-50">{{flight.arrival_month}}月{{ flight.arrival_day }}日, {{ flight.arrival_weekday_name }}</p>
                                        <p class="mb-0 opacity-100 font-bold text-[16px]">{{ flight.arrival_city }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-span-12 lg:col-span-2 lg:pl-0">
                                <div
                                    class="bg-[#F6F6F6] dark:bg-transparent border border-[#E1E6EA] dark:border-[#555669] rounded-md ezy__travel4-price p-2 lg:p-4 text-center h-full flex flex-col items-center justify-center ml-0">
                                    <h2 class="text-[32px] font-bold mb-1">￥{{ flight.price }}</h2>
                                    <button
                                        class="h-[46px] py-[8px] px-[25px] text-white bg-blue-600 border border-blue-600 hover:opacity-90 rounded-sm font-bold mt-8 sm:mt-0">预订
                                    </button>
                                </div>
                            </div>
                        </div>
                   
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>
<style scoped>

</style>


