<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model="title" placeholder="제목을 입력하세요" />
      <input type="text" v-model="content" placeholder="내용을 입력하세요" />
      <button type="submit">생성</button>
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import {ref} from "vue";
import {useCounterStore} from "@/stores/counter";
import {useAccountStore} from "@/stores/account";

const store = useCounterStore();
const store2 = useAccountStore();
const title = ref("");
const content = ref("");

const createArticle = () => {
  axios({
        method: "post",
        url: `${store.API_URL}/api/v1/articles/`,
        data: {
          title: title.value,
          content: content.value,
        },
        headers: {
          Authorization: `Token ${store2.token}`,
      },
      })
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
};

</script>

<style scoped>

</style>