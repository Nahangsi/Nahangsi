<template>
  <v-container>
    <v-row style="margin-left:50px" justify="center">
      <v-col md="6" v-model="money" @click="showDepositProducts"  button>예금 상품</v-col>
      <v-col md="6" v-model="money" @click="showSavingProducts" button>적금 상품</v-col>
    </v-row>
  </v-container>

  
  <v-container style="margin-bottom : 100px;" v-if="money">
    <v-row justify="center">
      <v-col v-for="selectedProduct in selectedProducts" :key="selectedProduct.fin_prdt_cd">
       <!-- {{ selectedProduct.depositoptions_set }} -->
        <v-card>
          <v-card-title>{{ selectedProduct.fin_prdt_nm }}</v-card-title>
          <v-card-text>
            <v-list-item>
              <v-list-item-content>최대 우대 금리 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.depositoptions_set[0].intr_rate2 }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>금리 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.depositoptions_set[0].intr_rate }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>가입 금액 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.join_member }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>가입 기간 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.depositoptions_set[0].save_trm }} 개월</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>가입 대상 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.join_member }}</v-list-item-content>
            </v-list-item>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

  <v-container v-else>
    <v-row justify="center">
      <v-col v-for="selectedProduct in selectedProducts" :key="selectedProduct.fin_prdt_cd">
       <!-- {{ selectedProduct.depositoptions_set }} -->
        <v-card>
          <v-card-title>{{ selectedProduct.fin_prdt_nm }}</v-card-title>
          <v-card-text>
            <v-list-item>
              <v-list-item-content>최대 우대 금리 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.savingoptions_set[0].intr_rate2 }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>금리 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.savingoptions_set[0].intr_rate }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>가입 금액 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.join_member }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>가입 기간 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.savingoptions_set[0].save_trm }} 개월</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>가입 대상 : </v-list-item-content>
              <v-list-item-content>{{ selectedProduct.join_member }}</v-list-item-content>
            </v-list-item>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const money = ref(false)
defineProps(['likedDepositProducts', 'likedsavingProducts'])
const likedDepositProducts = JSON.parse(localStorage.getItem('likedDepositProducts')) || [];
const likedsavingProducts = JSON.parse(localStorage.getItem('likedsavingProducts')) || [];
const selectedProducts = ref([])
const bestproducts = ref(null);

// 최대 우대 금리 구하기
// 내가 담은 상품의 옵션을 for문 돌면서 가장 높은 금리를 뽑는다
const deposit_best_intr2 = ref(0)
const deposit_best_intr = ref(0)

const saving_best_intr2 = ref(0)
const saving_best_intr = ref(0)
for (const product of likedDepositProducts) {
  for (const option of product.depositoptions_set) {
    if (option.intr_rate2 > deposit_best_intr2.value) {
      deposit_best_intr2.value = option.intr_rate2
    }
  }
}

for (const product of likedDepositProducts) {
  for (const option of product.depositoptions_set) {
    if (option.intr_rate > deposit_best_intr.value) {
      deposit_best_intr.value = option.intr_rate
    }
  }
}

const showDepositProducts = () => {
  money.value = true
  selectedProducts.value = likedDepositProducts
  console.log(selectedProducts.data)
}
const showSavingProducts = () => {
  selectedProducts.value = likedsavingProducts
}
</script>

<style scoped>

</style>