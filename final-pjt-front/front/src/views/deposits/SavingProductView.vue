<template>
    <div>
      정기 적금
      <button @click="rate = true">최고금리순</button>
      <button @click="rate = false">기본금리순</button>
  
      <v-bottom-sheet v-model="bottomSheetOpen">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" text="Click Me"></v-btn>
        </template>
  
        <v-card height="400">
          <v-btn height="50" @click="selectterm(6)">6개월</v-btn>
          <v-btn height="50" @click="selectterm(12)">12개월</v-btn>
          <v-btn height="50" @click="selectterm(24)">24개월</v-btn>
          <v-btn height="50" @click="selectterm(36)">36개월</v-btn>
        </v-card>
      </v-bottom-sheet>
  
      <div>
        <div v-show="rate === true">
          <div v-for="savingProduct in bestproducts">
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
  

  const selectedTerm = ref(36);
  const savingProducts = ref(null);
  const basicproducts = ref(null);
  const bestproducts = ref(null);
  
  const bottomSheetOpen = ref(false);
  
  const rate = ref(true);
  
  const selectterm = (term) => {
    selectedTerm.value = term;
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
        
      bestproducts.value = [...result].sort((a, b) => {
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
      basicproducts.value = [...result].sort((a, b) => {
        const getMaxIntrRate = (arr) => {
          return Math.max(...arr.map((item) => item.intr_rate));
        };
  
        const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
        const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);
  
        return maxIntrRateB - maxIntrRateA;
      });
    }
    bottomSheetOpen.value = false;
  };

  
  onMounted(() => {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/deposits/saving-product/",
    }).then((res) => {
      savingProducts.value = res.data;
    //   기본 금리 순
      basicproducts.value = res.data.slice().sort((a, b) => {
        const getMaxIntrRate = (arr) => {
          return Math.max(...arr.map((item) => item.intr_rate));
        };
  
        const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
        const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);
  
        return maxIntrRateB - maxIntrRateA;
      });
      // 최고 금리 순
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
  </script>
  
  <style scoped></style>
  