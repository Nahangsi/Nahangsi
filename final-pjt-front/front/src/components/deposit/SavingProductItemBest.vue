<template>
  <div>
    <v-avatar
      class="icon"
      image="https://item.kakaocdn.net/do/9fc0462374fa73111ee6b47046b9ce7b8b566dca82634c93f811198148a26065"
      size="40"
    ></v-avatar>
    {{ savingProduct.kor_co_nm }}
    {{ savingProduct.fin_prdt_nm }}
    <h3>최고 {{ maxRate2 }} %</h3>
    <p>기본 {{ maxRate1 }} %</p>
    <v-chip>
      {{ saving }}
    </v-chip>
    <v-chip>
      {{ everyone }}
    </v-chip>
    <v-chip>
      {{ remote }}
    </v-chip>
    <v-divider :thickness="1"></v-divider>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { onMounted } from "vue";

const props = defineProps({
  savingProduct: Object,
}); // 최고 저축 금리


const maxrateitme = ref(null);

const everyone = ref("");
const remote = ref("직접가입");
const saving = ref("");
 
const maxRate1 = computed(() => {
  return Math.max(
  ...props.savingProduct.savingoptions_set.map((item) => item.intr_rate)
);
})

const maxRate2 = computed(() => {
  return props.savingProduct.savingoptions_set.reduce(
  (max, currentValue) => {
    if (currentValue.intr_rate2 > max) {
      maxrateitme.value = currentValue;
      return currentValue.intr_rate2;
    }
    return max;
  },
  0
);
})

// console.log(props.savingProduct.savingoptions_set)
if (props.savingProduct.join_deny === 1) {
  everyone.value = "누구나가입";
} else if (props.savingProduct.join_deny === 3) {
  everyone.value = "일부제한";
}
if (
  props.savingProduct.join_way !== undefined &&
  (props.savingProduct.join_way.includes("인터넷") ||
    props.savingProduct.join_way.includes("스마트폰"))
) {
  remote.value = "방문없이가입";
}

if (props.savingProduct.savingoptions_set[0].rsrv_type_nm === "자유적립식") {
  saving.value = "자유적금";
} else {
  saving.value = "정기적금";
}

</script>

<style scoped>
.icon {
  box-shadow: 1px 2px 8px #cccccc;
}
</style>
