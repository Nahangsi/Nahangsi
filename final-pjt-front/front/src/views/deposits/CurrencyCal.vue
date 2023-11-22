<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>
            <h2 class="headline">환율 계산기💰</h2>
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col cols="10" md="6">
                <v-autocomplete
                  v-model="select1"
                  :items="payments"
                  variant="outlined"
                  label="환율 국가 선택"
                ></v-autocomplete>
              </v-col>
              <v-col cols="10" md="6">
                <v-autocomplete
                  v-model="select2"
                  :items="criterion"
                  variant="outlined"
                  label="환율 기준 선택"
                ></v-autocomplete>
              </v-col>
            </v-row>

           
            <v-row>
              <v-col cols="10" md="6">
                <v-text-field
                  v-model.number="payment1"
                  @input="updatePayment2(Math.round((payment1 * rate) / currencyUnit))"
                  variant="outlined"
                  label="가격 선택"
                >
                  <template v-slot:append>
                    {{ currencyName }}
                  </template>
                </v-text-field>
              </v-col>
              <v-col cols="10" md="6">
                <v-text-field
                  v-model.number="payment2"
                  @input="updatePayment1(Math.round((payment2 / rate) * currencyUnit))"
                  variant="outlined"
                  label="대한민국 (KRW)"
                  suffix="원"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, watch } from "vue";
import axios from "axios";


const payments = ref([
  "미국", "유럽", "일본", "영국", "스위스", "캐나다", "호주", "중국", "홍콩", "스웨덴", "뉴질랜드", "싱가포르", "노르웨이", "멕시코", "인도", "러시아", "남아공", "터키", "브라질", "아랍에미리트", "바레인", "브루나이", "체코", "덴마크", "인도네시아", "이스라엘", "말레이시아", "카타르", "사우디", "태국", "대만", "이집트", "헝가리", "쿠웨이트", "폴란드", "파키스탄", "방글라데시", "요르단", "카자흐스탄", "몽골", "베트남"
]);

const countries = {
  미국: "USD", 유럽: "EUR", 일본: "JPY", 영국: "GBP", 스위스: "CHF", 캐나다: "CAD", 호주: "AUD", 중국: "CNY", 홍콩: "HKD", 스웨덴: "SEK", 뉴질랜드: "NZD", 싱가포르: "SGD", 노르웨이: "NOK", 멕시코: "MXN", 인도: "INR", 러시아: "RUB", 남아공: "ZAR", 터키: "TRY", 브라질: "BRL", 아랍에미리트: "AED", 바레인: "BHD", 브루나이: "BND", 체코: "CZK", 덴마크: "DKK", 인도네시아: "IDR", 이스라엘: "ILS", 말레이시아: "MYR", 카타르: "QAR", 사우디: "SAR", 태국: "THB", 대만: "TWD", 이집트: "EGP", 헝가리: "HUF", 쿠웨이트: "KWD", 필리핀: "PHP", 폴란드: "PLN", 파키스탄: "PKR", 방글라데시: "BDT", 요르단: "JOD", 카자흐스탄: "KZT", 몽골: "MNT", 베트남: "VND"
};

const criterion = ref(["매매기준율", "현찰 살때", "현찰 팔때"]);

const select1 = ref(null);
const select2 = ref("매매기준율");

watch([select1, select2], ([newOption1, newOption2]) => {
  if (newOption1 !== null && newOption2 !== null) {
    axios({
      url: `https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${countries[newOption1]}`,
      method: "GET",
    })
      .then(({ data }) => {
        currencyUnit.value = data[0]?.currencyUnit || 1;
        currencyName.value = data[0]?.currencyName || 1;
        currencyCode.value = data[0]?.currencyCode || 1;
        country.value = data[0]?.country || 1;
        if (newOption2 == "매매기준율") {
          rate.value = data[0]?.basePrice || -1;
        } else if (newOption2 == "현찰 살때") {
          rate.value = data[0]?.cashBuyingPrice || -1;
        } else {
          rate.value = data[0]?.cashSellingPrice || -1;
        }
        payment1.value = 0;
        payment2.value = 0;
      })
      .catch((err) => console.log(err));
  }
});

const payment1 = ref(0);
const payment2 = ref(0);

const updatePayment1 = function (value) {
  payment1.value = value;
};

const updatePayment2 = function (value) {
  payment2.value = value;
};

const rate = ref(null);
const currencyUnit = ref(null);
const currencyName = ref(null);
const currencyCode = ref(null);
const country = ref(null);

watch([currencyName], () => {
  console.log("currencyName changed:", currencyName.value);
});
</script>

<style scoped>
.custom-select {

}
</style>
