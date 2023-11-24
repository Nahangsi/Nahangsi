<template>
  <div style="height: 1000px; text-align: center">
    <v-container>
      <v-row style="margin-top: 40px">
        <v-col>
          <p style="font-size: 24px; font-weight: 600; margin-top: 60px">
            게시글 수정
          </p>

          <v-form @submit.prevent="updatePost">
            <v-row>
              <v-col style="margin-top: 40px">
                <v-text-field
                  clearable
                  variant="underlined"
                  v-model="title"
                  label="제목"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-textarea
                  clearable
                  variant="underlined"
                  v-model="content"
                  label="내용"
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                style="
                  display: flex;
                  justify-content: space-between;
                  padding-top: 0px;
                "
              >
                <v-btn type="submit" color="#1E88E5" @click="updatePost"
                  >수정</v-btn
                >
                <v-btn
                  type="button"
                  color="#F6F7F9"
                  class="me-2"
                  @click="goDetailView"
                  >취소</v-btn
                >
              </v-col>
            </v-row>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";

const store = useAccountStore();
const route = useRoute();
const router = useRouter();

const title = ref("");
const content = ref("");

// 게시글 수정 페이지에서 게시글 수정하기
const updatePost = () => {
  axios({
    method: "put",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);
      router.push({ name: "DetailView", params: { id: route.params.id } });
    })
    .catch((err) => {
      console.log(err);
    });
};

// 수정하고 나면 게시글 상세페이지로 이동함
const goDetailView = () => {
  router.push({
    name: "DetailView",
    params: {
      id: route.params.id,
    },
  });
};

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      title.value = res.data.title;
      content.value = res.data.content;
    })
    .catch((err) => {
      console.log(err);
    });
});

// axios({
//   method: "post",
//   url: `${store.API_URL}/api/v1/articles/`,
//   data: {
//     title: title.value,
//     content: content.value,
//     category: category.value,
//   },
//   headers: {
//     Authorization: `Token ${store.token}`,
//   },
//   })
//   .then((res) => {
//     router.push({ name: "DetailView" });
//   })
//   .catch((err) => {
//     console.log(err);
//   });
</script>

<style scoped></style>
