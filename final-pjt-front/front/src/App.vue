<template>
  <div>
    <RouterLink :to="{name : 'CurrencyCal'}">환전</RouterLink> |
    <RouterLink :to="{name : 'DepositView'}">예금</RouterLink> |
    <RouterLink :to="{name : 'SignUpView'}">회원가입</RouterLink>
  </div>


  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";

</script>

<style scoped></style>
