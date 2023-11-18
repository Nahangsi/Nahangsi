<template>
  <div>
    <RouterLink :to="{name : 'CurrencyCal'}">환전</RouterLink> |
    <RouterLink :to="{name : 'SignUpView'}">회원가입</RouterLink> |
    <RouterLink :to="{name : 'BankMapView'}">가까운 은행 찾기</RouterLink> |
  </div>


  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";

</script>

<style scoped></style>
