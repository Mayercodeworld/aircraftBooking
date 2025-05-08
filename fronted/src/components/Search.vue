<script setup>
import { ref } from 'vue';
import { formData } from '@/stores/formdata';
import { cities } from '@/stores/cities';
import { useRouter } from 'vue-router';
const router = useRouter(); 
const showModal = ref(false); 
const activeCityPicker = ref(null);
const activeTab = ref('热门');
const proData = ref('其他错误')

// 接收父组件传递的 searchFlights 方法
const props = defineProps({
    searchFlights: {
        type: Function,
        required: false
    }
});
const searchFlights = () => {
    if (!formData.from) {
        showModal.value = true; 
        proData.value = '请选择或者输入出发地'
        document.body.style.overflow = 'hidden';
        return;
    } 
    if (!formData.to) {
        showModal.value = true; 
        proData.value = '请选择或者输入目的地';
        return;
    } 
    if (!formData.depart) {
        showModal.value = true; 
        proData.value = '请选择或者输入出发时间';
        return;
    }
    if (formData.from == formData.to) {
        showModal.value = true;
        proData.value = '出发地与目的地不能相同';
        return;
    }
    console.log(formData.depart)
    // 检查当前路由是否为 /ticket
    if (router.currentRoute.value.path === '/ticket') {
        if (props.searchFlights) {
            props.searchFlights();
        }
    } else {
        router.push('/ticket');
    }
    
    showModal.value = false; 
    document.body.style.overflow = 'auto';
};

const closeModal = () => {
    showModal.value = false;
    document.body.style.overflow = 'auto'; 
};

// 显示城市选择器
const showCityPicker = (type) => {
    activeCityPicker.value = type;
};

// 切换标签页
const switchTab = (tab) => {
    activeTab.value = tab;
};

// 选择城市
const selectCity = (city, type) => {
    if (type === 'from') {
        formData.from = city.name;
    } else if (type === 'to') {
        formData.to = city.name;
    }
    activeCityPicker.value = null;
};
</script>

