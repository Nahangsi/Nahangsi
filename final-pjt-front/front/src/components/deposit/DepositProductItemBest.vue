<template>
  <div @click="godetail">
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
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { onMounted } from "vue";


const router = useRouter()
const props = defineProps({
  depositProduct: Object

})


const everyone = ref('')
const remote = ref('직접가입')


const maxRate1 = computed(() => {
  return Math.max(
  ...props.depositProduct.depositoptions_set.map((item) => item.intr_rate)
);
})

const maxRate2 = computed(() => {
  return props.depositProduct.depositoptions_set.reduce(
  (max, currentValue) => {
    if (currentValue.intr_rate2 > max) {
      return currentValue.intr_rate2;
    }
    return max;
  },
  0
);
})


if (props.depositProduct.join_deny === 1) {
  everyone.value = '누구나가입'
} else if (props.depositProduct.join_deny === 3) {
  everyone.value = '일부제한'
}
if (props.depositProduct.join_way !== undefined && (props.depositProduct.join_way.includes('인터넷') || (props.depositProduct.join_way.includes('스마트폰'))) ) {
  remote.value = '방문없이가입'
}


const godetail = () => {
  console.log(props.depositProduct)

  router.push({name: 'productdetail', params: {id : props.depositProduct.fin_prdt_cd}})

}
</script>

<style scoped>
.icon {
  box-shadow: 1px 2px 8px #cccccc;
}

</style>








