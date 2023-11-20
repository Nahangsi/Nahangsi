<!-- 단일 게시글 데이터 출력 vue -->
<template>
    <div class="article-detail">
        <div class="container">
            <h2>상세 정보</h2> 
                <!-- <div v-if="article"> -->
                    <p>글 번호 : {{ article?.id }}</p>
                    <p>제목 : {{  article?.title }}</p>
                    <p>내용 : {{  article?.content }}</p>
                    <p>작성일 : {{ formatDate(article?.created_at) }}</p>
                    <p>수정일 : {{ formatDate(article?.updated_at) }}</p>
                    <!-- <div class="button-group"> -->
                        <!-- <RouterLink :to="{name:'UpdateView'}">[수정]</RouterLink> -->
                        <button @click="moveUpdate">수정</button>
                        <button @click="deleteArticle">삭제</button>
                    <!-- </div> -->
                <!-- </div> -->
        </div>
    </div>
    <RouterView />

</template>


<script setup>
// DeatilView 마운트 될 때 특정 게시글 조회하는 AJAX 요청 진행
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account';

const store = useAccountStore()
const route = useRoute()
const router = useRouter();
// 응답 데이터 출력
const article = ref({})


const moveUpdate = () => {
  router.push({ name: "UpdateView", params: { id: article.value.id } });
};

const deleteArticle = () => {
  axios({
    method: "delete",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
            Authorization: `Token ${store.token}`,
        },
  })
    .then((res) => {
      console.log("삭제 완료");
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.log(err);
    });
    
};

const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('ko-KR', options);
};

onMounted(() => {
    axios({
      method: 'GET',
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    })
    .then((res) => {
        // 응답 데이터 저장
        console.log(res.data)
        article.value = res.data
    })
    .catch((err) => { 
        console.log(err)
    })
})
</script>

    

<style scoped>

</style>