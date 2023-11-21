<!-- 게시글 메인 화면을 보여주는 vue -->
<template>
    <div class="community">
        <div class="container">
            <h1 class="header d-flex justify-content-center text-center mt-4">게시판</h1>
            <h4 class="text d-flex justify-content-center text-center mt-4">회원들 간 금융 상품을 소개하고, 의견을 공유하는 소중한 공간입니다.</h4>
            <!-- <div class="d-flex justify-content-end">
                <button class="create-button" @click="CreateView">글 작성</button> -->
            <RouterLink :to="{name:'CreateView'}">[글 작성]</RouterLink>
            <!-- </div> -->
            <ArticleList />
        </div>
    </div>
</template>

<script setup>
// ArticleView 컴포넌트 마운트 될 때 getArticles 함수 실행되도록
// -> 해당 컴포넌트 렌더링 될때 최신 게시글 목록 불러오기 위해
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
// ArticleList 컴포넌트 등록
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
    store.getArticles()
})


</script>

<style scoped>

</style>