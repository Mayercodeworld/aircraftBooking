<script setup>
import {ref, onMounted} from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const num = ref(0);
const showModal = ref(false); 
const selectedInsurance = ref(null);
const insprice = ref(0)
const route = useRoute();
const flight = ref([]);
const flightId = ref(route.params.id);
const loading = ref(true);
function toggleModal() {
    showModal.value = !showModal.value;
}

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
async function searchFlightById() {
    try {
        const response = await axios.get(`http://localhost:8000/back/flights/${flightId.value}`);
        flight.value = response.data;
        // console.log(flight.value.price)
    } catch (error) {
        console.error('Error fetching flight:', error);
    } finally {
        loading.value = false;
    }
}

onMounted(() => {
    searchFlightById();
})
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
                                    <input type="text"
                                        class="min-h-[48px] w-full leading-[36px] bg-transparent border boder-[#BBBFC8] dark:border-[#888993] pl-[24px] focus:outline focus:outline-blue-500 focus:border-none rounded-md opacity-75"
                                        id="lName" placeholder="姓名" />
                                </div>
                            </div>
                            <div class="col-span-12 md:col-span-6 lg:col-span-2">
                                <label class="text-[18px] opacity-80 mb-0 font-medium" for="bDate">出生日期</label>
                                <div class="mt-4 md:mt-3 mb-4">
                                    <input type="text"
                                        class="min-h-[48px] w-full leading-[36px] bg-transparent border boder-[#BBBFC8] dark:border-[#888993] pl-[24px] focus:outline focus:outline-blue-500 focus:border-none rounded-md opacity-75"
                                        id="bDate" placeholder="年/月/日" />
                                </div>
                            </div>
                            <div class="col-span-12 md:col-span-6 lg:col-span-2">
                                <label class="font-medium mb-0">性别</label>
                                <select
                                    class="min-h-[48px] leading-[36px] border border-[#BBBFC8] dark:border-[#888993] dark:bg-[#2E2F41] text-gray-400 px-4 w-full focus:outline focus:outline-blue-500 focus:border-none mt-3 mb-4 rounded-md"
                                    aria-label="Default select example">
                                    <option value="0" selected>男</option>
                                    <option value="1">女</option>
                                </select>
                            </div>
                        </div>

                        <div class="grid grid-cols-12 gap-4">
                            <!-- country -->
                            <div class="col-span-12 md:col-span-6 lg:col-span-4">
                                <label class="font-medium mb-0">国籍</label>
                                <select
                                    class="min-h-[48px] leading-[36px] border border-[#BBBFC8] dark:border-[#888993] dark:bg-[#2E2F41] text-gray-400 px-4 w-full focus:outline focus:outline-blue-500 focus:border-none mt-3 mb-4 rounded-md"
                                    aria-label="Default select example">
                                    <option value="0" selected>中国</option>
                                    <option value="1">美国</option>
                                    <option value="2">法国</option>
                                    <option value="3">英国</option>

                                </select>
                            </div>
                            <!-- passport no -->
                            <div class="col-span-12 md:col-span-6 lg:col-span-4">
                                <label class="text-[18px] opacity-80 mb-0 font-medium" for="passport">身份证/护照</label>
                                <div class="mt-4 md:mt-3 mb-4">
                                    <input type="password"
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
                                    <div class="col-span-6 sm:col-span-2 md:col-span-1">
                                        <div
                                            class="w-10 h-10 rounded-full flex justify-center items-center text-[22px] cursor-pointer opacity-30 bg-[#4c4d5a] hover:opacity-75">
                                            <i class="fas fa-times"></i>
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
                                    <div class="col-span-6 sm:col-span-2 md:col-span-1">
                                        <div
                                            class="w-10 h-10 rounded-full flex justify-center items-center text-[22px] cursor-pointer opacity-30 bg-[#4c4d5a] hover:opacity-75">
                                            <i class="fas fa-times"></i>
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
                                                    确认行李</h6>
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
                                                    请选择保险</h6>
                                            </div>
                                            <div class="col-span-6">
                                                
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-span-2 sm:col-span-1">
                                    <div
                                        class="min-h-[48px] bg-[#F2F6FD] dark:bg-[#3E435A] flex flex-col justify-center px-[16px] w-full rounded-md">
                                        <input type="text" class=" bg-[#F2F6FD] dark:bg-[#3E435A]" />
                                    </div>
                                </div>
                                <div class="col-span-2 sm:col-span-3">
                                    <button type="reset"
                                        class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥{{ insprice }}
                                    </button>
                                </div>
                            </div>
                    </div>
                </div>
            </form>
            <div class="grid grid-cols-12 gap-2 md:gap-4 mt-10">
                <div class="col-span-12">
                    <div class="flex items-center">
                        <button type="reset"
                            class="text-[18px] text-white font-medium py-[12px] px-[30px] bg-blue-600 hover:bg-opacity-90 rounded text-center mt-5 md:mt-0">￥{{ parseFloat(flight.price) + (num * 80) + insprice }}
                        </button>
  
                        <button type="submit" @click="toggleModal"
                            class="text-[18px] text-white font-medium py-[12px] px-[30px] bg-blue-600 hover:bg-opacity-90 rounded text-center mt-5 md:mt-0">
                            提交
                        </button>
                        
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section v-if="showModal"
    class="modal-overlay ezy__eporder1 light py-14 md:py-24 bg-white dark:bg-[#0b1727] text-zinc-900 dark:text-white relative overflow-hidden z-10"
    >
        <div class="container px-4 mx-auto">
            <div class="flex justify-center max-w-md mx-auto">
            <div class="bg-gray-100 dark:bg-slate-800 rounded-md overflow-hidden">
                <div class="bg-slate-200 dark:bg-slate-700 relative p-6">
                <div @click="toggleModal"
                    class="absolute top-4 right-4 w-8 h-8 rounded-full cursor-pointer border border-black dark:border-white flex justify-center items-center"
                >
                    <svg t="1741340923685" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1466" width="32" height="32"><path d="M0 0h1024v1024H0z" fill="#FF0033" fill-opacity="0" p-id="1467"></path><path d="M240.448 168l2.346667 2.154667 289.92 289.941333 279.253333-279.253333a42.666667 42.666667 0 0 1 62.506667 58.026666l-2.133334 2.346667-279.296 279.210667 279.274667 279.253333a42.666667 42.666667 0 0 1-58.005333 62.528l-2.346667-2.176-279.253333-279.253333-289.92 289.962666a42.666667 42.666667 0 0 1-62.506667-58.005333l2.154667-2.346667 289.941333-289.962666-289.92-289.92a42.666667 42.666667 0 0 1 57.984-62.506667z" fill="#111111" p-id="1468"></path></svg>
                </div>
                <h5 class="text-xl font-bold">交易</h5>
                <h6 class="font-medium opacity-60">总价：￥{{ parseFloat(flight.price) + num * 80 + insprice }}</h6>
                </div>
                <div class="text-center py-12 px-4">
                    <div
                        class="relative left-1/2 -translate-x-1/2 w-10 h-10 text-[22px] rounded-full border border-blue-600 text-blue-600 flex justify-center items-center"
                    >
                        <i class="fas fa-check"></i>
                    </div>
                    <h1 class="text-2xl font-bold leading-none my-4">
                        Your Certificate Order is Successful
                    </h1>
                    <p class="text-base opacity-80 px-12">
                        In purus donec ac in nulla lobortis. Lectus massa erat odio
                        turpis nulla sed.
                    </p>
                    <button
                        class="bg-blue-600 text-white hover:bg-opacity-90 rounded-md px-6 py-3 mt-6 mb-3"
                    >
                    支付
                    </button>
                </div>
                <div class="bg-slate-200 dark:bg-slate-700 text-center p-6">
                <div class="flex items-center justify-center">
                    <i class="fas fa-lock mr-2"></i>
                    <b>确保当前网络安全</b>
                </div>
                <b>有问题? 0123 4567 891</b>
                </div>
            </div>
            </div>
        </div>
    </section>

</template>
<style scoped>
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
