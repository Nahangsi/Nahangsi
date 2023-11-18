<template>

  <div>
    <RouterLink :to="{name : 'CurrencyCal'}">환전</RouterLink> |
    <RouterLink :to="{name : 'SignUpView'}">회원가입</RouterLink> |
    <RouterLink :to="{name : 'BankMapView'}">가까운 은행 찾기</RouterLink> |
  </div>



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

import { RouterLink, RouterView } from "vue-router";

</script>


<style scoped>

</style>

