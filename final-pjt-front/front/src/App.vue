<template>
  <div>  
    <header>
      <nav>
        <!-- ArticleView 컴포넌트로 이동하는 RouterLink 작성 -->
        <RouterLink :to="{name:'ArticleView'}">Articles</RouterLink>
      </nav>
    </header>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>

</style>