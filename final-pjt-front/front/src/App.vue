<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink :to="{ name: 'CurrencyCal' }">환전</RouterLink>
    <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
    <div v-if="store.isLogin">
      <RouterLink :to="{ name: 'mypage' }">Mypage</RouterLink>
      <p @click="logout">로그아웃</p>
    </div>
    <div v-else>
      <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
      <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
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
};
</script>

<style scoped></style>
