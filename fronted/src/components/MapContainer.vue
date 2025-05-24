<script setup>
import { onMounted, onUnmounted } from "vue";
import AMapLoader from "@amap/amap-jsapi-loader";
window._AMapSecurityConfig = {
  securityJsCode: '9c6c83d08507f32bad97c7d2a80c49a1',//你的秘钥
}
let map = null;

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

      // const hawkEye = new AMap.HawkEye();
      // map.addControl(hawkEye);

      const placeSearch = new AMap.PlaceSearch({
        pageSize: 5,
        pageIndex: 1,
        city: "北京", //城市，默认：“全国”
        map: map,
        panel: "my-panel",
        autoFitView: true,
      });
      placeSearch.search("景点");

    })
    .catch((e) => {
      console.log(e);
    });
});

onUnmounted(() => {
  map?.destroy();
});
</script>

<template>
  <link rel="stylesheet" href="https://webapi.amap.com/styles/api-v2.css" />
  <div class="map-container">
    <div id="container"></div>
    <div id="my-panel" style="margin-top: 20px;"></div>
  </div>
</template>

<style scoped>
.map-container {
  display: flex;
  /* position: relative; */
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
  height: 450px;
  box-shadow: 4px 12px 22px 0px rgba(100, 100, 111, 0.35);
}
.amap_lib_placeSearch {
  border-radius: 10px;
  width: 50px;
}
</style>
