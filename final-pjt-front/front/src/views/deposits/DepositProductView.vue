<template>
  <div>
    정기 예금
    <div v-for="depositProduct in depositProducts">
      <DepositProductItemBest :depositProduct= "depositProduct"/>  
    </div>
    
    

  </div>
</template>

<script setup>

import { useAccountStore } from "@/stores/account";
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { onMounted } from "vue";
import DepositProductItemBest from "@/components/deposit/DepositProductItemBest.vue"
import DepositProductItemBsic from "@/components/deposit/DepositProductItemBsic.vue"

const depositProducts = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/deposits/deposit-product/'
  })
  .then((res) => {
    depositProducts.value = res.data
  })
})

</script>

<style scoped>

</style>