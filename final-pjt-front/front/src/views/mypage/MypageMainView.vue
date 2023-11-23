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

          

        <p style="font-size: 20px;">안녕하세요 <span style="font-weight: 600; color: #1E88E5;">{{ User.username }}님!</span></p>
        <p style="font-size: 15px; font-weight: 400; color: #959595;">재정 보충이 필요한 상태입니다 :)</p>
      </v-col>
    </v-row>
  </v-container>

  <v-divider></v-divider>

  <v-container style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <div title="윗줄" style="display: flex; justify-content: space-between; margin-top: 20px; margin-bottom: 20px;">

      <v-btn style="display: flex; flex-direction: column; align-items: center; justify-content: center;" variant="text" class="my-btn" :to="{ name: 'mypageupdate' }">
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
          <v-avatar color="surface-variant" rounded="0" :size="60">
          <v-img src="src/assets/infochange.gif" />
        </v-avatar>
        <p>정보수정</p>
        </div>

      </v-btn>
    <v-btn style="display: flex; flex-direction: column; align-items: center; justify-content: center;" variant="text" class="my-btn" :to="{ name: 'mypagepasswordupdate' }"
      >  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <v-avatar color="surface-variant" rounded="0" :size="60">
          <v-img src="src/assets/password_lock.gif" />
        </v-avatar><p>
          비밀번호 변경
        </p>
      </div>      
      </v-btn
    >
    
    <v-btn style="display: flex; flex-direction: column; align-items: center; justify-content: center;" variant="text" class="my-btn" :to="{ name: 'mypagepasswordupdate' }"
      >    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center;"><v-avatar color="surface-variant" rounded="0" :size="60">
          <v-img src="src/assets/zzim.gif" />
        </v-avatar><p>찜한 상품</p></div>    
      </v-btn
    > 
    </div>


    
  </v-container>

  <v-container >
    <v-row>
      <v-col cols="12" md="6">
        <v-card variant="flat" style="background-color: #F6F7F9;">
          <v-card-title>My Profile 🙏</v-card-title>
          <v-card-text>
            <v-list-item>
              <v-list-item-content style="font-size: 16px;" >이름 : </v-list-item-content>
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

  <p style="font-size: 20px; font-weight: 600; margin: 10px;">필요한 기능을 모아봤어요!</p>

  <!-- 내가 찜한 목록, 캘린더, 은행찾기, 환전 -->
  <v-icon icon="mdi-chevron-right"></v-icon>

<v-card height="200">
  <v-divider :thickness="1"></v-divider>
        <v-btn append-icon="mdi-chevron-right" style="font-size: 20px;" variant="text" height="50" @click="selectterm(6)">
          6개월</v-btn>
        <v-divider :thickness="1"></v-divider>
        <v-btn style="font-size: 20px;" variant="text" height="50" @click="selectterm(12)">12개월</v-btn>
        <v-divider :thickness="1"></v-divider>
        <v-btn style="font-size: 20px;" variant="text" height="50" @click="selectterm(24)">24개월</v-btn>
        <v-divider :thickness="1"></v-divider>
        <v-btn style="font-size: 20px;" variant="text" height="50" @click="selectterm(36)">36개월</v-btn>
      </v-card>

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

  <div title="밑줄"  style="display: flex; justify-content: space-between;">
      <v-btn style="display: flex; flex-direction: column; align-items: center; justify-content: center;" variant="text" class="my-btn" :to="{ name: 'CurrencyCal' }"
      >    <div>
        <v-avatar color="surface-variant" rounded="0" :size="60">
          <v-img src="src/assets/change.gif" />
        </v-avatar><p>환율 보기</p>
      </div>   
      </v-btn
    >    
    <v-btn style="display: flex; flex-direction: column; align-items: center; justify-content: center;" variant="text" class="my-btn" :to="{ name: 'Bank' }"
      >   <div><v-avatar color="surface-variant" rounded="0" :size="60">
          <v-img src="src/assets/change.gif" />
        </v-avatar><p>내 주변 은행 찾기</p></div>     
      </v-btn>
      <v-btn style="display: flex; flex-direction: column; align-items: center; justify-content: center;" variant="text" class="my-btn" :to="{ name: 'Bank' }"
      >   <div><v-avatar color="surface-variant" rounded="0" :size="60">
          <v-img src="src/assets/change.gif" />
        </v-avatar><p>내 주변 은행 찾기</p></div>     
      </v-btn>
    </div>
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