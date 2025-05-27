<script setup>
import { ref, onMounted, onUnmounted, computed, watch } from 'vue';
import { formData } from '@/stores/formdata';
import axios from 'axios';
import Search from '@/components/Search.vue';
import {useAuthStore} from '../stores/user_store.js'

const authStore = useAuthStore();
const depart = ref();
const flightsData = ref([]);
const loading = ref(true);
const showSearch = ref(false);
const isLoggedIn = ref(false);
const priceNumber = ref(0);
const FlyTime = ref(0);
const flights_company = ref("");
const Price_flightsData = ref([]);
const new_flightsData = ref([]);
const showNoFlightsModal = ref(false);
const selectedPrice = ref(2000);
const selectedTime = ref(null);
const selectedCompany = ref(null);

// // 从 localStorage 加载 formData
if (localStorage.getItem('formData')) {
    Object.assign(formData, JSON.parse(localStorage.getItem('formData')));
    console.log("formData: ",formData);
}

function select_price_flightData(price) {
    // 确保 price 是数字类型
    priceNumber.value = parseFloat(price);
    selectedPrice.value = price;
    // 使用 filter 方法查找低于指定价格的航班
    Price_flightsData.value = flightsData.value.filter(flight => parseFloat(flight.price) < priceNumber.value);
}

function select_time_flightData(time) {
    FlyTime.value = parseFloat(time);
    console.log("FlyTime: ",FlyTime.value);
    // 使用 filter 方法查找起飞时间早于指定时间的航班
    selectedTime.value = time; 
    Price_flightsData.value = flightsData.value.filter(flight => parseFloat(flight.departureParsed.hour) < FlyTime.value);
    console.log("Price_flightsData: ",Price_flightsData.value);
}

function select_company_flightData(company) {
    flights_company.value = company;
    console.log("flights_company: ",flights_company.value);
    // 使用 filter 方法查找特定公司航班
    Price_flightsData.value = flightsData.value.filter(flight => flight.airline === flights_company.value);
    console.log("Price_flightsData: ",Price_flightsData.value);
}

function clear_data()
{
    priceNumber.value = 0;
    FlyTime.value = 0;
    flights_company.value = "";
    selectedPrice.value = null;
    selectedTime.value = null;
    selectedCompany.value = null; 
}

// 移除 new_flightsData.value = filtered; 从 computed 中
const filteredFlights = computed(() => {

    if(priceNumber.value === 0 && FlyTime.value === 0 && flights_company.value === ""){
        return flightsData.value;
    }

    let filtered = flightsData.value;

    if (priceNumber.value !== 0) {
        filtered = filtered.filter(flight => parseFloat(flight.price) < priceNumber.value);
    }
    if (FlyTime.value !== 0) {
        filtered = filtered.filter(flight => parseFloat(flight.departureParsed.hour) < FlyTime.value);
    }
    if (flights_company.value !== "") {
        filtered = filtered.filter(flight => flight.airline === flights_company.value);
    }
    checkAndShowNoFlightsModal(filtered); // 调用方法更新模态框状态
    return filtered.length > 0 ? filtered : []; // 返回计算结果
});

// 定义一个方法来控制 showNoFlightsModal
function checkAndShowNoFlightsModal(filtered) {
    if (filtered.length > 0) {
        showNoFlightsModal.value = false; // 如果有结果，隐藏模态框
    } else {
        showNoFlightsModal.value = true; // 如果没有结果，显示模态框
    }
}

// 使用 watch 监听 filteredFlights 的变化并更新 new_flightsData
watch(filteredFlights, (newFilteredFlights) => {
    new_flightsData.value = newFilteredFlights; // 在这里更新 new_flightsData
}, { immediate: true }); // 立即执行一次以初始化 new_flightsData


const flightsData_length = computed(() => {
    return new_flightsData.value.length !== 0 ?  new_flightsData.value.length :  flightsData.value.length;
});

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

function closeModal() {
    showNoFlightsModal.value = false;
    clear_data();
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
        });
      // 保存 formData 到 localStorage
    localStorage.setItem('formData', JSON.stringify(formData));
    console.log("flight: ",flightsData.value);

    } catch (error) {
        console.error('Error fetching flights:', error);
    } finally {
        loading.value = false;
    }
}


