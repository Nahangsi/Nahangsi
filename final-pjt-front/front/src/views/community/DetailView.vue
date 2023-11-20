<template>
  <div class="article-detail">
    <div class="container">
      <h2>상세 정보</h2>
      <p>글 번호 : {{ article?.id }}</p>
      <p>제목 : {{ article?.title }}</p>
      <p>내용 : {{ article?.content }}</p>
      <p>작성일 : {{ formatDate(article?.created_at) }}</p>
      <p>수정일 : {{ formatDate(article?.updated_at) }}</p>
      <button @click="moveUpdate">수정</button>
      <button @click="deleteArticle">삭제</button>
      <hr />
      <form @submit.prevent="createComment">
        <label for="content">댓글 내용 : </label>
        <input type="text" v-model="content" />
        <input type="submit" value="댓글 작성" />
      </form>
      <div v-for="comment in article.comments" :key="comment.id">
        <p>{{ comment.id }} - {{ comment.content }}</p>
        <button @click="deleteComment(comment.id)">댓글 삭제</button>
</div>

    </div>
  </div>
  <!-- <RouterView /> -->
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/account';

const store = useAccountStore();
const route = useRoute();
const router = useRouter();

const article = ref({});
const content = ref("");



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

const createComment = () => {
  
  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);
      // router.push({ name: "DetailView" });
      console.log("댓글이 생성되었습니다.")
      if (article.value && Array.isArray(article.value.comments)) {
        article.value.comments.push(res.data);
        article.value = { ...article.value };
      }
      
      content.value = "";
      console.log(article.value.comment)
    })
    .catch((err) => {
      console.log(err);
    });
};

const deleteComment = (commentId) => {
  axios({
    method: "delete",
    url: `${store.API_URL}/api/v1/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("댓글 삭제 완료");
      router.go();

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
      console.log(res.data);
      article.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style scoped>

</style>
