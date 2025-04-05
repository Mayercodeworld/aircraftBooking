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

const cancel_order = (order_id) => {
  axios.post(`http://127.0.0.1:8000/api/order/${order_id}/cancel/`).then(res => {
    console.log(res.data.message);
    // 更新订单状态
    orders.value = orders.value.map(order => 
      order.order_id === order_id ? { ...order, status: '已取消' } : order
    );
  }).catch(error => {
    console.error("There was an error canceling the order!", error);
  });
}

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  return `${year}-${month}-${day} ${hours}:${minutes}`;
}
</script>

<template>
  <section
    class="ezy__eporder8 light py-14 md:py-24 bg-white dark:bg-[#0b1727] text-zinc-900 dark:text-white relative overflow-hidden z-10"
  >
    <div class="container px-4 mx-auto">
      <div class="box1 flex justify-center  mx-auto">
        <div class="box2 bg-gray-100 dark:bg-slate-800 p-4 sm:p-8 lg:p-12 w-full">
          <table class="table-fixed text-center w-full">
            <thead class="mb-6">
            <tr class="text-lg sm:text-[22px] font-bold py-5">
              <th>航班号</th>
              <th>出发日期</th>
              <th>价格</th>
              <th>状态</th>
              <th>退订</th>
              <th>出发地</th>
              <th>目的地</th>
              <th>座位号</th>
              <th>乘客</th>
              <!-- <th>删除</th> -->
            </tr>
            </thead>
            <tbody class="sm:text-lg font-medium align-baseline">
            <tr v-for="order in orders" :key="order.order_id">
              <td class="py-5">{{ order.flight.flight_no }}</td>
              <td class="py-5">{{ formatDate(order.flight.departure_time) }}</td>
              <td class="py-5">￥{{ order.price }}</td>
              <td class="flex justify-center py-5">
                  <span
                    class="w-full max-w-[150px] py-2 px-2.5 text-white rounded-md font-medium text-base"
                    :class="{
                      'bg-blue-600': order.status === '已结束',
                      'bg-red-600': order.status === '已取消',
                      'bg-green-600': order.status === '等待出行',
                      'bg-green-700': order.status === '进行中'
                    }">
                    {{ order.status }}
                  </span>
              </td>
              <td class="py-5">
                <span 
                  class="bg-red-600 text-white hover:bg-opacity-90 rounded-md px-5 py-2 cursor-pointer"
                  @click="cancel_order(order.order_id)"
                >
                  退订
                </span>
              </td>
              <td class="py-5">
                {{ order.flight.departure_city }}
              </td>
              <td>
                {{ order.flight.arrival_city }}
              </td>
              <td>
                {{ order.seat.seat_number }}
              </td>
              <td>
                {{ order.name}}
              </td>
              <!-- <td>
                <span 
                  class="bg-red-600 text-white hover:bg-opacity-90 rounded-md px-5 py-2 cursor-pointer"
                  @click="cancel_order(order.order_id)">
                  删除
                </span>
              </td> -->
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.container {
  width: 100%;
}

.container .box1 {
  display: block;
  width: 90%;
}

</style>
