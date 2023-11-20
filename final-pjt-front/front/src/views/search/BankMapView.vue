<template>
  <div>
    <h2>가까운 은행 검색하기</h2>
    <div>
      <div>
        <div>
          <div>
            <label for="mainList">시/도</label>
            <select
              @change="selectedProvince"
              id="mainList"
              v-model="selectPro"
            >
              <option v-for="province in store.mainList" :key="province">
                {{ province }}
              </option>
            </select>
          </div>
          <div>
            <label for="subList">시/군/구</label>
            <select @change="selectedCity" id="subList" v-model="selectCity">
              <option v-for="city in store.subList[selectPro]" :key="city">
                {{ city }}
              </option>
            </select>
          </div>
          <div>
            <label for="bankList">은행</label>
            <select @change="selectedBank" id="bankList" v-model="selectB">
              <option v-for="bank in store.bankList" :key="bank">
                <li>
                  {{ bank }}
                </li>

              </option>
            </select>

            <button @click="searchNow">찾기</button>
          </div>
        </div>

        <div class="map" id="map" style="width: 900px; height: 450px"></div>
        
        <div>
          <div v-if="bankMarkers.length > 0">
            <h6>
              {{ searchResultText }}
            </h6>
            <ul>
              <p
                v-for="bankMarker in bankMarkers"
                :key="bankMarker.place_name"
              >
                {{ bankMarker.place_name }}
              </p>
            </ul>
          </div>
          <div v-else>
            <h6>검색 목록이 없습니다.</h6>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from "vue";
  import { useLocationStore } from "@/stores/location";

  const store = useLocationStore();

  // 시도 / 시군구 / 은행 저장하는 변수
  const selectPro = ref("");
  const selectCity = ref("");
  const selectB = ref("");

  // 지도 저장
  const map = ref(null);

  // 은행 마커 저장
  const bankMarkers = ref([]);

  // 현재 열려있는 인포윈도우
  let currentInfowindow = null;

  // 드롭다운 선택
  const selectedProvince = (event) => {
    selectPro.value = event.target.value;
  };
  const selectedCity = (event) => {
    selectCity.value = event.target.value;
  };
  const selectedBank = (event) => {
    selectB.value = event.target.value;
  };

  // 지도가 넘 느려서 비동기로 처리...( 흠 어려움 )
  const loadMap = async () => {
    if (!window.kakao || !window.kakao.maps) {
      console.error("Kakao Maps API is not loaded.");
      return;
    }

    // 초기값은 우선... 싸피 구미캠 근처로...
    const mapContainer = document.getElementById("map");
    const mapOption = {
      center: new kakao.maps.LatLng(36.107071, 128.419289),
      level: 5,
    };

    // 지도 객체 생성
    map.value = new kakao.maps.Map(mapContainer, mapOption);
  };

  // 검색 결과 지도에 표시
  const placesSearchCB = async (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
      // 이전 은행 목록과 마커 초기화
      clearMarkers();

      // 검색 결과가 있으면 지도에 마커 표시 및 은행 목록 업데이트
      const bounds = new kakao.maps.LatLngBounds();

      for (let i = 0; i < data.length; i++) {
        // 마커 지도에 찍고 경계 만들긩
        displayMarker(data[i]);
        bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
      }

      // 마커 포함 지도 경계로 재설정
      map.value.setBounds(bounds);

      // 은행 목록 업데이트
      updateBankList(data);
    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
      console.warn("검색 결과가 없어요 !!");
      // 검색 결과 없는 경우 메세지 표시하기
    } else {
      console.error(`검색 실패 : ${status}`);
    }
  };

  // 은행 목록 업데이트 함수
  function updateBankList(data) {
    // 새로운 은행 목록 추가하기
    for (const marker of data) {
      bankMarkers.value.push({
        marker: null,
        place_name: marker.place_name,
      });

      // 콘솔 확인용 (나중에 지우기)
      console.log("은행: ", marker.place_name);
    }
  }

  const searchResultText = ref("");

  // 검색 버튼 클릭
  const searchNow = () => {
    const ps = new kakao.maps.services.Places(map.value);
    // 검색 키워드 저장
    const keyword = `${selectPro.value} ${selectCity.value} ${selectB.value}`;

    // 이전 은행 목록과 마커 초기화
    clearMarkers();

    // 검색
    ps.keywordSearch(
      keyword,
      (data, status, pagination) => {
        // 검색 결과가 있는 경우에만 텍스트 업데이트
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

  // 이전 마커 및 검색 결과 초기화 함수
  const clearMarkers = () => {
    for (const marker of bankMarkers.value) {
      if (marker.marker) {
        marker.marker.setMap(null);
      }
    }
    bankMarkers.value = [];
  };

  // 지도에 마커 표시
  function displayMarker(place) {
    const marker = new kakao.maps.Marker({
      map: map.value,
      position: new kakao.maps.LatLng(place.y, place.x),
    });

    // 마커 리스트 추가하기
    bankMarkers.value.push({
      marker: marker,
      place_name: place.place_name,
    });

    kakao.maps.event.addListener(marker, "click", function () {
      // 현재 열려있는 인포윈도우 닫기
      if (currentInfowindow) {
        currentInfowindow.close();
      }

      // 새로운 인포윈도우 열기
      const infowindow = new kakao.maps.InfoWindow({
        zIndex: 1,
        content: `<div style="padding:5px;font-size:12px;">${place.place_name}</div>`,
      });

      infowindow.open(map.value, marker);
      currentInfowindow = infowindow;
    });
  }

  // 컴포넌트가 마운트된 후 지도 로딩
  onMounted(loadMap);
</script>

<style scoped>




</style>