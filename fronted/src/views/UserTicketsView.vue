<script setup>
import { ref, onMounted } from "vue";
import Cookies from 'js-cookie';
import axios from "axios";

// 定义一个响应式变量来存储订单数据
const orders = ref([]);

onMounted(() => {
  // 切换界面之后，初始显示顶部
  window.scrollTo({
    top: 0,
  });
  get_user_tickets();
});

const get_user_tickets = () => {
  const user_id = Cookies.get('user_id');
  if (user_id) {
    axios.get(`http://127.0.0.1:8000/api/user/${user_id}/tickets/`).then(res => {
      console.log(res.data);
      // 将返回的数据赋值给 orders 变量
      orders.value = res.data;
    }).catch(error => {
      console.error("There was an error fetching the user tickets!", error);
    });
  }
}
</script>

<template>
  <section
    class="ezy__eporder8 light py-14 md:py-24 bg-white dark:bg-[#0b1727] text-zinc-900 dark:text-white relative overflow-hidden z-10"
  >
    <div class="container px-4 mx-auto">
      <div class="flex justify-center max-w-5xl mx-auto">
        <div class="bg-gray-100 dark:bg-slate-800 p-4 sm:p-8 lg:p-12 w-full">
          <table class="table-fixed text-center w-full">
            <thead class="mb-6">
            <tr class="text-lg sm:text-[22px] font-bold py-5">
              <th class="text-start">Order Id</th>
              <th>Date</th>
              <th>Price</th>
              <th>Status</th>
            </tr>
            </thead>
            <tbody class="sm:text-lg font-medium align-baseline">
            <tr v-for="order in orders" :key="order.order_id">
              <td class="text-start py-5">{{ order.order_id }}</td>
              <td class="py-5">{{ order.date }}</td>
              <td class="py-5">${{ order.price }}</td>
              <td class="flex justify-center py-5">
                  <span
                    class="w-full max-w-[150px] py-2 px-2.5 rounded-md font-medium text-base text-white"
                    :class="{
                      'bg-blue-600 bg-opacity-10': order.status === 'Completed',
                      'bg-red-600 bg-opacity-10': order.status === 'Failed',
                      'bg-green-600 bg-opacity-10': order.status === 'In Progress'
                    }"
                  >
                    {{ order.status }}
                  </span>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
</style>
