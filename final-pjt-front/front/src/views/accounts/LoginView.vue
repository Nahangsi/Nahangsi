<template>
  <div>
    <v-sheet width="300" class="mx-auto">
      <p class="login">Login</p>
      <v-form @submit.prevent="login">
        <v-text-field
          v-model.trim="username"
          label="아이디"
          variant="outlined"
        ></v-text-field>
        <v-text-field
          v-model.trim="password1"
          label="비밀번호"
          type="password"
          hint="비밀번호는 8자리 이상 입력해주세요!"
          variant="outlined"
        ></v-text-field>
        <v-btn
          class="font-weight-black mt-2 submit"
          type="submit"
          block
          variant="text"
          >로그인
          <v-icon icon="$vuetify"></v-icon>
          <v-icon icon="md:home"></v-icon>
          </v-btn>
        <v-btn variant="text" class="footer"> 회원가입 > </v-btn>
        <v-btn variant="text" class="footer"> 비밀번호찾기 > </v-btn>
      </v-form>
    </v-sheet>
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

<style scoped>
.login {
  text-align: center;
  margin-bottom: 25px;
  font-size: 24px;
}
.submit {
  background-color: #1565c0;
  color: whitesmoke;
}
.footer {
  margin-left: 37px;
  color: darkgrey;
  padding: 4px;
}
</style>
