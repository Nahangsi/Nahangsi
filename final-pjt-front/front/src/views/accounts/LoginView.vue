<template>
  <div>
    <div>
      <h1>로그인</h1>
      <v-sheet width="300" class="mx-auto">
        <v-form @submit.prevent="login">
          <v-text-field
            v-model.trim="username"
            label="First name"
            variant="outlined"
          ></v-text-field>
          <v-text-field
            v-model.trim="password1"
            label="Password"
            type="password"
            hint="Enter your password to access this website"
            variant="outlined"
          ></v-text-field>
          <v-btn type="submit" block class="mt-2" variant="outlined"
            >Submit</v-btn
          >
        </v-form>
      </v-sheet>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAccountStore } from "@/stores/account";

const store = useAccountStore();
const username = ref(null);
const password1 = ref(null);

const login = () => {
  const payload = {
    username: username.value,
    password: password1.value,
  };
  store.login(payload);
};
</script>

<style scoped></style>
