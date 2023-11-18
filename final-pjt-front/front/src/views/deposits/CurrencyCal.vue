<template>
  <div>
    <h1>환율 계산기</h1>

    <div>
      <select v-model="select1">
        <option v-for="payment in payments" :key="payment" :value="payment">
          {{ payment }} ({{ currencyCode }})
        </option>
        <br />
      </select>  :
      <input
        type="text"
        v-model.number="payment1"
        @input="updatePayment2(Math.round((payment1 * rate) / currencyUnit))"
      />
      {{ currencyName }}
    </div>
    <div>
      대한민국 (KRW) :
      <input
        type="text"
        v-model.number="payment2"
        @input="updatePayment1(Math.round((payment2 / rate) * currencyUnit))"
      />
      원
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import axios from "axios";

const payments = [
  "미국", "유럽", "일본", "영국","스위스","캐나다","호주","중국","홍콩","스웨덴","뉴질랜드","싱가포르","노르웨이","멕시코","인도","러시아","남아공","터키","브라질","아랍에미리트","바레인","브루나이","체코","덴마크","인도네시아","이스라엘","말레이시아","카타르","사우디","태국","대만","이집트","헝가리","쿠웨이트","필리핀","폴란드","파키스탄","방글라데시","요르단","카자흐스탄","몽골","베트남", "한국"
];

const countries = { 
  미국:"USD", 유럽: "EUR", 일본: "JPY", 영국: "GBP", 스위스: "CHF", 캐나다:"CAD", 호주:"AUD", 중국:"CNY", 홍콩:"HKD", 스웨덴:"SEK", 뉴질랜드:"NZD", 싱가포르:"SGD", 노르웨이:"NOK", 멕시코:"MXN", 인도:"INR", 러시아:"RUB", 남아공:"ZAR", 터키:"TRY", 브라질:"BRL", 아랍에미리트:"AED", 바레인:"BHD", 브루나이:"BND",체코:"CZK",덴마크:"DKK", 인도네시아:"IDR", 이스라엘:"ILS", 말레이시아:"MYR", 카타르:"QAR",사우디:"SAR", 태국:"THB", 대만:"TWD", 이집트:"EGP", 헝가리:"HUF", 쿠웨이트:"KWD", 필리핀:"PHP", 폴란드:"PLN", 파키스탄:"PKR", 방글라데시:"BDT", 요르단:"JOD", 카자흐스탄:"KZT", 몽골:"MNT", 베트남:"VND",
};

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
        rate.value = data[0]?.basePrice || -1;
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
</script>

<style scoped>

</style>
