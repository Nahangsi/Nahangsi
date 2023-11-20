<template>

    <p>hi</p>
    <div id="map" style="width:500px;height:400px;"></div>
    
    </template>
    
    
    <script setup>
    
    import { onMounted } from 'vue';
    
    let map = null
    
    onMounted(() => {
      if (window.kakao && window.kakao.maps) {
        initMap();
      } else {
        const script = document.createElement('script');
        /* global kakao */
        script.onload = () => kakao.maps.load(initMap);
        script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey={당신의api키입력하시오}`;
        document.head.appendChild(script);
      }
    });
    
    const initMap = () => {
      const container = document.getElementById('map');
      const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 5,
      };
    
      // 지도 객체를 등록합니다.
      // 지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
      map = new kakao.maps.Map(container, options);
    
    }
    
    
  
    </script>
    
  
    
    
    <style scoped>
    
    
    </style>