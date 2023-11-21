<template>
  <div>

  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { onMounted } from "vue";

const store = useAccountStore()

onMounted(() => {
  axios({
    method: 'get',
    url:
  })
})

</script>

<style scoped>

</style>