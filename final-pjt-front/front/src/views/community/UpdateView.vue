<template>
    <div>
        <div>
        <h2>게시글 수정</h2>
        <hr class="my-4" />
        <form @submit.prevent="updatePost">
        <div>
            <label for="title">제목:</label>
            <input type="text" id="title" v-model="title" />
        </div>
        <div>
            <label for="content">내용:</label>
            <textarea id="content" v-model="content"></textarea>
        </div>
            <div class="pt-4">
                <button type="submit" class="btn btn-primary" @click="updatePost">수정</button> |

                <button type="button" class="btn btn-outline-danger me-2" @click="goDetailView">취소</button>
            </div>
        </form>
    </div>
    </div>
  </template>
  
  <script setup>
  import axios from "axios";
  import { ref, onMounted } from "vue";
  import { useRoute, useRouter } from 'vue-router';
  import { useAccountStore } from '@/stores/account';

  const store = useAccountStore()
  const route = useRoute();
  const router = useRouter();
  
  const title = ref('');
  const content = ref('');

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
        name: 'DetailView',
        params: {
            id: route.params.id,
        }
      }
    )}
    
    onMounted(() => {
    axios({
        method: 'get',
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
  
  <style scoped>
  
  </style>
