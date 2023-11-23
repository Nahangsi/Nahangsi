<template>
  <div>
    <v-sheet width="300" class="mx-auto">
      <p class="login">Login</p>
      <v-form @submit.prevent="login">
        <v-text-field
          v-model.trim="username"
          label="아이디"
          variant="outlined"
          clearable
        ></v-text-field>
        <v-text-field
          v-model.trim="password1"
          label="비밀번호"
          type="password"
          variant="outlined"
          clearable
        ></v-text-field>
        <v-btn
          class="font-weight-black mt-2 submit"
          type="submit"
          block
          variant="text"
          >로그인
          </v-btn>
        <v-btn variant="text" class="footer"> <RouterLink :to="{ name: 'signup'}" style="color:darkgrey; text-decoration: none;">회원가입 > </RouterLink></v-btn>
        <v-btn variant="text" class="footer"> 비밀번호찾기 > </v-btn>
      </v-form>
    </v-sheet>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAccountStore } from "@/stores/account";
import { useRouter } from 'vue-router'

const router = useRouter()
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

const moverouter = (go) => {
  router.push({name: 'signup'})

}


</script>

<style scoped>
.login {
  margin-top: 50px;
  margin-bottom: 50px;
  text-align: center;
  font-size: 30px;
  font-weight:bolder;
  color: dimgrey;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}
.submit {
  background-color: #1E88E5;
  color: whitesmoke;
}
.footer {
  margin-left: 37px;
  color: darkgrey;
  padding: 4px;
}
</style>
