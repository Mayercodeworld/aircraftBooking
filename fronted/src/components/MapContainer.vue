<script setup>
import { onMounted, onUnmounted ,ref} from "vue";
import AMapLoader from "@amap/amap-jsapi-loader";
window._AMapSecurityConfig = {
  securityJsCode: '9c6c83d08507f32bad97c7d2a80c49a1',//你的秘钥
}
let map = null;
let placeSearchInstance = null;
const props = defineProps({
    place: {
        type: String,
        required: false
    }
});
const display = ref(false);

onMounted(() => {
  AMapLoader.load({
    key: "60ad4b680019f571a2cffd7df843d67e", // 申请好的Web端开发者Key，首次调用 load 时必填
    version: "2.0", // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
    plugins: ["AMap.ToolBar", "AMap.Scale", 'AMap.HawkEye', 'AMap.PlaceSearch'], // 需要使用的的插件列表，如比例尺'AMap.Scale'等
  })
    .then((AMap) => {
      map = new AMap.Map("container", {
        viewMode: "2D",
        zoom: 11,
        center: [116.397428, 39.90923],
      });

      // const toolBar = new AMap.ToolBar();
      // map.addControl(toolBar);

      const scale = new AMap.Scale();
      map.addControl(scale);


      // 初始化 PlaceSearch 插件
      placeSearchInstance = new AMap.PlaceSearch({
        pageSize: 4,
        pageIndex: 1,
        city: props.place,
        map: map,
        panel: "my-panel",
        autoFitView: true,
      });
      console.log(props.place)
      // 页面加载时即执行搜索
      placeSearchInstance.search("景点");
    })
    .catch((e) => {
      console.log(e);
    });
});

onUnmounted(() => {
  map?.destroy();
});

function handleButtonClick() {
  display.value = !display.value;
}

</script>

<template>
  <link rel="stylesheet" href="https://webapi.amap.com/styles/api-v2.css" />
  <div class="map-container">
    <div id="container"></div>
    <!-- v-if 是条件渲染指令，它会销毁并重建 DOM 元素 -->
    <div v-show = "display" id="my-panel"></div>
    <button class="circle-button" @click="handleButtonClick">
      <svg t="1748267652481" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2854" width="32" height="32"><path d="M1009.19461 5.118447a32.054274 32.054274 0 0 0-35.125341 0.255922l-959.708789 639.805859a31.830341 31.830341 0 0 0-14.043738 29.942914 31.830341 31.830341 0 0 0 19.929952 26.360002l250.292052 100.161607 117.692288 205.953506a31.990293 31.990293 0 0 0 27.415681 16.123108H415.998608c11.228593 0 21.657428-5.950194 27.415681-15.547283l66.443839-110.782384 310.14589 124.026365a31.734371 31.734371 0 0 0 27.543642-1.855437c8.445437-4.734563 14.23568-13.05204 15.867185-22.617137l159.951465-959.708788A32.054274 32.054274 0 0 0 1009.19461 5.118447zM100.446359 664.662317L841.821398 170.3803 302.784962 747.389214c-2.847136-1.695486-5.374369-3.934806-8.509418-5.182427l-193.829185-77.54447z m225.627536 105.216073l-0.223932-0.319903L931.842082 120.955298 415.230841 925.895049l-89.156946-156.016659z m480.750122 177.322194l-273.229092-109.278841a63.564712 63.564712 0 0 0-19.929952-3.806845L934.401305 181.896806l-127.577288 765.303778z" fill="#333333" p-id="2855"></path></svg>
    </button>
  </div>
</template>

<style scoped>
.map-container {
  display: flex;
  position: relative;
  width: 47%;
  height: 450px;
}

#container {
  width: 100%;
  height: 450px;
  border-radius: 10px;
  box-shadow: 4px 12px 22px 0px rgba(100, 100, 111, 0.35);
}

#my-panel {
  position: absolute;
  /* right: 0; */
  width: 100px;
  top: 0;
  box-shadow: 4px 12px 22px 0px rgba(100, 100, 111, 0.35);
}


/* 圆形按钮样式 */
.circle-button {
  position: absolute;
  right: 5px;
  bottom: 5px;
  width: 50px; 
  height: 50px; 
  border-radius: 50%; 
  background-color: #fff;
  border: 2px solid #ccc; 
  padding-left: 4px; 
  overflow: hidden; 
  cursor: pointer; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  z-index: 100; 
}

/* 图片样式 */
.button-icon {
  width: 100%; 
  height: 100%;
  object-fit: cover; 
}
</style>
