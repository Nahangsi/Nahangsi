<template>
  <div>
    정기 적금
    <button @click="rate=true">최고금리순</button>
    <button @click="rate=false">기본금리순</button>

    <v-bottom-sheet v-model="bottomSheetOpen">
  <template v-slot:activator="{ props }">
    <v-btn v-bind="props" text="Click Me"></v-btn>
  </template>

  <v-card height="400">
    <v-btn height="50"  @click="selectterm(6)">6개월</v-btn>
    <v-btn height="50" @click="selectterm(12)">12개월</v-btn>
    <v-btn height="50" @click="selectterm(24)">24개월</v-btn>
    <v-btn height="50" @click="selectterm(36)">36개월</v-btn>
  </v-card>
</v-bottom-sheet>


    <div>
  <div v-show="rate === true">
    <div v-for="savingProduct in bestproducts">
      <SavingProductItemBest :savingProduct="savingProduct"/>  
    </div>
  </div>
  <div v-show="rate === false">
    <div v-for="savingProduct in basicproducts">
      <SavingProductItemBasic :savingProduct="savingProduct"/>  
    </div>
  </div>
</div>


  </div>
</template>

<script setup>

import axios from "axios";
import { ref } from "vue";
import { onMounted } from "vue";
import SavingProductItemBasic from "@/components/deposit/SavingProductItemBasic.vue"
import SavingProductItemBest from "@/components/deposit/SavingProductItemBest.vue"



const savingProducts = ref(null)
const basicproducts = ref(null)
const bestproducts = ref(null)

const bottomSheetOpen = ref(false)

const rate = ref(true)

const selectterm = (term) => {}


onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/deposits/saving-product/'
  })
  .then((res) => {
    savingProducts.value = res.data
  })
  .then((res) => {
    basicproducts.value = savingProducts.value.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map(item => item.intr_rate));
      };
      
      const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);

      return maxIntrRateB - maxIntrRateA; 
    });
  })
  .then(() => {
    bestproducts.value = savingProducts.value.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map(item => item.intr_rate2));
      };
      
      const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);

      return maxIntrRateB - maxIntrRateA; 
    });
  })
})


</script>

<style  scoped>

</style>