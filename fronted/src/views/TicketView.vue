<script setup>
import { ref, onMounted, watch } from 'vue';
import { formData } from '@/stores/formdata';
import axios from 'axios';

const depart = ref();
const flightsData = ref([]);
const loading = ref(true);
const showSearch = ref(false);
// 辅助函数：解析日期字符串并提取日期和时间部分
function parseDateTime(dateTimeString) {
    const date = new Date(dateTimeString);

    return {
        year: date.getFullYear(),
        month: date.getMonth() + 1, // 月份从0开始，需要加1
        day: date.getDate(),
        hour: date.getHours().toString().padStart(2, '0'),
        minute: date.getMinutes().toString().padStart(2, '0'),
        weekday: date.getDay(), // 0 表示星期日，1 表示星期一，依此类推
        weekdayName: ["周日", "周一", "周二", "周三", "周四", "周五", "周六"][date.getDay()]
    };
}

function calDuration(departureTime, arrivalTime) {
    const departure = new Date(departureTime);
    const arrival = new Date(arrivalTime);
    const duration = (arrival - departure) / 1000; // 转换为秒
    const hours = Math.floor(duration / 3600);
    const minutes = Math.floor((duration % 3600) / 60);
    return {
        hours: hours.toString().padStart(2, '0'), // 确保小时是两位数
        minutes: minutes.toString().padStart(2, '0') // 确保分钟是两位数
    };
}
function toggleSearch() {
    showSearch.value = !showSearch.value;
}
// 搜索航班信息
async function searchFlights() {
    try {
        const response = await axios.post('http://localhost:8000/back/flights/', formData);
        depart.value = formData.from;
        flightsData.value = response.data.map(flight => {
            return {
                ...flight,
                departureParsed: parseDateTime(flight.departure_time),
                arrivalParsed: parseDateTime(flight.arrival_time),
                duration: calDuration(flight.departure_time, flight.arrival_time),
            }
        })
    } catch (error) {
        console.error('Error fetching flights:', error);
    } finally {
        loading.value = false;
    }
}

