<template>
    <div id="main" ref="chartDom" style="width: 100%; height: 450px;"></div>
</template>

<script setup>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { ref, onMounted, onBeforeUnmount } from 'vue';
import * as echarts from 'echarts/core';
import { TooltipComponent, GeoComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import flightSeatsSvg from '@/assets/flight-seats.svg?raw';

echarts.use([TooltipComponent, GeoComponent, CanvasRenderer]);

const route = useRoute();
const flightId = ref(route.params.id);
const emit = defineEmits(['select-seat'])
const takenSeats = ref([])

const chartDom = ref(null);
let myChart = null;

async function fetchSeats() {
  try {
    const response = await axios.get(`http://localhost:8000/api/flights/${flightId.value}/seats/`)
    takenSeats.value = response.data.filter(seat => seat.status === 'booked').map(seat => seat.seat_number)
    // console.log("takenSeats: ", takenSeats.value);
  } catch (error) {
    console.error('Error fetching seats:', error.response.data)
  }
}
// console.log("takenSeats: ", takenSeats.value)
function makeTakenRegions(takenSeatNames) {
  // console.log("takenSeatNames: ", takenSeatNames);
  let a = takenSeatNames.map(name => ({
    name,
    silent: true,
    itemStyle: { color: '#bf0e08' },
    emphasis: { itemStyle: { borderColor: '#aaa', borderWidth: 1 } },
    select: { itemStyle: { color: '#bf0e08' } }
  }));
  // console.log('a: ', a);
  return a;
}

function initChart(svg) {
  echarts.registerMap('flight-seats', { svg: svg });

  const option = {
    tooltip: {},
    geo: {
      map: 'flight-seats',
      roam: true,
      selectedMode: 'single',
      layoutCenter: ['50%', '50%'],
      layoutSize: '280%',
      itemStyle: { color: '#fff' },
      emphasis: {
        itemStyle: { color: undefined, borderColor: 'green', borderWidth: 2 },
        label: { show: false }
      },
      select: {
        itemStyle: { color: 'green' },
        label: { show: false }
      },
      regions: makeTakenRegions(takenSeats.value)
    }
  };

  myChart = echarts.init(chartDom.value);
  myChart.setOption(option);
  // 用户在地图上点击一个区域（即一个座位）时，会触发此回调函数
  myChart.on('geoselectchanged', function (params) {
    if (params.allSelected && params.allSelected.length > 0) {
      const selectedName = params.allSelected[0].name[0];

      if (selectedName && !takenSeats.value.includes(selectedName)) {
        console.log('Selected seat:', selectedName);
        emit('select-seat', selectedName);
      }
    }
  });
}

onMounted(async () => {
  try {
    await fetchSeats();
    initChart(flightSeatsSvg);
  } catch (err) {
    console.error('Initialization failed:', err);
  }
});

onBeforeUnmount(() => {
  if (myChart) {
    myChart.dispose();
    myChart = null;
  }
});
</script>