onMounted(async () => { // 声明为 async 函数
    window.scrollTo({
    top: 0,
    });
    await searchFlights(); // 使用 await 调用异步函数
    console.log("被调用");
    // clear_data();
    isLoggedIn.value = await authStore.CheckLogin(); // 使用 await 获取 CheckLogin 的结果
});

onUnmounted(() => {
    // 清除 localStorage 中的 formData 内容
    localStorage.removeItem('formData');
    console.log()
    console.log("localStorage cleared")
});

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

// function submitFilters() {
//     // 这里可以添加提交筛选条件的逻辑，例如重新过滤航班数据
//     console.log("筛选条件已提交");
// }


function handleBooking(id) {
    if (isLoggedIn.value) {
        window.location.href = `/ticket/verify/${id}`;
    }else{
        window.location.href = '/login';
    }
}
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
                            <div>
                                <h3 class="text-[28px] font-medium mb-1 sm:mb-2 leading-none">{{ depart }} ↦ {{ formData.to }}</h3>
                                <p class="mb-0 opacity-75 font-normal">{{ formData.depart }} | 直达</p>
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
            <Search v-if="showSearch" :search-flights="searchFlights"></Search>
            <!-- body portion -->
            <div class="grid grid-cols-12 gap-4 mt-10 ">
                <!-- filter -->
                <div class="col-span-12 lg:col-span-3 md:pl-0 bg-[#F6F6F6] dark:bg-transparent">
                    <div class="h-full rounded-md border border-[#E1E6EA] dark:border-[#555669] pb-4">
                        <div class="text-white bg-[#404156] dark:bg-[#282836] rounded p-8 text-center">
                            <h3 class="text-[28px] leading-[1px] font-medium mb-0">筛选</h3>
                        </div>

                        <form>
                            <!-- price range -->
                            <div>
                                <a id="travel4BTN"
                                    class="p-3 lg:p-6 w-full text-start flex justify-between items-center focus:shadow-none"
                                    href="#!">
                                    <h5 class="mb-0 font-medium text-[20px] text-[#28303B] dark:text-white">价格范围
                                    </h5>
                                    <span class="fas fa-chevron-down"></span>
                                </a>
                                <div id="travel4Modal2">
                                    <div class="px-3 lg:px-4 lg:pb-4 mt-4">
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none"
                                            :class="{ 'bg-blue-600 text-white': selectedPrice === 500 }"
                                            @click="select_price_flightData(500); submitFilters()">
                                            <i class="fas fa-cloud-sun mr-6"></i>500以下
                                        </button>
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2"
                                            :class="{ 'bg-blue-600 text-white': selectedPrice === 800 }"
                                            @click="select_price_flightData(800); submitFilters()">
                                            <i class="fas fa-cloud-moon mr-6"></i>800以下
                                        </button>
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2"
                                            :class="{ 'bg-blue-600 text-white': selectedPrice === 2000 }"
                                            @click="select_price_flightData(2000); submitFilters()">
                                            <i class="fas fa-cloud mr-6"></i>2000以下
                                        </button>
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
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none"
                                            :class="{ 'bg-blue-600 text-white': selectedTime === 6 }"
                                            @click="select_time_flightData(6); submitFilters()">
                                            <i class="fas fa-cloud-sun mr-6"></i>6点之前
                                        </button>
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2"
                                            :class="{ 'bg-blue-600 text-white': selectedTime === 12 }"
                                            @click="select_time_flightData(12); submitFilters()">
                                            <i class="fas fa-cloud-moon mr-6"></i>12点之前
                                        </button>
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2"
                                            :class="{ 'bg-blue-600 text-white': selectedTime === 18 }"
                                            @click="select_time_flightData(18); submitFilters()">
                                            <i class="fas fa-cloud mr-6"></i>18点之前
                                        </button>
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2"
                                            :class="{ 'bg-blue-600 text-white': selectedTime === 24 }"
                                            @click="select_time_flightData(24); submitFilters()">
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
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none"
                                            :class="{ 'bg-blue-600 text-white': selectedCompany === '南方航空' }"
                                            @click="select_company_flightData('南方航空'); submitFilters()">
                                            南方航空
                                        </button>
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2"
                                            :class="{ 'bg-blue-600 text-white': selectedCompany === '海南航空' }"
                                            @click="select_company_flightData('海南航空'); submitFilters()">
                                            海南航空
                                        </button>
                                        <button type="button"
                                            class="w-full text-[#28303b] dark:text-white hover:text-white text-[18px] font-medium bg-[#EDF2F6] dark:bg-[#4C4D61] hover:bg-[#404156] dark:hover:bg-[#282836]  py-[5px] px-[20px] border-none mt-2"
                                            :class="{ 'bg-blue-600 text-white': selectedCompany === '东方航空' }"
                                            @click="select_company_flightData('东方航空'); submitFilters()">
                                            东方航空
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <div class="px-4 mt-4">
<!--                                <button-->
<!--                                    class="text-white h-[46px] font-medium py-[8px] px-[25px] bg-blue-600 hover:opacity-90 rounded w-full"-->
<!--                                    @click="submitFilters">提交选项</button>-->
                                <button
                                    class="text-white h-[46px] font-medium py-[8px] px-[25px] bg-blue-600 hover:opacity-90 rounded w-full mt-2"
                                    @click="clear_data">重置所有选项</button>
                            </div>
                        </form>

                    </div>
                </div>

                <!-- results -->
                <div class="col-span-12 lg:col-span-9 mt-4 lg:mt-0">
                    <!-- filters -->
                    <div class="grid grid-cols-12 gap-4">
                        <div class="col-span-12 sm:col-span-6">
                            <h4 class="mb-0 font-medium text-[24px] text-[#28303B] dark:text-white">{{ flightsData_length }} 条结果</h4>
                        </div>
                    </div>

                    <div>
                      <!-- 弹窗 -->
                        <div v-if="showNoFlightsModal" class="fixed inset-0 flex items-center justify-center bg-gray-100 bg-opacity-10">
                            <div class="bg-white p-8 rounded-lg shadow-lg">
                                <p class="text-lg font-medium mb-4">抱歉,没有找到符合条件的机票</p>
                                <button class="text-white h-[46px] font-medium py-[8px] px-[25px] bg-blue-600 hover:opacity-90 rounded" @click="closeModal">关闭</button>
                            </div>
                        </div>

                      <!-- 航班列表 -->
                      <div v-else>
                        <div v-for="(flight, index) in filteredFlights" :key="index" class="grid grid-cols-12 mt-4">

                            <div class="col-span-12 lg:col-span-10 lg:pr-0">
                                <div
                                    class="bg-[#F6F6F6] dark:bg-transparent border border-[#E1E6EA] dark:border-[#555669] rounded-md grid grid-cols-12 gap-4 items-center h-full p-2">
                                    <!-- airlines name -->
                                    <div class="col-span-6 sm:col-span-3">
                                        <div class="flex items-center">
                                            <div class="p-4">
                                                <!-- <img src="https://cdn.easyfrontend.com/pictures/airlines_logo1.png"
                                                    alt="" class="w-full h-auto" width="47" /> -->
                                            </div>
                                            <div>
                                                <h4 class="font-medium ml-10 mb-0 text-[16px] opacity-75">
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
                                    class="rightbox bg-[#F6F6F6] dark:bg-transparent border border-[#E1E6EA] dark:border-[#555669] rounded-md ezy__travel4-price p-2 lg:p-4 text-center h-full flex flex-col items-center justify-center ml-0">
                                    <h2 class="text-[32px] font-bold mb-1">￥{{ flight.price }}</h2>
                                    <button class="h-[46px] py-[8px] px-[25px] text-white bg-blue-600 border border-blue-600 hover:opacity-90 rounded-sm font-bold mt-8 sm:mt-0" @click="handleBooking(flight.id)" >
                                        预订
                                    </button>
                                    <span class="remainbox">剩{{ flight.remaining_seats }}张</span>
                                </div>
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

.rightbox {
    position: relative;
}

.rightbox .remainbox {
    position: absolute;
    color: #fff;
    right: 0;
    background-color: #FF9900;
}
</style>


