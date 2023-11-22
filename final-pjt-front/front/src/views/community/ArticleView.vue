<template>
  <div>
    <h2>자유게시판</h2>
    <p>*회원들 간 금융 상품을 소개하고, 소중한 의견을 공유하는 공간입니다.</p> 

    <v-container>
      
  
    <v-toolbar
      color="white-lighten-1"
      dark
      height="30" 
      style="border-radius: 10px; max-width: 300px;" 
      class="mx-auto"
    >
      

      <v-toolbar-title></v-toolbar-title>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>
    
      
      <p>  </p>

      <v-row>
        <v-col class="text-right "> 
          <v-btn 
          variant="outlined" 
          @click="goToCreateView"
          height="30" 
          style="border-radius: 5px; max-width: 50px;"
          >
            글쓰기
          </v-btn>
        </v-col>
      </v-row>
  
      <ArticleList />

    </v-container>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { RouterLink, useRouter } from 'vue-router'
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
/* Adjust the styles based on your design preferences */
v-container {
  margin-top: 20px;
}

h2 {
  text-align: center;
  font-size: 24px;
  margin-bottom: 15px;
}

p {
  text-align: center;
  font-size: 11px;
  margin-bottom: 15px;
}

.text-right {
  text-align: right;
}

v-btn {
  margin-bottom: 50px;

}
</style>
