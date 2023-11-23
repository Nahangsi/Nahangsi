<template>
  <v-container>
    <v-row style="margin-left:50px" justify="center">
      <v-col md="6"  @click="rate=true"  button>예금 상품</v-col>
      <v-col md="6"  @click="rate=false" button>적금 상품</v-col>
    </v-row>
  </v-container>

  
  <v-container style="margin-bottom : 100px;">
    <v-row justify="center" v-if="viewproduct">
      <v-col v-show="rate==true">
        <div v-for="depositProduct in depositProducts" :key="depositProduct.id">
          <v-card class="card">
            <v-card-title>{{ depositProduct.fin_prdt_nm }}</v-card-title>
            <v-card-text>
              <v-list-item>
                <v-list-content>최고 우대 금리 : </v-list-content>
                <v-list-content>{{ getMaxIntrRate2(depositProduct.depositoptions_set) }}</v-list-content>
              </v-list-item>
              <v-list-item>
                <v-list-content>기본 금리 : </v-list-content>
                <v-list-content>{{ getMaxIntrRate(depositProduct.depositoptions_set) }}</v-list-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>가입 대상 : </v-list-item-content>
                <v-list-item-content>{{ depositProduct.join_member }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>가입 기간 : </v-list-item-content>
                <v-list-item-content>{{getSavetrmText(depositProduct.depositoptions_set)}}</v-list-item-content>
              </v-list-item>
            </v-card-text>

          </v-card>
        </div>
      </v-col>
      <v-col v-show="rate==false">
        <div v-for="savingProduct in savingProducts" :key="savingProduct.id">
          <v-card class="card">
            <v-card-title>{{ savingProduct.fin_prdt_nm }}</v-card-title>
            <v-card-text>
              <v-list-item>
                <v-list-content>최고 금리 : </v-list-content>
                <v-list-content>{{ getMaxIntrRate2(savingProduct.savingoptions_set) }}</v-list-content>
              </v-list-item>
              <v-list-item>
                <v-list-content>기본 금리 : </v-list-content>
                <v-list-content>{{ getMaxIntrRate(savingProduct.savingoptions_set) }}</v-list-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>가입 대상 : </v-list-item-content>
                <v-list-item-content>{{ savingProduct.join_member }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>가입 기간 : </v-list-item-content>
                <v-list-item-content>{{ getSavetrmText(savingProduct.savingoptions_set) }}</v-list-item-content>
              </v-list-item>
            </v-card-text>
          </v-card>
        </div>
      </v-col>

    </v-row>     
  </v-container>   
</template>

<script setup>
import { onMounted, ref } from 'vue'
// true : 예금, false : 적금
const rate = ref(true);

const likedDepositProducts = JSON.parse(localStorage.getItem('likedDepositProducts')) || [];
const likedsavingProducts = JSON.parse(localStorage.getItem('likedsavingProducts')) || [];

const depositProducts = ref(null);
const savingProducts = ref(null);

const getMaxIntrRate2 = (arr) => {
  const maxRate = Math.max(...arr.map((item) => item.intr_rate2));
  return maxRate.toFixed(2) + '%';
}

const getMaxIntrRate = (arr) => {
  const maxRate = Math.max(...arr.map((item) => item.intr_rate));
  return maxRate.toFixed(2) + '%';
}

const getallsavetrm = (arr) => {
  return arr.map((item) => item.save_trm);
}

const getSavetrmText = (optionsSet) => {
  const savetrmArray = getallsavetrm(optionsSet);
  const savetrmArray2 = savetrmArray.map((item) => item + '개월');
  return savetrmArray2.join(', ');
};

const viewproduct = () => {
  
    depositProducts.value = likedDepositProducts.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate2));
      };
      const maxIntrRateA = getMaxIntrRate(a.depositoptions_set);
      const maxIntrRateB = getMaxIntrRate(b.depositoptions_set);

      return maxIntrRateB - maxIntrRateA;
    })
    
    savingProducts.value = likedsavingProducts.sort((a, b) => {
      const getMaxIntrRate = (arr) => {
        return Math.max(...arr.map((item) => item.intr_rate))
      }

      const maxIntrRateA = getMaxIntrRate(a.savingoptions_set)
      const maxIntrRateB = getMaxIntrRate(b.savingoptions_set)

      return maxIntrRateB - maxIntrRateA
    }).reverse()
  
  console.log(depositProducts.value)
  console.log(savingProducts.value)
}

onMounted(() => {
  viewproduct()
})


</script>

<style scoped>
.card {
  margin-bottom: 30px;
}
</style>