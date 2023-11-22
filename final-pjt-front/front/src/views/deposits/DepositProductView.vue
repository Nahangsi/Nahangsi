<template>
  <div>
    정기 예금
    <button @click="rate = true">최고금리순</button>
    <button @click="rate = false">기본금리순</button>

    <v-bottom-sheet v-model="bottomSheetOpenterm">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" text="기간 선택"></v-btn>
      </template>

      <v-card height="400">
        <v-btn height="50" @click="selectterm(6)">6개월</v-btn>
        <v-btn height="50" @click="selectterm(12)">12개월</v-btn>
        <v-btn height="50" @click="selectterm(24)">24개월</v-btn>
        <v-btn height="50" @click="selectterm(36)">36개월</v-btn>
      </v-card>
    </v-bottom-sheet>
    <v-form @submit.prevent="selectbank(bank)">
      <v-autocomplete
  label="은행 선택"
  :items="primaryBankItems"
  variant="outlined"
  v-model="bank"
></v-autocomplete>
<v-btn  type="submit" block class="mt-2 submit" variant="outlined"
          >Submit</v-btn
        >
    </v-form>




    <div v-show="rate === true">
      <div v-for="depositProduct in bestproducts">
        <DepositProductItemBest :depositProduct= "depositProduct"/>  
      </div>
    </div>
    <div v-show="rate === false">
      <div v-for="depositProduct in basicproducts">
          <DepositProductItemBsic :depositProduct="depositProduct" />
        </div>
    </div>

  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import DepositProductItemBest from "@/components/deposit/DepositProductItemBest.vue"
import DepositProductItemBsic from "@/components/deposit/DepositProductItemBsic.vue"

const depositProducts = ref(null)
const basicproducts = ref(null);
const bestproducts = ref(null);
const bottomSheetOpenterm = ref(false);
const bottomSheetOpenbank = ref(false);
const rate = ref(true);
const bank = ref(null)

const selectterm = (term) => {
  const result = [];
  for (const product of depositProducts.value) {
    const filteredItems = product.depositoptions_set.filter((item) => {
      return item.save_trm === term;
    });
    filteredItems.forEach((filteredItem) => {
      const newProduct = {
        ...product,
        depositoptions_set: [filteredItem],
      };
      result.push(newProduct);
    });
  }

  if (rate.value === true) {
    bestproducts.value = result.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate2));
      };

      const maxIntrRateA = getMaxIntrRate(a.depositoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.depositoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
  } else {
    basicproducts.value = result.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate));
      };

      const maxIntrRateA = getMaxIntrRate(a.depositoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.depositoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
  }
  bottomSheetOpenterm.value = false;
};


const selectbank = (bank) => {

  const result = [];
  for (const product of depositProducts.value) {
    if (product.kor_co_nm === bank) {
      result.push(product)
    }
  }

  if (rate.value === true) {
    bestproducts.value = result.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate2));
      };

      const maxIntrRateA = getMaxIntrRate(a.depositoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.depositoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
  } else {
    basicproducts.value = result.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate));
      };

      const maxIntrRateA = getMaxIntrRate(a.depositoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.depositoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
  }
  bottomSheetOpenbank.value = false;
};




onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/deposits/deposit-product/'
  })
  .then((res) => {
    depositProducts.value = res.data
    basicproducts.value = res.data.slice().sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate));
      };

      const maxIntrRateA = getMaxIntrRate(a.depositoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.depositoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
    bestproducts.value = res.data.slice().sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate2));
      };

      const maxIntrRateA = getMaxIntrRate(a.depositoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.depositoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
  });
});


const primaryBankItems = [
  "한국은행",
  "수출입은행",
  "KDB산업은행",
  "IBK기업은행",
  "Sh수협은행",
  "NH농협은행",
  "KB국민은행",
  "신한은행",
  "우리은행",
  "KEB하나은행",
  "부산은행",
  "경남은행",
  "대구은행",
  "광주은행",
  "전북은행",
  "제주은행",
  "SC제일은행",
  "씨티은행",
  "카카오뱅크",
  "케이뱅크",
  "토스뱅크",
];


</script>

<style scoped></style>


