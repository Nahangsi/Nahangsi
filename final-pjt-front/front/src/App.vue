<template>
  <v-layout>
    <v-system-bar>
    <v-icon icon="mdi-wifi-strength-4"></v-icon>
    <v-icon icon="mdi-signal" class="ms-2"></v-icon>
    <v-icon icon="mdi-battery" class="ms-2"></v-icon>

    <span class="ms-2">3:13PM</span> 
    </v-system-bar>
  </v-layout>

   <v-card class="nav">
    <v-tabs
      v-model="tab"
      bg-color="blue-darken-1"
    >
      <v-tab value="three"><RouterLink :to="{ name: 'depositproduct' }">예금 상품</RouterLink></v-tab>
      <v-tab value="four"><RouterLink :to="{ name: 'savingproduct' }">적금 상품</RouterLink></v-tab>
      <div v-if="store.isLogin">
        <v-tab value="five"  @click="logout">로그아웃</v-tab>
        <v-tab value="six"><RouterLink :to="{ name : 'mypagepasswordupdate'}">비밀번호변경</RouterLink></v-tab>
      </div>
      <div v-else>
        <v-tab value="five">
          <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
        </v-tab>
        <v-tab value="six">
          <RouterLink :to="{ name: 'signup'}">회원가입</RouterLink>
        </v-tab>
      </div>
    </v-tabs>
  </v-card>

  <nav>
  </nav>

  <v-layout class="overflow-visible" style="height: 56px">
    <v-bottom-navigation v-model="value" color="teal" grow>
      <v-btn>
        <v-icon>mdi-history</v-icon>
        <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
      </v-btn>
      <v-btn>
        <v-icon>mdi-home</v-icon>
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
.nav {margin-top: 25px;}
</style>

