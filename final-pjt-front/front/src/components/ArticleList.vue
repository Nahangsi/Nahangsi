<template>
    <div>
        <h4>게시글 목록</h4>
        <!-- 게시글 목록 출력, store의 articles 데이터 참조 -->
        <!-- , v-for 활용해 article 단위 객체 정보 props로 전달 -->
        <hr>
        <ArticleListItem
            v-for="article in store.articles"
            :key="article.id"
            :article="article"
            
        />
        
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import ArticleListItem from '@/components/ArticleListItem.vue';

const store = useCounterStore()
</script>

<style scoped>

</style>