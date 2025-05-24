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
      <img src="" alt="按钮图标" class="button-icon" />
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
  position: absolute; /* 绝对定位，可以根据需要调整位置 */
  right: 5px;
  bottom: 5px;
  width: 50px; /* 按钮宽度 */
  height: 50px; /* 按钮高度 */
  border-radius: 50%; /* 圆形效果 */
  background-color: #fff; /* 背景颜色，可以自定义 */
  border: 2px solid #ccc; /* 边框 */
  padding: 0; /* 去除默认内边距 */
  overflow: hidden; /* 隐藏超出范围的内容 */
  cursor: pointer; /* 鼠标悬停时显示为手型 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 添加阴影效果 */
  z-index: 999; /* 确保按钮在地图之上 */
}

/* 图片样式 */
.button-icon {
  width: 100%; /* 让图片填满按钮区域 */
  height: 100%;
  object-fit: cover; /* 图片按比例覆盖整个按钮区域 */
}
</style>
