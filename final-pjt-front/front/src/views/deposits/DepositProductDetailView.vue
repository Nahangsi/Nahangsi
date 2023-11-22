<template >
  <div v-if="item">

    <v-card text=""  class="mb-5 backwhite"
    >
      <v-card-text>
        <v-avatar
      class="icon"
      image="https://item.kakaocdn.net/do/9fc0462374fa73111ee6b47046b9ce7b8b566dca82634c93f811198148a26065"
      size="40"
    ></v-avatar>
    <h2>{{ item.kor_co_nm }}</h2>
    <h3>{{ item.fin_prdt_nm }}</h3>
    <p>{{ item.kor_co_nm }}에서 보기></p>
    <P>금융 감독원 {{ item.dcls_strt_day.substring(2,4) }}.{{ item.dcls_strt_day.substring(4,6) }}.{{ item.dcls_strt_day.substring(6,8)}}일 공시된 내용 기반</P>
        </v-card-text>
    </v-card>

    <v-card text="" variant="tonal" class="mb-5">
      <v-card-text>
        <h2>가입기간 별 금리</h2>
     <div v-for="option in item.depositoptions_set">
      <div v-if="option.intr_rate">
        <v-btn>
        <div>{{option.save_trm}} 개월</div>
        <div>기본 {{ option.intr_rate }}%</div>
      </v-btn>
      <h3>금리 {{ option.intr_rate2 }}%</h3>
      <p>기본 {{ option.intr_rate }}% + 우대 {{ (option.intr_rate2 - option.intr_rate).toFixed(1) }}%</p>
      </div>
     </div>
          
        </v-card-text>


    </v-card>


  <v-card
  variant="tonal"
    class="backwhite"
  >
    <v-card-title>
      상품 정보
    </v-card-title>

    <v-card-text>
          <h2>가입 대상</h2>
          {{ item.join_member }}
        </v-card-text>
        <v-divider :thickness="1"></v-divider>
        
    <v-card-text >
          <h2>가입 방법</h2>
          {{ item.join_way }}
        </v-card-text>
        <v-divider :thickness="1"></v-divider>

    <v-card-actions>
      
      <v-spacer></v-spacer> 
      더보기
      <v-btn
        :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
        @click="cardshow = !cardshow"
      ></v-btn>
    </v-card-actions>

    <v-expand-transition class="last">
      <div v-show="cardshow">
        <v-divider></v-divider>

        <v-card-text>
         <h2>만기 후 이자율</h2>
         <p>{{ item.mtrt_int }}</p>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-text>
         <h2>기타 유의사항</h2>
         <p>{{ item.etc_note }}</p>
        </v-card-text>

      </div>
    </v-expand-transition>
  </v-card>


  </div>
</template>

<script setup>

import { useRoute } from 'vue-router';
import { onMounted, ref } from 'vue';

import axios from 'axios';

const route = useRoute()
const item = ref(null)
const cardshow = ref(false)

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/deposits/deposit-product/${route.params.id}`
  })
  .then((res) => {
    item.value = res.data[0]
  })
  .catch((err) => {
  })
})





</script>

<style scoped>

.last {
  padding-bottom: 100px;
  margin-bottom: 50px;
}
.backwhite {
  background-color: whitesmoke;
}

</style>