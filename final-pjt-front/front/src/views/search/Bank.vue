<template>
    <v-app>
      <v-container>
        <v-form>
          <v-row>
              <v-select
                v-model="selectPro"
                :items="store.mainList"
                label="시 / 도"
                @change="selectedProvince"
                color="teal-darken-2"
              ></v-select>
              <v-select
                v-model="selectCity"
                :items="store.subList[selectPro]"
                label="시 / 군 / 구"
                @change="selectedCity"
              ></v-select>
              <v-select
                v-model="selectB"
                :items="store.bankList"
                label="은행"
                @change="selectedBank"
              ></v-select>
            </v-row>
            <!-- 찾기 버튼 -->
            <v-btn class="button" @click="searchNow" color="teal-darken-2">찾기</v-btn>
  
        </v-form>
  
        <div class="map" id="map" style="width: 100%; height: 90vh"></div>
  
        <v-divider class="my-4"></v-divider>
  
      </v-container>
    </v-app>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { useLocationStore } from "@/stores/location";
  
  const store = useLocationStore();
  
  const selectPro = ref("");
  const selectCity = ref("");
  const selectB = ref("");
  
  const map = ref(null);
  const bankMarkers = ref([]);
  let currentInfowindow = null;
  
  const selectedProvince = (event) => {
    selectPro.value = event.target.value;
  };
  const selectedCity = (event) => {
    selectCity.value = event.target.value;
  };
  const selectedBank = (event) => {
    selectB.value = event.target.value;
  };
  
  const loadMap = async () => {
    if (!window.kakao || !window.kakao.maps) {
      console.error("Kakao Maps API is not loaded.");
      return;
    }
  
    const mapContainer = document.getElementById("map");
    const mapOption = {
      center: new kakao.maps.LatLng(36.107071, 128.419289),
      level: 7,
    };
  
    map.value = new kakao.maps.Map(mapContainer, mapOption);
  };
  
  const placesSearchCB = async (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
      clearMarkers();
  
      const bounds = new kakao.maps.LatLngBounds();
  
      for (let i = 0; i < data.length; i++) {
        displayMarker(data[i]);
        bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
      }
  
      map.value.setBounds(bounds);
      updateBankList(data);
    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
      console.warn("검색 결과가 없어요 !!");
    } else {
      console.error(`검색 실패 : ${status}`);
    }
  };
  
  function updateBankList(data) {
    for (const marker of data) {
      bankMarkers.value.push({
        marker: null,
        place_name: marker.place_name,
      });
  
      console.log("은행: ", marker.place_name);
    }
  }
  
  const searchResultText = ref("");
  
  const searchNow = () => {
    const ps = new kakao.maps.services.Places(map.value);
    const keyword = `${selectPro.value} ${selectCity.value} ${selectB.value}`;
  
    clearMarkers();
  
    ps.keywordSearch(
      keyword,
      (data, status, pagination) => {
        if (status === kakao.maps.services.Status.OK) {
          searchResultText.value = "";
        } else {
          searchResultText.value = "검색 목록이 없습니다.";
        }
  
        placesSearchCB(data, status, pagination);
      },
      {
        useMapBounds: false,
      }
    );
  };
  
  const clearMarkers = () => {
    for (const marker of bankMarkers.value) {
      if (marker.marker) {
        marker.marker.setMap(null);
      }
    }
    bankMarkers.value = [];
  };
  
  function displayMarker(place) {
    const marker = new kakao.maps.Marker({
      map: map.value,
      position: new kakao.maps.LatLng(place.y, place.x),
    });
  
    bankMarkers.value.push({
      marker: marker,
      place_name: place.place_name,
    });
  
    kakao.maps.event.addListener(marker, "click", function () {
      if (currentInfowindow) {
        currentInfowindow.close();
      }
  
      const infowindow = new kakao.maps.InfoWindow({
        zIndex: 1,
        content: `<div style="padding:5px;font-size:12px;">${place.place_name}</div>`,
      });
  
      infowindow.open(map.value, marker);
      currentInfowindow = infowindow;
    });
  };
  
  onMounted(loadMap);
  </script>
  
  <style scoped>
  /* 추가적인 스타일링 여기에 추가 */
  .map-container {
    width: 100%;
    position: relative; /* position 추가 */
    z-index: 2; /* 지도를 덮는 검은색 배경을 지도 아래로 내리기 위한 z-index 값 */
  }
  .button {
    margin: 10px;
    text-align: center;
    position: absolute; /* position을 absolute로 변경 */
    z-index: 5; /* 찾기 버튼을 지도 위로 올리기 위한 z-index 값 */
  }
</style>
  