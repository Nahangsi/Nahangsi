<template>
    <div class="article-list-item">
        <div class="container">
            <div class="article-info">
        <h5 class="id">{{ article.id }}</h5>
        <p class="title">{{ article.title }}</p>
        <p class="content">{{ article.content }}</p>
            </div>
        <RouterLink :to="{ name: 'DetailView', params: {id: article.id}}">
        [DETAIL]
        </RouterLink>
        <div class="additional-info">
            <div class="info-group">
                <p class="comment-count">댓글 수: {{ article.comment_count }}</p>
                <p class="username">작성자: {{ article.username }}</p>
            </div>
        </div>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    article : Object
})
import {RouterLink} from 'vue-router'
</script>

<style scoped>

</style>