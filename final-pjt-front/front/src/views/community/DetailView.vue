<!-- 단일 게시글 데이터 출력 vue -->
<template>
    <div class="article-detail">
        <div class="container">
            <h2>상세 정보</h2> 
                <div v-if="article">
                    <p>글 번호 : {{ article.id }}</p>
                    <p>제목 : {{  article.title }}</p>
                    <p>내용 : {{  article.content }}</p>
                    <p>작성시간 : {{ article.created_at }}</p>
                    <p>수정시간 : {{ article.updated_at  }}</p>
                    <div class="button-group">
                        <button class="btn btn-light" @click="editArticle">수정</button>
                        <button class="btn btn-light" @click="deleteArticle">삭제</button>
                    </div>
                </div>
        </div>
    </div>
</template>


<script setup>
// DeatilView 마운트 될 때 특정 게시글 조회하는 AJAX 요청 진행
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const route = useRoute()
// 응답 데이터 출력
const article = ref(null)

onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    })
    .then(res=> {
        // 응답 데이터 저장
      article.value = res.data
    })
    .catch(err => console.log(err))
})
</script>

    

<style scoped>

</style>