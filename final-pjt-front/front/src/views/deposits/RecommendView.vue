<template>

<v-container>
    <v-row style="margin-left:50px" justify="center">
      <v-col md="6"  @click="rate=true"  button>예금 상품</v-col>
      <v-col md="6"  @click="rate=false" button>적금 상품</v-col>
    </v-row>
  </v-container>
    <div>
      
        {{ User.age }}
        {{ User.money }}
        {{ User.salary }}
        {{ User.financial_products }}
        {{ User.primary_bank }}
        {{ User.savings_term }}
    </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import axios from 'axios'
import {useAccountStore} from '@/stores/account'

const rate = ref(true)
const store = useAccountStore()
const User = store.userinfo
const savingProducts = ref([]);
const depositProducts = ref([])
const basicproducts = ref([])
const bestproducts = ref([])

onMounted(() => {
    // 예금 상품 가져오기
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

    // 적금 상품 가져오기
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
})

</script>

<style scoped>

</style>