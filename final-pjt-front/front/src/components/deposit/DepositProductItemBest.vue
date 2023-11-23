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
          :image= "`src/assets/${depositProduct.kor_co_nm}.png`"
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
              {{ depositProduct.kor_co_nm }}
            </p>
            <p style="font-size: 14px; font-weight: 400">
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
              <p style="font-size: 18px; font-weight: 600; color: #1E88E5;">최고 {{ maxRate2 }} %</p>
            </div>
            <div>
              <p style="font-size: 14px; font-weight: 400; color: #858585;">기본 {{ maxRate1 }} %</p>
            </div>
          </div>
        </div>
        <div
          title="칩+좋아요"
          style="display: flex; justify-content: space-between"
        >
          <div title="칩">
            <v-chip  style="color: #858585; background-color: #F0F2F5; font-weight: 500; margin: 0 5px;" density="comfortable" variant="text">
              {{ everyone }}
            </v-chip>
            <v-chip style="color: #858585; background-color: #F0F2F5; font-weight: 500;" density="comfortable" variant="text">
              {{ remote }}
            </v-chip>
          </div>
          <div title="찜하기">
            <button
              @click.stop="likedepositProduct"
              :class="{ liked: depositProduct.liked }"
            >
              {{ depositProduct.liked ? '💗' : '🤍' }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <v-divider style="margin-left: 20px; margin-right: 20px;" :thickness="1"></v-divider>

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

