<template>

<v-container>
    <v-row style="margin-left:50px" justify="center">
      <v-col md="6"  @click="rate=true"  button>예금 상품</v-col>
      <v-col md="6"  @click="rate=false" button>적금 상품</v-col>
    </v-row>
</v-container>

{{ User.depositoptions_set }}
<v-container style="margin-bottom : 100px;">
  <v-row justify="center">
    <v-col v-show="rate==true">
      <div v-for="bestproduct in bestproducts" :key="bestproduct.id">
        <v-card class="card">
          <v-card-title>{{ bestproduct.fin_prdt_nm }}</v-card-title>
          <v-card-text>
            <v-list-item>
              <v-list-content>최고 우대 금리 : </v-list-content>
              <v-list-content>{{ getMaxIntrRate2(bestproduct.depositoptions_set) }}</v-list-content>
            </v-list-item>
            <v-list-item>
              <v-list-content>기본 금리 : </v-list-content>
              <v-list-content>{{ getMaxIntrRate(bestproduct.depositoptions_set) }}</v-list-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>가입 대상 : </v-list-item-content>
              <v-list-item-content>{{ bestproduct.join_member }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>유의사항 : </v-list-item-content>
              <v-list-item-content>{{ bestproduct.etc_note }}</v-list-item-content>
            </v-list-item>
          </v-card-text>
        </v-card>
      </div>
    </v-col>

    <v-col v-show="rate==false">
        <div v-for="bestproduct in bestproducts2" :key="bestproduct.id">
          <v-card class="card">
            <v-card-title>{{ bestproduct.fin_prdt_nm }}</v-card-title>
            <v-card-text>
              <v-list-item>
                <v-list-content>최고 금리 : </v-list-content>
                <v-list-content>{{ getMaxIntrRate2(bestproduct.savingoptions_set) }}</v-list-content>
              </v-list-item>
              <v-list-item>
                <v-list-content>기본 금리 : </v-list-content>
                <v-list-content>{{ getMaxIntrRate(bestproduct.savingoptions_set) }}</v-list-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>가입 대상 : </v-list-item-content>
                <v-list-item-content>{{ bestproduct.join_member }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>유의사항 : </v-list-item-content>
                <v-list-item-content>{{ bestproduct.etc_note }}</v-list-item-content>
              </v-list-item>
            </v-card-text>
          </v-card>
        </div>
    </v-col>
  </v-row>
</v-container>  
    
</template>

<script setup>
import {ref, onMounted} from 'vue'
import axios from 'axios'
import {useAccountStore} from '@/stores/account'

const rate = ref(true)
const store = useAccountStore()
const User = store.userinfo
const savingProducts = ref(null);
const depositProducts = ref(null)
const bestproducts = ref(null)
const bestproducts2 = ref(null)

const getMaxIntrRate = (arr) => {
  return Math.max(...arr.map((item) => item.intr_rate));
};

const getMaxIntrRate2 = (arr) => {
  return Math.max(...arr.map((item) => item.intr_rate2));
};


onMounted(() => {
    // 예금 상품 가져오기
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/deposits/deposit-product/'
    })
    .then((res) => {
      // 예금 상품 가져오기
      depositProducts.value = res.data
      // 최고 금리순으로 정렬하기
      bestproducts.value = res.data.slice().sort((a, b) => {
        const getMaxIntrRate = (arr) => {
          return Math.max(...arr.map((item) => item.intr_rate2));
        };
  
        const maxIntrRateA = getMaxIntrRate(a.depositoptions_set);
        const maxIntrRateB = getMaxIntrRate(b.depositoptions_set);
  
        return maxIntrRateB - maxIntrRateA;
        });
      // 정렬한 상태에서 내가 이미 가입한 상품은 제외하고,
      // 원하는 기간에 맞는 상품만 가져오기,
      // 가장 높은 금리에 있는 상품 중 상위 3개 가져오기
      const filteredProducts = bestproducts.value
        .filter((item) => !User.financial_products.includes(item.id))
        .filter((item) => item.depositoptions_set.some((option) => option.save_trm === User.savings_term))
        .filter((item) => item.depositoptions_set.some((option) => option.kor_co_nm === User.primary_bank));

      if (filteredProducts.length > 0) {
        bestproducts.value = filteredProducts.slice(0, 3);
      } else {
        // 주거래 은행에 해당하는 상품이 없을 경우, 전체 예금 상품에서 상위 3개를 추천
        bestproducts.value = bestproducts.value.slice(0, 3);
      }
      });

    // 적금 상품 가져오기
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/deposits/saving-product/",
    }).then((res) => {
      savingProducts.value = res.data;
      bestproducts2.value = res.data.slice().sort((a, b) => {
        const getMaxIntrRate = (arr) => {
          return Math.max(...arr.map((item) => item.intr_rate2));
        };
  
        const maxIntrRateA = getMaxIntrRate(a.savingoptions_set);
        const maxIntrRateB = getMaxIntrRate(b.savingoptions_set);
  
        return maxIntrRateB - maxIntrRateA;
      });
      // 정렬한 상태에서 내가 이미 가입한 상품은 제외하기
      // 내가 원하는 기간에 맞는 상품만 가져오기
      // 이 중에서 가장 높은 금리에 있는 상품 최대 3개 가져오기

      // const filteredProducts2 = bestproducts2.value
      //   .filter((item) => !User.financial_products.includes(item.id))
      //   .filter((item) => item.savingoptions_set.some((option) => option.save_trm === User.savings_term))
      //   .filter((item) => item.savingoptions_set.some((option) => option.kor_co_nm === User.primary_bank));

      
      // if (filteredProducts2.length > 0) {
      //   bestproducts2.value = filteredProducts2.slice(0, 3);
      // } else {
      //   bestproducts2.value = bestproducts2.value.slice(0, 3);
      // }
      const filteredProducts2 = bestproducts2.value
        .filter((item) => !User.financial_products.includes(item.id))
        .filter((item) => item.savingoptions_set.some((option) => option.save_trm === User.savings_term))
        .filter((item) => item.savingoptions_set.some((option) => option.kor_co_nm === User.primary_bank));

      // Separate the products with the specified primary bank from the rest
      const primaryBankProducts2 = filteredProducts2.filter((item) => item.savingoptions_set.some((option) => option.kor_co_nm === User.primary_bank));
      const otherProducts2 = filteredProducts2.filter((item) => !item.savingoptions_set.some((option) => option.kor_co_nm === User.primary_bank));

      // Sort the products to bring the specified primary bank to the top
      const sortedProducts2 = [...primaryBankProducts2, ...otherProducts2];

      // Update the bestproducts2.value with the sorted products (up to 3)
      if (sortedProducts2.length > 0) {
        bestproducts2.value = sortedProducts2.slice(0, 3);
      } else {
        bestproducts2.value = bestproducts2.value.slice(0, 3);
      }
    });
})

</script>

<style scoped>
.card {
  margin-bottom: 30px;
}
</style>