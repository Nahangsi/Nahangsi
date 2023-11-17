<template>
  <ExchangeRateCal />

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import ExchangeRateCal from "@/components/ExchangeRateCal.vue";
</script>

<style scoped></style>
