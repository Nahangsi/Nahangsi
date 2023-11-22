<template>
  <v-container>
    <v-row>
      <!-- Avatar Column -->
      <v-col cols="3" md="3">
        <v-avatar class="icon" :size="60">
          <v-img src="src/assets/gom.png" />
        </v-avatar>
      </v-col>

      <!-- Text Content Column -->
      <v-col cols="9" md="9">
        <h2>안녕하세요 {{ User.username }}님</h2>
        <h4>재정 보충이 필요한 상태입니다 :)</h4>
      </v-col>
    </v-row>
  </v-container>

  <v-divider></v-divider>

  <v-container>
    <v-btn class="my-btn" :to="{ name: 'mypageupdate' }">정보수정</v-btn>
    <v-btn class="my-btn" :to="{ name: 'mypagepasswordupdate' }"
      >비밀번호 변경</v-btn
    >
    <v-btn class="my-btn" :to="{ name: 'mypageendmembership' }">탈퇴하기</v-btn>
  </v-container>

  <v-container>
    <v-row>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>My Profile 🙏</v-card-title>
          <v-card-text>
            <v-list-item>
              <v-list-item-content>이름 : </v-list-item-content>
              <v-list-item-content>{{ User.username }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>저축 목표 : </v-list-item-content>
              <v-list-item-content>{{ User.savings_goal }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>가입 상품 : </v-list-item-content>
              <v-list-item-content v-if="product">{{
                product
              }}</v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>시드 머니 :</v-list-item-content>
              <v-list-item-content>{{ User.money }}</v-list-item-content>
            </v-list-item>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

  <!-- 내가 찜한 목록, 캘린더, 은행찾기, 환전 -->

  <!-- 만들어지면 vue component 넣기 -->
  <v-container class="text-center" style="margin-bottom: 50px">
    <v-row justify="center">
      <v-col cols="12">
        <v-btn block rounded="xl" size="x-large" class="text-left"
          >내가 찜한 상품</v-btn
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-btn block rounded="xl" size="x-large" class="text-left"
          ><RouterLink class="none" :to="{ name: 'CurrencyCal' }"
            >환전</RouterLink
          ></v-btn
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-btn block rounded="xl" size="x-large" class="text-left"
          ><RouterLink class="none" :to="{ name: 'Bank' }"
            >은행찾기</RouterLink
          ></v-btn
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <!-- <v-btn block rounded="xl" size="x-large" class="text-left"><RouterLink class="none" :to="{name : 'calendar'}">캘린더</RouterLink></v-btn> -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import { RouterLink } from "vue-router";

import { ref } from "vue";

const store = useAccountStore();
const User = store.userinfo;
const product = ref(null);
if (User.financial_products !== null) {
  product.value = User.financial_products.substring(
    1,
    User.financial_products.length - 1
  );
}
</script>

<style scoped>
.icon {
  box-shadow: 1px 2px 8px #cccccc;
}

.my-btn {
  margin: 6px;
}

.none {
  text-decoration: none;
  color: darkgrey;
}

.text-left {
  text-align: left;
  text-decoration: none;
  color: darkgrey;
}
</style>
