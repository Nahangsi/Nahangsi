<template>
  <nav>
    <RouterLink :to="{ name: 'CurrencyCal' }">환전</RouterLink>

    <RouterLink :to="{ name: 'depositproduct' }">예금 상품</RouterLink>
    <RouterLink :to="{ name: 'savingproduct' }">적금 상품</RouterLink>

    <div v-if="store.isLogin">
      <p @click="logout">로그아웃</p>
    </div>
    <div v-else>
      <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
      <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
    </div>
  </nav>

  <v-layout class="overflow-visible" style="height: 56px">
    <v-bottom-navigation v-model="value" color="teal" grow>
      <v-btn>
        <v-icon>mdi-history</v-icon>
        <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
      </v-btn>
      <v-btn>
        <v-icon icon="fa:fas fa-lock"></v-icon>
        <RouterLink to="/">Home</RouterLink>
      </v-btn>

      <v-btn>
        <v-icon icon="mdi-map-marker"></v-icon>
        <div @click="logincon">
          <RouterLink :to="{ name: 'mypage' }">Profile</RouterLink>
        </div>
      </v-btn>
    </v-bottom-navigation>
  </v-layout>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useAccountStore } from "@/stores/account";
import { useRouter } from "vue-router";

const store = useAccountStore();
const router = useRouter();
const logout = () => {
  store.logout();
};

const logincon = () => {
  if (store.isLogin === false) {
    alert("로그인시 이용가능합니다");
    router.push({ name: "login" });
  }
};
</script>

<style scoped>
a {
  color: inherit;
  text-decoration: none;
}
</style>
