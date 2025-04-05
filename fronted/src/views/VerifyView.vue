<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useAuthStore } from '../stores/user_store.js';
import axios from 'axios';
import router from '@/router';

const num = ref(0);
const showModal1 = ref(false);
const showModal2 = ref(false);
const selectedInsurance = ref(null);
const insprice = ref(0);
const route = useRoute();
const flight = ref([]);
const flightId = ref(route.params.id);
const loading = ref(true);
const isPaid = ref(false);
const isNull = ref(false);
const countdown = ref(5);
const authStore = useAuthStore();
const formData = ref({
    user: authStore.user_id,
    flight: flightId.value,
    name: '',
    age: '',
    gender: '',
    country: '',
    passportNo: '',
    price: 0,
});
const seats = ref([]);
const seatLetter = ref(null); // 新增座位字母字段
const alreadyPaid = ref(false);

function checked(event) {
    // 移除之前选中的保险的高亮类
    if (selectedInsurance.value) {
        selectedInsurance.value.classList.remove('border-blue-600');
        selectedInsurance.value.classList.add('border-transparent');
    }

    // 获取当前点击的保险选项
    const newSelection = event.target.closest('.border-transparent');
    if (newSelection) {
        newSelection.classList.add('border-blue-600');
        newSelection.classList.remove('border-transparent');
        selectedInsurance.value = newSelection;
        insprice.value = parseInt(newSelection.querySelector('button').textContent.replace('￥', ''), 10);
    }
}

// function selectSeat(seat) {
//     if (seat.is_booked) {
//         alert('该座位已被预订');
//         return;
//     }
//     formData.value.seat = seat.id;
//     seats.value.forEach(s => {
//         s.selected = s.id === seat.id;
//     });
// }

function selectSeatLetter(letter) {
    seatLetter.value = letter;
}

function submit() {
    if (formData.value.name === '' || formData.value.age === '' || formData.value.gender === '' || formData.value.country === '' || formData.value.passportNo === '') {
        showModal2.value = true;
        isNull.value = true;
    } else {
        isNull.value = false;
        showModal1.value = true;
    }
    console.log(formData.value);
}

async function pay() {
    try {
        // 确保 flight 数据已加载
        if (!flightId.value) {
            console.error('Flight data is not loaded or invalid');
            return;
        }

        const totalPrice = parseFloat(flight.value.price) + (num.value * 80) + insprice.value;
        formData.value.price = totalPrice;
        formData.value.seat_letter = seatLetter.value; // 添加座位字母到 formData
        // formData.value.flight = flight.value.id; // 确保传递的是 flight_id
        // console.log('formData:', formData.value)
        // 发送购票请求之前，检查一下是否已经购买本票
        await axios.post(`http://localhost:8000/api/order/check/`, formData.value);
        // 没有购买直接创建订单
        await axios.post('http://localhost:8000/api/order/book/', formData.value);
        isPaid.value = true;

        // 启动倒计时
        let interval = setInterval(() => {
            countdown.value--;
            if (countdown.value <= 0) {
                clearInterval(interval);
                router.push('/ticket');
            }
        }, 1000);
    } catch (error) {
        console.error('Error creating order:', error);
        showModal2.value = true;
        alreadyPaid.value = true;
    }
}

async function searchFlightById() {
    try {
        const response = await axios.get(`http://localhost:8000/api/flights/${flightId.value}`);
        flight.value = response.data;
    } catch (error) {
        console.error('Error fetching flight:', error);
    } finally {
        loading.value = false;
    }
}

async function fetchSeats() {
    try {
        const response = await axios.get(`http://localhost:8000/api/flights/${flightId.value}/seats/`);
        seats.value = response.data.map(seat => ({
            ...seat,
            selected: false,
            is_booked: seat.is_booked || false // 确保 is_booked 属性存在
        }));
    } catch (error) {
        console.error('Error fetching seats:', error);
        seats.value = []; // 确保 seats 不为 undefined
    }
}