onMounted(() => {
    searchFlights();
})

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
                                <h3 class="text-[28px] font-medium mb-1 sm:mb-2 leading-none">{{ depart }}</h3>
                                <p class="mb-0 opacity-75 font-normal">JUN 04,SAT | 2TRAVELLERS</p>
                            </div>
                        </div>
                        <div class="col-span-12 sm:col-span-4 flex items-center justify-center sm:justify-end">
                            <button v-on:click="toggleSearch"
                                class="h-[46px] py-[8px] px-[25px] text-white bg-blue-600 border border-blue-600 hover:opacity-90 rounded-md font-bold mt-8 sm:mt-0">更改
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <!-- 弹出搜索框 -->
            <div v-if="showSearch" class="searchbox grid grid-cols-12 gap-4 mt-20 md:mt-40 bg-white text-black px-4 rounded-md">
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
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500">
                                    <option selected>直达</option>
                                    <option>转机</option>
                                </select>
                            </div>
                            <!-- passengers -->
                            <div class="col-span-1">
                                <select v-model="formData.passengers"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500">
                                    <option selected>1人</option>
                                    <option>2人</option>
                                    <option>3人</option>
                                </select>
                            </div>

                            <!-- type -->
                            <div class="col-span-1">
                                <select v-model="formData.type"
                                    class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500">
                                    <option selected>经济</option>
                                    <option>商务</option>
                                </select>
                            </div>
                            <!-- button -->
                            <div class="col-span-2 md:col-span-1">
                               <button v-on:click="searchFlights" type="button"
                                    class="search-btn text-white min-h-[48px] w-full text-[15px] py-[5px] px-[30px] bg-blue-600 hover:opacity-90 rounded-md">查询
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <!-- body portion -->
            <div class="grid grid-cols-12 gap-4 mt-10 ">
                <!-- filter -->
                <div class="col-span-12 lg:col-span-3 md:pl-0 bg-[#F6F6F6] dark:bg-transparent">
                    <div class="h-full rounded-md border border-[#E1E6EA] dark:border-[#555669] pb-4">
                        <div class="text-white bg-[#404156] dark:bg-[#282836] rounded p-8 text-center">
                            <h3 class="text-[28px] leading-[1px] font-medium mb-0">筛选</h3>
                        </div>

                        <form action="">
                            <!-- price range -->
                            <div>
                                <a id="travel4BTN"
                                    class="p-3 lg:p-6 w-full text-start flex justify-between items-center focus:shadow-none"
                                    href="#!">
                                    <h5 class="mb-0 font-medium text-[20px] text-[#28303B] dark:text-white">价格范围
                                    </h5>
                                    <span class="fas fa-chevron-down"></span>
                                </a>
                                <div id="travel4Modal">
                                    <div class="px-3 lg:px-4 lg:pb-4 mt-3">
                                        <div class="mb-2">
                                            <label class="font-bold mb-2 opacity-75">最低价(￥100)</label>
                                            <input type="range"
                                                class="h-2 w-full bg-[#DEE2E6] appearance-none rounded-sm" />
                                        </div>
                                        <div class="mb-2">
                                            <label class="font-bold mb-2 opacity-75">最高价(￥2000)</label>
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
                                    <h5 class="mb-0 font-medium text-[20px] text-[#28303B] dark:text-white">起飞时间
                                    </h5>
                                    <span class="fas fa-chevron-down"></span>
                                </a>
                                <div id="travel4Modal2">
                                    <div class="px-3 lg:px-4 lg:pb-4 mt-4">
                                        <button
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none">
                                            <i class="fas fa-cloud-sun mr-6"></i>6点之前
                                        </button>
                                        <button
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2">
                                            <i class="fas fa-cloud-moon mr-6"></i>12点之前
                                        </button>
                                        <button
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2">
                                            <i class="fas fa-cloud mr-6"></i>18点之前
                                        </button>
                                        <button
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2">
                                            <i class="fas fa-sun mr-6"></i>24点之前
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- airlines -->
                            <div>
                                <a id="travel4BTN4"
                                    class="p-3 lg:p-6 w-full text-start flex justify-between items-center focus:shadow-none"
                                    href="#!">
                                    <h5 class="mb-0 font-medium text-[20px] text-[#28303B] dark:text-white">航空公司
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
                                        <h4 class="text-[28px] md:text-[32px] font-medium">{{ flight.departureParsed.hour }}:{{ flight.departureParsed.minute }}</h4>
                                        <p class="mb-1 mt-2 opacity-50">{{flight.departureParsed.month }}月{{ flight.departureParsed.day }}日, {{ flight.departureParsed.weekdayName }}</p>
                                        <p class="mb-0 opacity-100 font-bold text-[16px]">{{ flight.departure_city }}</p>
                                    </div>
                                    <!-- stops -->
                                    <div class="text-center col-span-6 sm:col-span-3">
                                        <p class="mb-0 opacity-50">历时{{ flight.duration.hours }}时{{ flight.duration.minutes }}分</p>
                                        <hr
                                            class="relative h-[2px] bg-slate-400 overflow-visible opacity-100 dark:opacity-50 before:content-[''] before:absolute before:top-1/2 before:-translate-y-1/2 before:left-0 before:bg-slate-400 dark:before:bg-gray-300 before:w-2 before:h-2 before:rounded-full after:content-[''] after:absolute after:top-1/2 after:-translate-y-1/2 after:right-0 after:bg-slate-400 dark:after:bg-gray-300 after:w-2 after:h-2 after:rounded-full my-2" />
                                        
                                    </div>

                                    <!-- time -->
                                    <div class="text-center col-span-6 sm:col-span-3">
                                        <h4 class="text-[28px] md:text-[32px] font-medium">{{ flight.arrivalParsed.hour }}:{{ flight.arrivalParsed.minute }}</h4>
                                        <p class="mb-1 mt-2 opacity-50">{{flight.arrivalParsed.month }}月{{ flight.arrivalParsed.day }}日, {{ flight.arrivalParsed.weekdayName }}</p>
                                        <p class="mb-0 opacity-100 font-bold text-[16px]">{{ flight.arrival_city }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-span-12 lg:col-span-2 lg:pl-0">
                                <div
                                    class="bg-[#F6F6F6] dark:bg-transparent border border-[#E1E6EA] dark:border-[#555669] rounded-md ezy__travel4-price p-2 lg:p-4 text-center h-full flex flex-col items-center justify-center ml-0">
                                    <h2 class="text-[32px] font-bold mb-1">￥{{ flight.price }}</h2>
                                    <router-link :to="`/ticket/verify/${flight.id}`"
                                        class="h-[46px] py-[8px] px-[25px] text-white bg-blue-600 border border-blue-600 hover:opacity-90 rounded-sm font-bold mt-8 sm:mt-0">预订
                                    </router-link>
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
.searchbox {
    margin-top: 20px;
}
</style>


