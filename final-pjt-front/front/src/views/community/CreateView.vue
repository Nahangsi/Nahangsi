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
import { useAccountStore } from "@/stores/account";
import { ref } from "vue";
import { useRouter } from "vue-router";

const title = ref(null);
const content = ref(null);
const category = ref(null);

const store = useAccountStore();
const router = useRouter();

const createArticle = () => {
  if (!title.value) {
    alert("제목을 입력해주세요");
    return;
  } else if (!content.value) {
    alert("내용을 입력해주세요");
    return;
  } else if (!category.value) {
    alert("카테고리를 지정해주세요");
  }

  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value,
      category: category.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.push({ name: "ArticleView" });

    })
    .catch((err) => {
      console.log(err);
    });
};

// export default {
//   name: "CreateView",
//   data() {
//     return {
//       title: null,
//       content: null,
//       category: null,
//     };
//   },
//   methods: {
//     createArticle() {
//       const title = this.title;
//       const content = this.content;
//       const category = this.category;

//       if (!title) {
//         alert("제목을 입력해주세요");
//         return;
//       } else if (!content) {
//         alert("내용을 입력해주세요");
//         return;
//       } else if (!category) {
//         alert("카테고리를 지정해주세요");
//       }
//       axios({
//         method: "POST",
//         url: `${store.API_URL}/api/v1/articles/`,
//         data: { title, content, category },
//         headers: {
//           Authorization: `Token ${store.token.value}`,
//         },
//       })
//         .then((res) => {
//           this.$router.push({ name: "ArticleView" });
//         })
//         .catch((err) => {
//           console.log(err);
//         });
//     },
//   },
// };

</script>

<style scoped>

</style>