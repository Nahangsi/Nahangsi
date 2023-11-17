<template>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink :to="{name:'signup'}">회원가입</RouterLink>
      </nav>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>
