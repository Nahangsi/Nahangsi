<template>
  <div class="gray" v-if="item" style="height: 1500px;">
    <v-card variant="flat" class="mb-5 card" height="300px">
      <v-card-text>
        <v-avatar
          class="icon mt-2 mb-7"
          :image= "`src/assets/${depositProduct.kor_co_nm}.png`"
          size="70"
          
        ></v-avatar>
        <h2 class="mb-2">{{ item.kor_co_nm }}</h2>
        <h2 class="mb-2">{{ item.fin_prdt_nm }}</h2>
        <p style="margin-top: 50px; font-size: 15px; font-weight: bolder;" class="fontgray">{{ item.kor_co_nm }}에서 보기></p>
        <P class="fontgray" style="margin-top: 10px; font-size: 13px; font-weight: 300;">금융 감독원 {{ item.dcls_strt_day.substring(2, 4) }}.{{
            item.dcls_strt_day.substring(4, 6)
          }}.{{ item.dcls_strt_day.substring(6, 8) }}일 공시된 내용 기반</P
        >
      </v-card-text>
    </v-card>

    <v-card variant="flat" class="mb-5 card">
      <h2 class="mtt bold-text">가입기간 별 금리</h2>
      <div class="btn">
        <v-card-text class="flex wrap">
          <div v-for="option in item.depositoptions_set">
            <div v-if="option.intr_rate">
              <v-btn
                @click="getrate(option.save_trm)"
                class="mr-1 ml-1 bbb"
                height="70px"
                width="85px"
                color="#545B66"
              >
                <div class="pa">
                  <div class="bold-text">{{ option.save_trm }} 개월</div>
                  <div>기본 {{ option.intr_rate }}%</div>
                </div>
              </v-btn>
            </div>
          </div>
        </v-card-text>
        <h3 class="mt-7 big font">최고 금리 {{ rate2 }}%</h3>
        <div class="mt-3">
          <span class="fontgray">기본 {{ rate1 }}% + </span>
          <span class="font">우대 {{ (rate2 - rate1).toFixed(1) }}%</span>
        </div>
      </div>
    </v-card>

    <v-card variant="flat" class="card" height="700px">
      <h2 class="mtt bold-text">가입 정보</h2>

      <v-card-text>
        <h2 class="ml-1 mt-2 mb-3 fontgray bold-text">가입 대상</h2>
        <p class="ml-1 fontgray">{{ item.join_member }}</p>
      </v-card-text>
      <v-divider :thickness="1"></v-divider>

      <v-card-text>
        <h2 class="ml-1 mt-2 mb-3 fontgray bold-text">가입 방법</h2>
        <p class="ml-1 fontgray">{{ item.join_way }}</p>
      </v-card-text>
      <v-divider :thickness="1"></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        더보기
        <v-btn
          :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
          @click="cardshow = !cardshow"
          variant="text"
        ></v-btn>
      </v-card-actions>

      <v-expand-transition>
        <div v-show="cardshow">
          <v-card-text style="margin-top: 0px; padding-top: 0px;">
            <h2 class="ml-1 mt-2 mb-3 fontgray bold-text">만기 후 이자율</h2>
            <p class="ml-1 fontgray">{{ item.mtrt_int }}</p>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-text>
            <h2 class="ml-1 mt-2 mb-3 fontgray bold-text">기타 유의사항</h2>
            <p class="ml-1 fontgray">{{ item.etc_note }}</p>
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { onMounted, ref } from "vue";

import axios from "axios";

const route = useRoute();
const item = ref(null);
const cardshow = ref(false);

const rate1 = ref(null);
const rate2 = ref(null);

const getrate = (term) => {
  item.value.depositoptions_set.forEach((x) => {
    if (x.save_trm === term) {
      rate1.value = x.intr_rate;
      rate2.value = x.intr_rate2;
    }
  });
};

onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/api/deposits/deposit-product/${route.params.id}`,
  })
    .then((res) => {
      item.value = res.data[0];

      rate1.value = item.value.depositoptions_set[0].intr_rate;
      rate2.value = item.value.depositoptions_set[0].intr_rate2;
    })
    .catch((err) => {});
});
</script>

<style scoped>
.last {
  padding-bottom: 400px;
  margin-bottom: 200px;
}
.backwhite {
  background-color: whitesmoke;
}
.flex {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.inline {
  display: inline;
}
.btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 70px;
  margin-bottom: 50px;
}

.card {
  height: 500px;
  margin-top: 10px;
}
.mtt {
  margin-top: 40px;
  margin-left: 18px;
}
.pa {
  margin: 20px;
}

.bold-text {
  font-weight: bolder; /* 두껍게 설정 */
}
.gray {
  background-color: #f6f7f9;
}
.font {
  color: #1e88e5;
}

.big {
  font-size: 29px;
  font-weight: bolder;
}

.fontgray {
  color: #959595;
}
.icon {
  box-shadow: 1px 2px 8px #cccccc;
}
p { font-size: 16px;}
</style>
