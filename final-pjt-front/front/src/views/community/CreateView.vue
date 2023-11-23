<template>
  <div style="background-color: #F6F7F9; height: 1000px;" >
    <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card style="margin: 10px; height: 800px; display: flex; flex-direction: column; ">
          <v-card-title style="text-align: center;" >
            <p style="font-size: 24px; font-weight: 600; margin-top: 60px;">게시글 작성</p>
          </v-card-title>
          <v-form style="margin: 20px; text-align: center; "  @submit.prevent="createArticle">
            <v-text-field
              v-model.trim="title"
              label="제목"
              required
              clearable variant="underlined"
            ></v-text-field>

            <v-textarea
              v-model="content"
              label="내용"
              rows="5"
              required
              clearable variant="underlined"
            ></v-textarea>

            <v-select
            variant="outlined"
              v-model="category"
              label="카테고리"
              :items="['예금', '적금', '기타']"
              required
            ></v-select>

            <v-btn block type="submit" color="#1E88E5">작성 완료</v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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