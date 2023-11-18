<template>
  <div>프로필</div>
</template>

<script setup>
import { onMounted } from "vue";
import axios from "axios";
import { useAccountStore } from "@/stores/account";

const store = useAccountStore();

onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/accounts/user/`,
    headers: {
      Authorization: `Token ${store.token.value}`,
    },
  })
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style scoped></style>
