<!-- 게시글 메인 화면을 보여주는 vue -->
<template>
    <div class="community">
        <div class="container">
            <v-card
                class="mx-auto"
                width="400"
                prepend-icon="mdi-home"
                color="blue-lighten-1"
                    dark
            >
                <template v-slot:title>
                게시판
                </template>

                <v-card-text>
                    회원들 간 금융 상품을 소개하고, 의견을 공유하는 공간입니다.
                </v-card-text>
            </v-card>
           
                <v-btn variant="outlined" @click="goToCreateView">
                글 작성
                </v-btn>
               </div>
                
            <ArticleList />
        </div>

      <!-- <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn> -->
    

    <v-list lines="two">
      <template v-for="(item, index) in items">
        <v-list-subheader
          v-if="item.header"
          :key="item.header"
          inset
        >
          {{ item.header }}
        </v-list-subheader>

        <v-divider
          v-else-if="item.divider"
          :key="index"
          inset
        ></v-divider>

        <v-list-item
          v-else
          :key="item.title"
          :prepend-avatar="item.avatar"
          ripple
        >
          <template v-slot:title>
            <div v-html="item.title"></div>
          </template>

          <template v-slot:subtitle>
            <div v-html="item.subtitle"></div>
          </template>
        </v-list-item>
      </template>
    </v-list>

</template>

<script setup>
// ArticleView 컴포넌트 마운트 될 때 getArticles 함수 실행되도록
// -> 해당 컴포넌트 렌더링 될때 최신 게시글 목록 불러오기 위해
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { RouterLink,useRouter } from 'vue-router'
// ArticleList 컴포넌트 등록
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()
const router = useRouter();

onMounted(() => {
    store.getArticles()
})

const goToCreateView = () => {
      router.push({ name: 'CreateView' });
    };

</script>

<style scoped>
/* .v-slot {
    text-align: center;
} */
</style>