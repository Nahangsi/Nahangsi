<template>
  <div
    style="
      height: 150px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    "
    @click="godetail"
  >
    <div
      title="아이콘+옆에것들 전체박스"
      style="display: flex; flex-direction: row; margin: 10px"
    >
      <div title="아이콘" style="flex-grow: 2">
        <v-avatar
          class="icon"
          image="https://item.kakaocdn.net/do/9fc0462374fa73111ee6b47046b9ce7b8b566dca82634c93f811198148a26065"
          size="50"
        ></v-avatar>
      </div>
      <div
        title="글자+칩"
        style="display: flex; flex-grow: 8; flex-direction: column"
      >
        <div
          title="제목+금리"
          style="
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            flex-grow: 6;
          "
        >
          <div
            title="제목"
            style="display: flex; flex-direction: column; margin-bottom: 15px"
          >
            <p style="font-size: 14px; font-weight: 400">
              {{ savingProduct.kor_co_nm }}
            </p>
            <p style="font-size: 14px; font-weight: 400">
              {{ savingProduct.fin_prdt_nm }}
            </p>
          </div>
          <div
            title="금리"
            style="
              display: flex;
              flex-direction: column;
              flex-wrap: nowrap;
              align-items: flex-end;
              flex-grow: 4;"
          >
            <div>
              <p style="font-size: 18px; font-weight: 600; color: #1E88E5;">기본 {{ maxRate1 }} %</p>
            </div>
            <div>
              <p style="font-size: 14px; font-weight: 400; color: #858585;">최고 {{ maxRate2 }} %</p>
            </div>
          </div>
        </div>
        <div
          title="칩+좋아요"
          style="display: flex; justify-content: space-between"
        >
          <div title="칩">
            <v-chip  style="color: #858585; background-color: #F0F2F5; font-weight: 500; margin: 0 5px;" density="comfortable" variant="text">
      {{ saving }}
    </v-chip>

            <v-chip  style="color: #858585; background-color: #F0F2F5; font-weight: 500; margin: 0 5px;" density="comfortable" variant="text">
              {{ everyone }}
            </v-chip>
            <v-chip style="color: #858585; background-color: #F0F2F5; font-weight: 500;" density="comfortable" variant="text">
              {{ remote }}
            </v-chip>
          </div>
          <div title="찜하기">
            <button
            @click.stop="likesavingProduct"
              :class="{ liked: savingProduct.liked }"
            >
              {{ savingProduct.liked ? '💗' : '🤍' }}
            </button>
            <!-- -----
              혹시 안되면 class 의 liked ""문자열 처리해보기
            ----- -->
          </div>
        </div>
      </div>
    </div>

  </div>

  <v-divider style="margin-left: 20px; margin-right: 20px;" :thickness="1"></v-divider>
</template>


<script setup>
import { useAccountStore } from "@/stores/account";
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { onMounted } from "vue";


const router = useRouter()

// 좋아요를 누르면 좋아요 취소를, 좋아요 취소 누르면 좋아요를 보이도록 하기
const likesavingProduct = () => {
//   router.push({ name: 'cart' })
  props.savingProduct.liked = !props.savingProduct.liked

  if (props.savingProduct.liked) {
    addToSavingCart(props.savingProduct)
    // navigateToCartView()
  }
}

// 좋아요 버튼을 누른 상품(게시글)이 cart에 담기도록 하기
const addToSavingCart = (savingProduct) => {
  const likedsavingProducts = JSON.parse(localStorage.getItem('likedsavingProducts')) || []
  likedsavingProducts.push(savingProduct)
  localStorage.setItem('likedsavingProducts', JSON.stringify(likedsavingProducts))
}

// 좋아요를 누르면 바로 cart로 이동하면서 담긴 상품 표시됨
// const navigateToCartView = () => {
//   router.push({ name: 'cart' })
// }


const item = ref(null);


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