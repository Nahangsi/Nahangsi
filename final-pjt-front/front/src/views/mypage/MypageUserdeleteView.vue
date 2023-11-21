<template>
  <div>
    <div>탈퇴하기 전에 확인해주세세요</div>
    나중에 여기 는 주의사항 같은거 써놓을거에요
    <v-sheet width="300" class="mx-auto">
      <v-form @submit.prevent="userdelete">
        <v-text-field
          label="이전 비밀번호"
          variant="underlined"
          v-model="password"
          type="password"
        ></v-text-field>

        <v-btn type="submit" block class="mt-2" variant="outlined"
          >탈퇴하기</v-btn
        >
      </v-form>
    </v-sheet>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";

const store = useAccountStore();
const router = useRouter();

const password = ref(null);

const userdelete = () => {
  axios({
    method: "post",
    url: `${store.API_URL}/accounts/user_delete/`,
    data: { password1: password.value },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      localStorage.removeItem("account");
      store.token = null;
      alert("회원탈퇴하셨습니다 이용해주셔서 감사합니다");
      router.push("/");
    })
    .catch((err) => {
      alert("오류로 인하여 회원탈퇴에 실패하였습니다 다시 시도해주세요!");
      router.push({ name: "mypage" });
    });
};
</script>

<style scoped></style>
