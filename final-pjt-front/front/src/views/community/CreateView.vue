<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>
            <h2 class="text-h5">게시글 작성</h2>
          </v-card-title>
          <v-form @submit.prevent="createArticle">
            <v-text-field
              v-model.trim="title"
              label="제목"
              required
            ></v-text-field>

            <v-textarea
              v-model="content"
              label="내용"
              rows="5"
              required
            ></v-textarea>

            <v-select
              v-model="category"
              label="카테고리"
              :items="['예금', '적금', '기타']"
              required
            ></v-select>

            <v-btn type="submit" color="primary">작성 완료</v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import axios from "axios";
import { useAccountStore } from "@/stores/account";
import { ref } from "vue";
import { useRouter } from "vue-router";

const title = ref(null);
const content = ref(null);
const category = ref(null);
const user_id = 2;

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

<style></style>