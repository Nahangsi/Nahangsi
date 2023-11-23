<template>
    <v-list lines="two">
      <v-list-item>
        <v-list-item-avatar>
          <span class="font-weight-black">{{ formatDate(article.created_at) }}</span>
        </v-list-item-avatar>
  
        <v-list-item-content>
          <v-list-item-title class="mb-1">{{ article.title }}</v-list-item-title>
          <v-list-item-subtitle class="mt-1">{{ article.content }}</v-list-item-subtitle>
  
          <v-divider class="mb-2"></v-divider>
  
          <v-btn size="small" variant="tonal" @click="goToDetailView">
            상세 보기
          </v-btn>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </template>

<script setup>
import { defineProps } from 'vue'
import { useRouter } from 'vue-router'


const props = defineProps({
  article: Object
})

const router = useRouter()

const goToDetailView = () => {
      router.push({ name: 'DetailView', params: {id: props.article.id} });
    };


    const formatDate = (dateString) => {
    const options = { month: '2-digit', day: '2-digit', year: '2-digit' };
    return new Date(dateString).toLocaleDateString('ko-KR', options);
};


</script>

<style scoped>
.mb-1 {
  margin-bottom: 2rem; 
}
.mt-1 {
  margin-top: 2rem;
  margin-bottom: 0.5rem; 
}

.mb-2 {
  margin-bottom: 0.5rem;
}
</style>