<template>
    <!-- search bar -->
    <div class="grid grid-cols-12 mt-10 bg-white text-black px-4 rounded-md">
        <div class="col-span-12">
            <div class="p-[24px]">
                <form class="grid grid-cols-2 gap-4 md:grid-cols-7" @submit.prevent="searchFlights">
                    <!-- from -->
                    <div class="col-span-1 flex justify-center items-center relative">
                        <input v-model="formData.from" type="text"
                            class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                            placeholder="出发地" @click="showCityPicker('from')"  />
                        <!-- 城市选择弹窗 -->
                        <transition name="slide-fade">
                            <div v-if="activeCityPicker === 'from'" class="city-picker-wrapper absolute min-w-xl max-h-60 font-light text-sm top-full left-0 w-full bg-white border border-gray-300 shadow-md rounded-md">
                                <ul class="city-picker-tabs">
                                    <li :class="{ 'active': activeTab === '热门' }" @click="switchTab('热门')">热门</li>
                                    <li :class="{ 'active': activeTab === 'ABCDEF' }" @click="switchTab('ABCDEF')">ABCDEF</li>
                                    <li :class="{ 'active': activeTab === 'GHIJ' }" @click="switchTab('GHIJ')">GHIJ</li>
                                    <li :class="{ 'active': activeTab === 'KLMN' }" @click="switchTab('KLMN')">KLMN</li>
                                    <li :class="{ 'active': activeTab === 'PQRSTUVW' }" @click="switchTab('PQRSTUVW')">PQRSTUVW</li>
                                    <li :class="{ 'active': activeTab === 'XYZ' }" @click="switchTab('XYZ')">XYZ</li>
                                </ul>
                                <div v-if="activeTab === '热门'" class="city-picker-body">
                                    <ul class="cities">
                                        <li v-for="city in cities.hot" :key="city.code" @click="selectCity(city, 'from')">{{ city.name }}</li>
                                    </ul>
                                </div>
                                <div v-if="activeTab === 'ABCDEF'" class="city-picker-body">
                                    <div v-for="group in cities.ABCDEF" :key="group.character" class="domestic-city-item">
                                        <div class="city-character">{{ group.character }}</div>
                                        <ul class="cities domestic-city-content">
                                            <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'from')">{{ city.name }}</li>
                                        </ul>
                                    </div>
                                </div>
                                <div v-if="activeTab === 'GHIJ'" class="city-picker-body">
                                    <div v-for="group in cities.GHIJ" :key="group.character" class="domestic-city-item">
                                        <div class="city-character">{{ group.character }}</div>
                                        <ul class="cities domestic-city-content">
                                            <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'from')">{{ city.name }}</li>
                                        </ul>
                                    </div>
                                </div>
                                <div v-if="activeTab === 'KLMN'" class="city-picker-body">
                                    <div v-for="group in cities.KLMN" :key="group.character" class="domestic-city-item">
                                        <div class="city-character">{{ group.character }}</div>
                                        <ul class="cities domestic-city-content">
                                            <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'from')">{{ city.name }}</li>
                                        </ul>
                                    </div>
                                </div>
                                <div v-if="activeTab === 'PQRSTUVW'" class="city-picker-body">
                                    <div v-for="group in cities.PQRSTUVW" :key="group.character" class="domestic-city-item">
                                        <div class="city-character">{{ group.character }}</div>
                                        <ul class="cities domestic-city-content">
                                            <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'from')">{{ city.name }}</li>
                                        </ul>
                                    </div>
                                </div>
                                <div v-if="activeTab === 'XYZ'" class="city-picker-body">
                                    <div v-for="group in cities.XYZ" :key="group.character" class="domestic-city-item">
                                        <div class="city-character">{{ group.character }}</div>
                                        <ul class="cities domestic-city-content">
                                            <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'from')">{{ city.name }}</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </transition>   
                    </div>
                    <!-- to -->
                    <div class="col-span-1 relative">
                        <input v-model="formData.to" type="text"
                            class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                            placeholder="目的地" @click="showCityPicker('to')" />
                            <!-- 城市选择弹窗 -->
                            <transition name="slide-fade">
                                <div v-if="activeCityPicker === 'to'" class="city-picker-wrapper absolute min-w-xl max-h-60 font-light text-sm top-full left-0 w-full bg-white border border-gray-300 shadow-md rounded-md">
                                    <ul class="city-picker-tabs">
                                        <li :class="{ 'active': activeTab === '热门' }" @click="switchTab('热门')">热门</li>
                                        <li :class="{ 'active': activeTab === 'ABCDEF' }" @click="switchTab('ABCDEF')">ABCDEF</li>
                                        <li :class="{ 'active': activeTab === 'GHIJ' }" @click="switchTab('GHIJ')">GHIJ</li>
                                        <li :class="{ 'active': activeTab === 'KLMN' }" @click="switchTab('KLMN')">KLMN</li>
                                        <li :class="{ 'active': activeTab === 'PQRSTUVW' }" @click="switchTab('PQRSTUVW')">PQRSTUVW</li>
                                        <li :class="{ 'active': activeTab === 'XYZ' }" @click="switchTab('XYZ')">XYZ</li>
                                    </ul>
                                    <div v-if="activeTab === '热门'" class="city-picker-body">
                                        <ul class="cities">
                                            <li v-for="city in cities.hot" :key="city.code" @click="selectCity(city, 'to')">{{ city.name }}</li>
                                        </ul>
                                    </div>
                                    <div v-if="activeTab === 'ABCDEF'" class="city-picker-body">
                                        <div v-for="group in cities.ABCDEF" :key="group.character" class="domestic-city-item">
                                            <div class="city-character">{{ group.character }}</div>
                                            <ul class="cities domestic-city-content">
                                                <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'to')">{{ city.name }}</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div v-if="activeTab === 'GHIJ'" class="city-picker-body">
                                        <div v-for="group in cities.GHIJ" :key="group.character" class="domestic-city-item">
                                            <div class="city-character">{{ group.character }}</div>
                                            <ul class="cities domestic-city-content">
                                                <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'to')">{{ city.name }}</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div v-if="activeTab === 'KLMN'" class="city-picker-body">
                                        <div v-for="group in cities.KLMN" :key="group.character" class="domestic-city-item">
                                            <div class="city-character">{{ group.character }}</div>
                                            <ul class="cities domestic-city-content">
                                                <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'to')">{{ city.name }}</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div v-if="activeTab === 'PQRSTUVW'" class="city-picker-body">
                                        <div v-for="group in cities.PQRSTUVW" :key="group.character" class="domestic-city-item">
                                            <div class="city-character">{{ group.character }}</div>
                                            <ul class="cities domestic-city-content">
                                                <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'to')">{{ city.name }}</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div v-if="activeTab === 'XYZ'" class="city-picker-body">
                                        <div v-for="group in cities.XYZ" :key="group.character" class="domestic-city-item">
                                            <div class="city-character">{{ group.character }}</div>
                                            <ul class="cities domestic-city-content">
                                                <li v-for="city in group.cities" :key="city.code" @click="selectCity(city, 'to')">{{ city.name }}</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <!-- 其他字母分组类似 -->
                                </div>
                            </transition>
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
                            <!-- <option>转机</option> -->
                        </select>
                    </div>
                    <!-- passengers -->
                    <div class="col-span-1">
                        <select v-model="formData.passengers"
                            class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                            placeholder="人数">
                            <option selected>1人</option>
                            <!-- <option>2人</option>
                            <option>3人</option> -->
                        </select>
                    </div
                    <!-- type -->
                    <div class="col-span-1">
                        <select v-model="formData.type"
                            class="h-[48px] w-full leading-[36px] border border-[#eaeaea] bg-transparent text-[#3b3b3b] rounded-md  placeholder:text-black py-[6px] px-[12px] focus:border-none focus:outline-blue-500"
                            placeholder="航班类型">
                            <option selected>经济</option>
                            <!-- <option>商务</option> -->
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


    <!-- 模态框 -->
    <div v-if="showModal" class="modal-overlay" @click="closeModal">
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
                        <p class="text-sm text-gray-600 dark:text-gray-200">
                            {{ proData }}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
/* .searchbox {
 margin-top: 20px;
} */

a.search-btn {
    text-align: center;
    line-height: 40px;
    display: block;
}

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

.modal-overlay .box {
    width: 400px;
    height: 85px;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
    transition: all 0.4s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
    transform: translateX(-80px);
    opacity: 0;
}

.city-picker-wrapper {
    z-index: 15;
}

.city-picker-tabs {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0;
    border-bottom: 1px solid #ccc;
}

.city-picker-tabs li {
    padding: 10px 20px;
    cursor: pointer;
    border-bottom: 2px solid transparent;
}

.city-picker-tabs li.active {
    border-bottom: 2px solid #007bff;
    color: #007bff;
}

.city-picker-body {
    padding: 0px 20px;
    max-height: 200px;
    overflow-y: auto;
}

.city-picker-body .city-character{
    margin-top: 5px;
    width: 10px;
}

.city-picker-body ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.city-picker-body ul li {
    display: inline-block;
    padding: 7px;
    cursor: pointer;
}

.city-picker-body ul li:hover {
    background-color: #f0f0f0;
}
</style>