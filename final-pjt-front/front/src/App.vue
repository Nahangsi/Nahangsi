<template>
  <CurrencyCal />

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import CurrencyCal from "@/components/CurrencyCal.vue";
</script>

<style scoped></style>