const closeModal = () => {
    showModal2.value = false;
    document.body.style.overflow = 'auto';
};

onMounted(() => {
    searchFlightById();
    fetchSeats();
});
</script>

<template>
    <section
        class="ezy__travel7 light bg-white dark:bg-[#2E2F41] text-gray-700 dark:text-white py-10 md:p-[100px] overflow-hidden">
        <div class="container px-4 mx-auto">
            <div class="grid grid-cols-12 gap-4">
                <div class="col-span-12">
                    <div class="bg-[#404156] p-6 rounded-md text-center">
                        <h2 class="font-bold text-2xl md:text-4xl leading-tight text-white mb-0">旅客信息</h2>
                    </div>
                </div>
            </div>

            <form class="shadow-2xl mt-10 p-4 md:p-[50px] border-none rounded-md">
                <div class="border-none rounded-md">
                    <div>
                        <div class="grid grid-cols-12 gap-4">
                            <div class="col-span-12">
                                <div class="flex items-center">
                                    <div class="w-[4px] h-[27px] rounded-md bg-[#0D6EFD]"></div>
                                    <h4 class="text-2xl font-bold mb-0 ml-3">个人信息</h4>
                                </div>
                            </div>
                            <!-- name -->
                            <div class="col-span-12 md:col-span-6 lg:col-span-4">
                                <label class="text-[18px] opacity-80 mb-0 font-medium" for="lName">姓名</label>
                                <div class="mt-4 md:mt-3 mb-4">
                                    <input type="text" v-model="formData.name"
                                        class="min-h-[48px] w-full leading-[36px] bg-transparent border boder-[#BBBFC8] dark:border-[#888993] pl-[24px] focus:outline focus:outline-blue-500 focus:border-none rounded-md opacity-75"
                                        id="lName" placeholder="姓名" />
                                </div>
                            </div>
                            <div class="col-span-12 md:col-span-6 lg:col-span-2">
                                <label class="text-[18px] opacity-80 mb-0 font-medium" for="bDate">年龄</label>
                                <div class="mt-4 md:mt-3 mb-4">
                                    <input type="text" v-model="formData.age"
                                        class="min-h-[48px] w-full leading-[36px] bg-transparent border boder-[#BBBFC8] dark:border-[#888993] pl-[24px] focus:outline focus:outline-blue-500 focus:border-none rounded-md opacity-75"
                                        id="bDate" placeholder="年龄" />
                                </div>
                            </div>
                            <div class="col-span-12 md:col-span-6 lg:col-span-2">
                                <label class="font-medium mb-0">性别</label>
                                <select v-model="formData.gender"
                                    class="min-h-[48px] leading-[36px] border border-[#BBBFC8] dark:border-[#888993] dark:bg-[#2E2F41] text-gray-400 px-4 w-full focus:outline focus:outline-blue-500 focus:border-none mt-3 mb-4 rounded-md"
                                    aria-label="Default select example">
                                    <option value="男" selected>男</option>
                                    <option value="女">女</option>
                                </select>
                            </div>
                        </div>

                        <div class="grid grid-cols-12 gap-4">
                            <!-- country -->
                            <div class="col-span-12 md:col-span-6 lg:col-span-4">
                                <label class="font-medium mb-0">国籍</label>
                                <select v-model="formData.country"
                                    class="min-h-[48px] leading-[36px] border border-[#BBBFC8] dark:border-[#888993] dark:bg-[#2E2F41] text-gray-400 px-4 w-full focus:outline focus:outline-blue-500 focus:border-none mt-3 mb-4 rounded-md"
                                    aria-label="Default select example">
                                    <option value="中国" selected>中国</option>
                                    <option value="美国">美国</option>
                                    <option value="法国">法国</option>
                                    <option value="英国">英国</option>

                                </select>
                            </div>
                            <!-- passport no -->
                            <div class="col-span-12 md:col-span-6 lg:col-span-4">
                                <label class="text-[18px] opacity-80 mb-0 font-medium" for="passport">身份证/护照</label>
                                <div class="mt-4 md:mt-3 mb-4">
                                    <input type="" v-model="formData.passportNo"
                                        class="min-h-[48px] w-full leading-[36px] bg-transparent border boder-[#BBBFC8] dark:border-[#888993] pl-[24px] focus:outline focus:outline-blue-500 focus:border-none rounded-md opacity-75"
                                        id="passport"/>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="grid grid-cols-12 gap-4 mt-6">
                        <div class="col-span-12">
                            <div class="flex items-center mb-4">
                                <div class="w-[4px] h-[27px] rounded-md bg-[#0D6EFD]"></div>
                                <h4 class="text-2xl font-bold mb-0 ml-3">选择座位</h4>
                            </div>
                            <div class="seat-map grid grid-cols-7 gap-2">
                                <!-- 添加座位字母选择按钮 -->
                                <div v-for="letter in ['A', 'B', 'C', 'D', 'E', 'F']" :key="letter" class="seat-letter w-10 h-10 flex items-center justify-center border border-gray-300 rounded cursor-pointer"
                                    :class="{ 'bg-blue-600 text-white': seatLetter === letter }"
                                    @click="selectSeatLetter(letter)">
                                    {{ letter }}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="grid grid-cols-12 gap-4 mt-6">
                        <div class="col-span-12">
                            <div class="flex items-center mb-4">
                                <div class="w-[4px] h-[27px] rounded-md bg-[#0D6EFD]"></div>
                                <h4 class="text-2xl font-bold mb-0 ml-3">行李托运</h4>
                            </div>
                            <div class="border border-[#888993] px-4 py-2 md:p-6">
                                <div class="grid grid-cols-12 gap-4 items-center">
                                    <div class="col-span-6 sm:col-span-4">
                                        <div>
                                            <h6 class="font-medium mb-0">小行李</h6>
                                        </div>
                                    </div>
                                    <div class="col-span-6 sm:col-span-4 md:col-span-5">
                                        <p class="mb-0 opacity-50">42x31x20cm</p>
                                    </div>
                                    <div class="col-span-6 sm:col-span-2">
                                        <div>
                                            <h6 class="mb-0 font-medium text-xl md:text-2xl">免费</h6>
                                        </div>
                                    </div>
                                </div>

                                <div class="grid grid-cols-12 gap-4 items-center mt-8">
                                    <div class="col-span-6 sm:col-span-4">
                                        <div>
                                            <h6 class="font-medium mb-0">大行李</h6>
                                        </div>
                                    </div>
                                    <div class="col-span-6 sm:col-span-4 md:col-span-5">
                                        <p class="mb-0 opacity-50">23kg</p>
                                    </div>
                                    <div class="col-span-6 sm:col-span-2">
                                        <div>
                                            <h6 class="mb-0 font-medium text-xl md:text-2xl">￥80</h6>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="grid grid-cols-12 gap-4 items-center mt-10">
                                <div class="col-span-6 sm:col-span-8">
                                    <div
                                        class="h-[48px] bg-[#F2F6FD] dark:bg-[#3E435A] flex flex-col justify-center px-[16px] w-full rounded-md">
                                        <div class="grid grid-cols-12 gap-4 items-center">
                                            <div class="col-span-6">
                                                <h6
                                                    class="mb-4 sm:mb-0 leading-none font-medium text-black dark:text-white">
                                                    确认行李
                                                </h6>
                                            </div>
                                            <div class="col-span-6">
                                                <p class="mb-0 opacity-50">23kg</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-span-2 sm:col-span-1">
                                    <div
                                        class="min-h-[48px] bg-[#F2F6FD] dark:bg-[#3E435A] flex flex-col justify-center px-[16px] w-full rounded-md">
                                        <input v-model="num" num type="number" placeholder="0" class=" bg-[#F2F6FD] dark:bg-[#3E435A]" />
                                    </div>
                                </div>
                                <div class="col-span-2 sm:col-span-3">
                                    <button type="reset"
                                        class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥{{ num * 80 }}
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div>
                        <div class="grid grid-cols-12 gap-4 mt-5">
                            <div class="col-span-12">
                                <div class="flex items-center mb-4">
                                    <div class="w-[4px] h-[27px] rounded-md bg-[#0D6EFD]"></div>
                                    <h4 class="text-2xl font-bold mb-0 ml-3">旅行保险</h4>
                                </div>
                            </div>
                            <div class="col-span-12 md:col-span-4">
                                <div @click="checked" 
                                    class="border border-transparent hover:border-blue-600 bg-transparent p-[24px] md:p-0 xl:p-[48px] rounded-md">
                                    <div class="p-[24px] md:p-4 xl:p-[48px]">
                                        <div class="flex items-center justify-center w-full">
                                            <i class="fas fa-heart-broken text-3xl"></i>
                                        </div>
                                        <h4 class="text-2xl font-medium text-center my-6">基础</h4>
                                        <ul class="flex flex-col">
                                            <li class="flex items-center">
                                                <i class="fas fa-times opacity-50 mr-6"></i>
                                                <p class="mb-0 opacity-50">Medical Expense</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Trip Cancellatuon</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Lost Baggage</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Air Travel Insurance</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Libability</p>
                                            </li>
                                        </ul>
                                        <div class="text-center mt-8">
                                            <button type="reset"
                                                class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥0
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="col-span-12 md:col-span-4">
                                <div @click="checked" 
                                    class="border border-transparent hover:border-blue-600 bg-transparent p-[24px] md:p-0 xl:p-[48px] rounded-md">
                                    <div class="p-[24px] md:p-4 xl:p-[48px]">
                                        <div class="flex items-center justify-center w-full">
                                            <i class="fas fa-star text-3xl"></i>
                                        </div>
                                        <h4 class="text-2xl font-medium text-center my-6">高级</h4>
                                        <ul class="flex flex-col">
                                            <li class="flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Medical Expense</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-times opacity-50 mr-6"></i>
                                                <p class="mb-0 opacity-50">Trip Cancellatuon</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Lost Baggage</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Air Travel Insurance</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Libability</p>
                                            </li>
                                        </ul>
                                        <div class="text-center mt-8">
                                            <button type="reset"
                                                class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥50</button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="col-span-12 md:col-span-4">
                                <div @click="checked" 
                                    class="border border-transparent hover:border-blue-600 bg-transparent p-[24px] md:p-0 xl:p-[48px] rounded-md">
                                    <div class="p-[24px] md:p-4 xl:p-[48px]">
                                        <div class="flex items-center justify-center w-full">
                                            <i class="fas fa-briefcase text-3xl"></i>
                                        </div>
                                        <h4 class="text-2xl font-medium text-center my-6">专业</h4>
                                        <ul class="flex flex-col">
                                            <li class="flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Medical Expense</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Trip Cancellatuon</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Lost Baggage</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Air Travel Insurance</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-times opacity-50 mr-6"></i>
                                                <p class="mb-0 opacity-50">Libability</p>
                                            </li>
                                        </ul>
                                        <div class="text-center mt-8">
                                            <button type="reset"
                                                class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥100
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-span-6 sm:col-span-8">
                                <div
                                    class="h-[48px] bg-[#F2F6FD] dark:bg-[#3E435A] flex flex-col justify-center px-[16px] w-full rounded-md">
                                    <div class="grid grid-cols-12 gap-4 items-center">
                                        <div class="col-span-6">
                                            <h6
                                                class="mb-4 sm:mb-0 leading-none font-medium text-black dark:text-white">
                                                确认保险</h6>
                                        </div>
                                        <div class="col-span-6">
                                            
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-span-2 sm:col-span-3">
                                <button type="reset"
                                    class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥{{ insprice }}
                                </button>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="grid grid-cols-12 gap-4 mt-5">
                            <div class="col-span-12">
                                <div class="flex items-center mb-4">
                                    <div class="w-[4px] h-[27px] rounded-md bg-[#0D6EFD]"></div>
                                    <h4 class="text-2xl font-bold mb-0 ml-3">总价</h4>
                                </div>
                            </div>
                            <div class="col-span-6 sm:col-span-8">
                                <div
                                    class="h-[48px] bg-[#F2F6FD] dark:bg-[#3E435A] flex flex-col justify-center px-[16px] w-full rounded-md">
                                    <div class="grid grid-cols-12 gap-4 items-center">
                                        <div class="col-span-6">
                                            <h6
                                                class="mb-4 sm:mb-0 leading-none font-medium text-black dark:text-white">
                                                确认价格
                                            </h6>
                                        </div>
                                        <div class="col-span-6">
                                                <p class="mb-0 opacity-50">￥{{ parseFloat(flight.price) }}(基础机票) + ￥{{ num * 80 }}(行李托运) + ￥{{ insprice }}(保险)</p>
                                        </div>
                                    </div>
                                </div>
                            </div> 

                            <div class="col-span-2 sm:col-span-3">
                                <button type="reset"
                                    class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥{{ parseFloat(flight.price) + (num * 80) + insprice  }}
                                </button>
                            </div>
                        </div>
                    </div>    
                </div>
                <div class="submit">
                    <div @click="submit"
                        class="text-[18px] text-white font-medium py-[12px] px-[30px] bg-blue-600 hover:bg-opacity-90 rounded text-center mt-5 md:mt-0">
                        提交
                    </div>
                </div>
            </form>
        </div>
    </section>
    <section v-if="showModal1" 
    class="modal-overlay1 ezy__eporder1 light py-14 md:py-24 bg-white dark:bg-[#0b1727] text-zinc-900 dark:text-white relative overflow-hidden z-10">
        <div class="container px-4 mx-auto">
            <div class="flex justify-center max-w-md mx-auto">
            <div class="box bg-gray-100 dark:bg-slate-800 rounded-md overflow-hidden">
                <div class="bg-slate-200 dark:bg-slate-700 relative p-6">
                <div @click="showModal1 = false"
                    class="absolute top-4 right-4 w-8 h-8 rounded-full cursor-pointer border border-black dark:border-white flex justify-center items-center">
                    <svg t="1741340923685" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1466" width="32" height="32"><path d="M0 0h1024v1024H0z" fill="#FF0033" fill-opacity="0" p-id="1467"></path><path d="M240.448 168l2.346667 2.154667 289.92 289.941333 279.253333-279.253333a42.666667 42.666667 0 0 1 62.506667 58.026666l-2.133334 2.346667-279.296 279.210667 279.274667 279.253333a42.666667 42.666667 0 0 1-58.005333 62.528l-2.346667-2.176-279.253333-279.253333-289.92 289.962666a42.666667 42.666667 0 0 1-62.506667-58.005333l2.154667-2.346667 289.941333-289.962666-289.92-289.92a42.666667 42.666667 0 0 1 57.984-62.506667z" fill="#111111" p-id="1468"></path></svg>
                </div>
                    <h5 class="text-xl font-bold">交易</h5>
                    <h6 class="font-medium opacity-60">总价：￥{{ formData.price = parseFloat(flight.price) + num * 80 + insprice }}</h6>
                </div>
                <div class="text-center py-12 px-4">
                    <div v-if="isPaid">
                        <div
                        class="relative left-1/2 -translate-x-1/2 w-10 h-10 text-[22px] rounded-full border border-blue-600 text-blue-600 flex justify-center items-center">
                        <svg t="1741443205323" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2973" width="200" height="200"><path d="M512 93.090909c230.4 0 418.909091 188.509091 418.909091 418.909091s-188.509091 418.909091-418.909091 418.909091S93.090909 742.4 93.090909 512 281.6 93.090909 512 93.090909m0-93.090909C228.072727 0 0 228.072727 0 512s228.072727 512 512 512 512-228.072727 512-512S795.927273 0 512 0z" fill="#13cb1f" p-id="2974"></path><path d="M430.545455 716.8c-11.636364 0-23.272727-4.654545-32.581819-13.963636l-151.272727-151.272728c-18.618182-18.618182-18.618182-46.545455 0-65.163636 18.618182-18.618182 46.545455-18.618182 65.163636 0l118.69091 118.690909 281.6-281.6c18.618182-18.618182 46.545455-18.618182 65.163636 0 18.618182 18.618182 18.618182 46.545455 0 65.163636L463.127273 702.836364c-9.309091 9.309091-20.945455 13.963636-32.581818 13.963636z" fill="#13cb1f" p-id="2975"></path></svg>
                        </div>
                        <h1 class="text-2xl font-bold leading-none my-4">
                            支付成功
                        </h1>
                        <p class="text-base opacity-80 px-12">{{ countdown }}秒后自动返回上一个页面</p>
                        <p class="text-base opacity-80 px-12">
                            您已支付成功，前往<router-link to="/mystickets" style="color: blue;">我的行程</router-link>中确认订单？
                        </p>
                        
                    </div>
                    <div v-else>
                        <h1 class="text-2xl font-bold leading-none my-4">
                            请您再次确认支付金额
                        </h1>
                        <p class="text-base opacity-80 px-12">
                           ￥{{ formData.price }}
                        </p>
                        <button @click="pay" class="bg-blue-600 text-white hover:bg-opacity-90 rounded-md px-6 py-3 mt-6 mb-3">支付</button>
                    </div>
                </div>
                <div class="bg-slate-200 dark:bg-slate-700 text-center p-6">
                    <div class="flex items-center justify-center">
                        <i class="fas fa-lock mr-2"></i>
                        <b>请确保当前网络安全</b>
                    </div>
                        <b>有问题? 0123 4567 891</b>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- 模态框 -->
    <div v-if="showModal2" class="modal-overlay2" @click="closeModal">
        <div class="modal" @click.stop>
            <div class="box flex w-full max-w-sm overflow-hidden bg-white rounded-lg shadow-md dark:bg-gray-800">
                <div class="flex items-center justify-center w-12 bg-yellow-400">
                    <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM21.6667 28.3333H18.3334V25H21.6667V28.3333ZM21.6667 21.6666H18.3334V11.6666H21.6667V21.6666Z" />
                    </svg>
                </div>

                <div class="px-4 py-2 -mx-3">
                    <div class="mx-3">
                        <span class="font-semibold text-yellow-400 dark:text-yellow-300">警告</span>
                        <p v-if="alreadyPaid" class="text-sm text-gray-600 dark:text-gray-200" >
                            您已购买该机票，请勿重复购买。
                        </p>
                        <p v-if="isNull">
                            请输入姓名和身份证等重要信息。
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
/* .seat {
    @apply w-10 h-10 flex items-center justify-center border border-gray-300 rounded cursor-pointer;
}

.seat.booked {
    @apply bg-gray-400 text-gray-600 cursor-not-allowed;
}

.seat.selected {
    @apply bg-blue-600 text-white;
}

.aisle {
    @apply col-span-1;
} */

.submit {
    display: flex;
    margin-top: 50px;
    padding-top: 50px;
    width: 100%;
    border-top: 1px solid #878893;
}

.submit div {
    margin: auto;
    width: 25%;
}

.modal-overlay1 {
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

.modal-overlay1 .box {
    width: 100%;
    height: 100%;
}

.modal-overlay2 {
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
.modal-overlay2 .box {
    width: 500px;
    height: 100px;
}
</style>
