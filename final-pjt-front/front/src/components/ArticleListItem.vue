<template>
    <div class="article-list-item">
        <div class="container">
            <div class="article-info">
        <h5 class="id, font-weight-black">{{ article.id }}</h5>
        <p class="title, font-weight-medium">{{ article.title }}</p>
        <p class="content, font-weight-medium">{{ article.content }}</p>
        <!-- <p class="category">{{ article.category }}</p> -->
            </div>
            <v-btn size="small" variant="tonal" @click="goToDetailView">
                상세 보기
            </v-btn>
        <div class="additional-info">
            <div class="info-group">
                <!-- <p class="comment-count">댓글 수: {{ article.comments_count }}</p> -->
                <p class="username">작성자: {{ article.username }}</p>
            </div>
            <!-- 좋아요 버튼 만들기 -->
            <button @click="likeArticle" :class="{ 'liked': article.liked }">
                {{ article.liked ? '좋아요 취소' : '좋아요' }}
            </button>
            <v-divider></v-divider>
        </div>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
  article: Object
})

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

const goToDetailView = () => {
      router.push({ name: 'DetailView', params: {id: props.article.id} });
    };

</script>

<style scoped>


</style>