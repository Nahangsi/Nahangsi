<template>
  <div>
    <p style="font-size: 30px; font-weight: 700; margin: 10px;">정기 예금</p>

    <v-form @submit.prevent="selectbank(bank)">
      <v-autocomplete
  label="은행 선택"
  :items="primaryBankItems"
  variant="underlined"
  v-model="bank"
  style="margin-bottom: -10px; margin-left: 10px; margin-right: 10px;"

></v-autocomplete>

<div title="은행 기간 비트윈" style="display: flex; flex-direction: row; justify-content: space-between;">

  <div style="width: 100px; margin-bottom: 10px; margin-left: 10px;">
  <v-btn   style="" type="submit" block class="mt-2 submit" variant="outlined"
          >은행 검색</v-btn
        >
      </div>
        <div title="기간선택" style="margin-top: 7px; margin-right: 10px;">
          <v-bottom-sheet v-model="bottomSheetOpenterm">
      <template v-slot:activator="{ props }">
        <v-btn color="#1E88E5" v-bind="props" text="기간 선택" variant="outlined"></v-btn>
      </template>

      <v-card height="400">
        <v-btn style="font-size: 20px;" variant="text" height="100" @click="selectterm(6)">6개월</v-btn>
        <v-divider :thickness="1"></v-divider>
        <v-btn style="font-size: 20px;" variant="text" height="100" @click="selectterm(12)">12개월</v-btn>
        <v-divider :thickness="1"></v-divider>
        <v-btn style="font-size: 20px;" variant="text" height="100" @click="selectterm(24)">24개월</v-btn>
        <v-divider :thickness="1"></v-divider>
        <v-btn style="font-size: 20px;" variant="text" height="100" @click="selectterm(36)">36개월</v-btn>
      </v-card>
    </v-bottom-sheet>
        </div>
</div>


    </v-form>

    <v-btn @click="rate = true" variant="text">
      최고금리순
</v-btn>
<v-btn @click="rate = false" variant="text">
      기본금리순
</v-btn>

    <div>
      <div v-show="rate === true">
        <div v-for="savingProduct in bestproducts" :key="savingProduct.id">
          <SavingProductItemBest :savingProduct="savingProduct" />
        </div>
      </div>
      <div v-show="rate === false">
        <div v-for="savingProduct in basicproducts">
          <SavingProductItemBasic :savingProduct="savingProduct" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { onMounted } from "vue";
import SavingProductItemBasic from "@/components/deposit/SavingProductItemBasic.vue";
import SavingProductItemBest from "@/components/deposit/SavingProductItemBest.vue";

const savingProducts = ref(null);
const basicproducts = ref(null);
const bestproducts = ref(null);

const bottomSheetOpenterm = ref(false);

const rate = ref(true);

const selectterm = (term) => {
  const result = [];
  for (const product of savingProducts.value) {
    const filteredItems = product.savingoptions_set.filter((item) => {
      return item.save_trm === term;
    });
    filteredItems.forEach((filteredItem) => {
      const newProduct = {
        ...product,
        savingoptions_set: [filteredItem],
      };
      result.push(newProduct);
    });
  }

  if (rate.value === true) {
    bestproducts.value = result.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate2));
      };

      const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
  } else {
    // result.sort((a, b) => {
    //   b.savingoptions_set[0].intr_rate - a.savingoptions_set[0].intr_rate;
    // });

    // basicproducts.value = result;
    basicproducts.value = result.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate));
      };

      const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
  }
  bottomSheetOpenterm.value = false;
  
};

const selectbank = (bank) => {

const result = [];
for (const product of savingProducts.value) {
  if (product.kor_co_nm === bank) {
    result.push(product)
  }
}

if (rate.value === true) {
  bestproducts.value = result.sort((a, b) => {
    const getMaxIntrRate = (arr) => {
      return Math.max(...arr.map((item) => item.intr_rate2));
    };

    const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
    const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);

    return maxIntrRateB - maxIntrRateA;
  });
} else {
  basicproducts.value = result.sort((a, b) => {
    const getMaxIntrRate = (arr) => {
      return Math.max(...arr.map((item) => item.intr_rate));
    };

    const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
    const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);

    return maxIntrRateB - maxIntrRateA;
  });
}
};

onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/api/deposits/saving-product/",
  }).then((res) => {
    savingProducts.value = res.data;
    basicproducts.value = res.data.slice().sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate));
      };

      const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);

      return maxIntrRateB - maxIntrRateA;
    });
    bestproducts.value = res.data.slice().sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate2));
      };

      const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);

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
