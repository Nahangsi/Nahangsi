<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <div v-if="store.isLogin">
      <RouterLink :to="{ name: 'profile' }">프로필</RouterLink>
      <p @click="logout">로그아웃</p>
    </div>
    <div v-else>
      <RouterLink :to="{name : 'CurrencyCal'}">환전</RouterLink> |
      <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
      <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
      <RouterLink :to="{name:'ArticleView'}">Articles</RouterLink>
    </div>
  </nav>

  <RouterView />
</template>

<script setup>

import { RouterLink, RouterView } from "vue-router";
import { useAccountStore } from "@/stores/account";

const store = useAccountStore();
const logout = () => {
  store.logout();
  console.log(store.isLogin);
};
</script>

<style scoped></style>
