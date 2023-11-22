<template>
    <div>
      정기 예금
      <button @click="rate=true">최고금리순</button>
      <button @click="rate=false">기본 금리순</button>

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
                <div v-for="depositProduct in bestproducts">
                    <DepositProductItemBest :depositProduct="depositProduct" />
                </div>
            </div>
            <div v-show="rate === false">
                <div v-for="depositProduct in basicproducts">
                    <DepositProductItemBsic :depositProduct="depositProduct" />
                </div>
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
  const basicproducts = ref(null)
  const bestproducts = ref(null)

  const bottomSheetOpen = ref(false)

  const rate = ref(true)

  const selectterm = (term) => {
    const result = []
    for (const product of depositProducts.value) {
        const filteredItems = product.depositoptions_set.filter((item) => {
            return item.save_trm === term
        })
        filteredItems.forEach((filteredItem) => {
            const newProduct = {
                ...product,
                depositoptions_set: [filteredItem]
            }
            result.push(newProduct)
        })
    }
    
    if (rate.value === true) {
        bestproducts.value = result.sort((a, b) => {
            const getMaxIntrRate = (arr) => {
                return Math.max(...arr.map((item) => item.intr_rate2))
            }

            const maxIntrRateA = getMaxIntrRate(a.depositoptions_set)
            const maxIntrRateB = getMaxIntrRate(b.depositoptions_set)

            return maxIntrRateB - maxIntrRateA
        })
    } else {
        basicproducts.value = result.sort((a, b) => {
            const getMaxIntrRate = (arr) => {
                return Math.max(...arr.map((item) => item.intr_rate))
            }

            const maxIntrRateA = getMaxIntrRate(a.depositoptions_set)
            const maxIntrRateB = getMaxIntrRate(b.depositoptions_set)

            return maxIntrRateB - maxIntrRateA
        })
    }
    bottomSheetOpen.value = false
  }

  onMounted(() => {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/deposits/deposit-product/'
    })
    .then((res) => {
      depositProducts.value = res.data
      basicproducts.value = res.data.slice().sort((a, b) => {
        const getMaxIntrRate = (arr) => {
          return Math.max(...arr.map((item) => item.intr_rate))
        }

        const maxIntrRateA = getMaxIntrRate(a.depositoptions_set)
        const maxIntrRateB = getMaxIntrRate(b.depositoptions_set)

        return maxIntrRateB - maxIntrRateA
      })
      bestproducts.value = res.data.slice().sort((a, b) => {
        const getMaxIntrRate = (arr) => {
          return Math.max(...arr.map((item) => item.intr_rate2))
        }

        const maxIntrRateA = getMaxIntrRate(a.depositoptions_set)
        const maxIntrRateB = getMaxIntrRate(b.depositoptions_set)

        return maxIntrRateB - maxIntrRateA
      })
    })
  })
  
  </script>
  
  <style scoped>
  
  </style>
  