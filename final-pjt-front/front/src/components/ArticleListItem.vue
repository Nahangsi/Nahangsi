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
            
            <v-divider></v-divider>
        </div>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
import { useRouter } from 'vue-router'


const props = defineProps({
  article: Object
})

const router = useRouter()

const goToDetailView = () => {
      router.push({ name: 'DetailView', params: {id: props.article.id} });
    };

</script>

<style scoped>


</style>