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
import { ref } from "vue";
import { useRouter } from "vue-router";
import { onMounted } from "vue";

const props = defineProps({
  savingProduct: Object,
}); // 최고 저축 금리

if (props.savingProduct.savingoptions_set[0].save_trm === 6) {
  console.log(props.savingProduct);
}

const maxRate1 = ref(null);
// 최고 최고우대 금리
const maxRate2 = ref(null);
const maxrateitme = ref(null);

const everyone = ref("");
const remote = ref("직접가입");
const saving = ref("");

maxRate1.value = Math.max(
  ...props.savingProduct.savingoptions_set.map((item) => item.intr_rate)
);

maxRate2.value = props.savingProduct.savingoptions_set.reduce(
  (max, currentValue) => {
    if (currentValue.intr_rate2 > max) {
      maxrateitme.value = currentValue;
      return currentValue.intr_rate2;
    }
    return max;
  },
  0
);

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
if (maxrateitme.value.rsrv_type_nm === "자유적립식") {
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
