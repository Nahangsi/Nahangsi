<template>
  <div>
    <v-avatar class="icon" image="https://item.kakaocdn.net/do/9fc0462374fa73111ee6b47046b9ce7b8b566dca82634c93f811198148a26065" size="40"></v-avatar>
    {{ depositProduct.kor_co_nm }}
    {{ depositProduct.fin_prdt_nm }}
    <h3>기본 {{ maxRate1 }} %</h3>
    <p>최고 {{ maxRate2 }} %</p>
    <v-chip>
      {{  everyone}}
</v-chip>
<v-chip>
  {{ remote }}
</v-chip>
<button @click="likeArticle" :class="{ 'liked': article.liked }">
                {{ article.liked ? '좋아요 취소' : '좋아요' }}
</button>
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

// 좋아요를 누르면 좋아요 취소를, 좋아요 취소 누르면 좋아요를 보이도록 하기
const likeArticle = () => {
//   router.push({ name: 'cart' })
  props.article.liked = !props.article.liked

  if (props.article.liked) {
    addToCart(props.article)
    // navigateToCartView()
  }
}

// 좋아요 버튼을 누른 상품(게시글)이 cart에 담기도록 하기
const addToCart = (article) => {
  const likedArticles = JSON.parse(localStorage.getItem('likedArticles')) || []
  likedArticles.push(article)
  localStorage.setItem('likedArticles', JSON.stringify(likedArticles))
}

// 좋아요를 누르면 바로 cart로 이동하면서 담긴 상품 표시됨
// const navigateToCartView = () => {
//   router.push({ name: 'cart' })
// }



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
    

</script>

<style scoped>
.icon {
  box-shadow: 1px 2px 8px #cccccc;
}

</style>