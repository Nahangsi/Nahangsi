<template>
    <div v-if="item">
      <v-avatar class="icon" image="https://item.kakaocdn.net/do/9fc0462374fa73111ee6b47046b9ce7b8b566dca82634c93f811198148a26065" size="40"></v-avatar>
      {{ depositProduct.kor_co_nm }}
      {{ depositProduct.fin_prdt_nm }}
      <h3>최고 {{ maxRate2 }} %</h3>
      <p>기본 {{ maxRate1 }} %</p>
      <v-chip>
        {{  everyone}}
  </v-chip>
  <v-chip>
    {{ remote }}
  </v-chip>
  <v-divider :thickness="1"></v-divider>
  
      
  
    </div>
  </template>
  
  <script setup>
  import { useAccountStore } from "@/stores/account";
  import axios from "axios";
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import { onMounted } from "vue";
  
  
  const item = ref(null)
  const props = defineProps({
    depositProduct: Object
  
  })// 최고 저축 금리
  const maxRate1 = ref(null)
  // 최고 최고우대 금리
  const maxRate2 = ref(null)
  
  const everyone = ref('')
  const remote = ref('직접가입')
  
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/deposits/deposit-product/${props.depositProduct.fin_prdt_cd}`
    })
    .then((res) => {
      item.value = res.data
    })
    .then((res) => {
      maxRate1.value = item.value.reduce((max, currentValue) => {
      if (currentValue.intr_rate > max) {
        return currentValue.intr_rate; 
      }
      return max; 
      }, 0);
      maxRate2.value = item.value.reduce((max, currentValue) => {
      if (currentValue.intr_rate2 > max) {
        return currentValue.intr_rate2; 
      }
      return max; 
      }, 0); 
    })
    .then((res) => {
      if (props.depositProduct.join_deny === 1) {
        everyone.value = '누구나가입'
      } else if (props.depositProduct.join_deny === 3) {
        everyone.value = '일부제한'
      }
      if (props.depositProduct.join_way !== undefined && (props.depositProduct.join_way.includes('인터넷') || (props.depositProduct.join_way.includes('스마트폰'))) ) {
        remote.value = '방문없이가입'
      }
      
    })
  })
  
  
  
  
  
  
  
  
  
  </script>
  
  <style scoped>
  .icon {
    box-shadow: 1px 2px 8px #cccccc;
  }
  
  </style>
  