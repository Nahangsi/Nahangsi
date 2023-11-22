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
            <p style="font-size: 14px; font-weight: bolder">
              {{ depositProduct.kor_co_nm }}
            </p>
            <p style="font-size: 14px; font-weight: bolder">
              {{ depositProduct.fin_prdt_nm }}
            </p>
          </div>
          <div
            title="금리"
            style="
              display: flex;
              flex-direction: column;
              flex-wrap: nowrap;
              align-items: flex-end;
              flex-grow: 4;
            "
          >
            <div>
              <p style="font-size: 18px">최고 {{ maxRate2 }} %</p>
            </div>
            <div>
              <p>기본 {{ maxRate1 }} %</p>
            </div>
          </div>
        </div>
        <div
          title="칩+좋아요"
          style="display: flex; justify-content: space-between"
        >
          <div title="칩">
            <v-chip density="comfortable">
              {{ everyone }}
            </v-chip>
            <v-chip density="comfortable">
              {{ remote }}
            </v-chip>
          </div>
          <div title="찜하기">
            <button
              @click="likedepositProduct"
              :class="{ liked: depositProduct.liked }"
            >
              {{ depositProduct.liked ? "좋아요 취소" : "좋아요" }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <v-divider :thickness="1"></v-divider>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import axios from "axios";
import { ref, computed, defineProps } from "vue";
import { useRouter } from "vue-router";
import { onMounted } from "vue";

// 좋아요를 누르면 좋아요 취소를, 좋아요 취소 누르면 좋아요를 보이도록 하기
const likedepositProduct = () => {
  //   router.push({ name: 'cart' })
  props.depositProduct.liked = !props.depositProduct.liked;

  if (props.depositProduct.liked) {
    addToDepositCart(props.depositProduct);
    // navigateToCartView()
  }
};

// 좋아요 버튼을 누른 상품(게시글)이 cart에 담기도록 하기
const addToDepositCart = (depositProduct) => {
  const likedDepositProducts =
    JSON.parse(localStorage.getItem("likedDepositProducts")) || [];
  likedDepositProducts.push(depositProduct);
  localStorage.setItem(
    "likedDepositProducts",
    JSON.stringify(likedDepositProducts)
  );
};

// 좋아요를 누르면 바로 cart로 이동하면서 담긴 상품 표시됨
// const navigateToCartView = () => {
//   router.push({ name: 'cart' })
// }

const router = useRouter();
const props = defineProps({
  depositProduct: Object,
});

const everyone = ref("");
const remote = ref("직접가입");

const maxRate1 = computed(() => {
  return Math.max(
    ...props.depositProduct.depositoptions_set.map((item) => item.intr_rate)
  );
});

const maxRate2 = computed(() => {
  return props.depositProduct.depositoptions_set.reduce((max, currentValue) => {
    if (currentValue.intr_rate2 > max) {
      return currentValue.intr_rate2;
    }
    return max;
  }, 0);
});

if (props.depositProduct.join_deny === 1) {
  everyone.value = "누구나가입";
} else if (props.depositProduct.join_deny === 3) {
  everyone.value = "일부제한";
}
if (
  props.depositProduct.join_way !== undefined &&
  (props.depositProduct.join_way.includes("인터넷") ||
    props.depositProduct.join_way.includes("스마트폰"))
) {
  remote.value = "방문없이가입";
}

const godetail = () => {
  console.log(props.depositProduct);

  router.push({
    name: "productdetail",
    params: { id: props.depositProduct.fin_prdt_cd },
  });
};
</script>

<style scoped>
.icon {
  box-shadow: 1px 2px 8px #cccccc;
}
</style>
