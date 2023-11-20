<template>
  <div>
    <v-sheet width="300" class="mx-auto">
      <v-form @submit.prevent="passwordupdate">
        <v-text-field label="이전 비밀번호" variant="underlined" v-model="oldPassword" :rules="rules"></v-text-field>
        <v-text-field label="변경할 비밀번호" variant="underlined" v-model="newPassword" :rules="rules"></v-text-field>
        <v-btn type="submit" block class="mt-2" variant="outlined"
          >비밀번호 변경하기</v-btn>

      </v-form>
    </v-sheet>

  </div>
</template>


<script>
// 여기는 유효성 검사 하는 곳
// 아이디 검사
export default {
  data() {
    return {
      username: "",
      rules: [
        (value) => {
          if (value) return true;
          return "비밀번호 입력란이 비어있습니다!";
        },
      ],
    };
  },
};
</script>

<script setup>
import { useAccountStore } from "@/stores/account";
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";

const store = useAccountStore()
const router = useRouter()

const oldPassword = ref(null)
const newPassword = ref(null)


const passwordupdate = () => {
  if (oldPassword.value !== null && newPassword !== null) {
    axios({
    method: "post",
    url: `${store.API_URL}/accounts/change_password/`,
    data : { old_password: oldPassword.value, new_password: newPassword.value
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then((res) => {
    alert("회원정보가 수정되었습니다!");
    store.Getuserinfo()
    router.push({name: "mypage"});
  })
  .catch((err) => {
    console.log(err);
    alert("회원정보 수정에 실패했습니다. 다시 시도해주세요!");
    router.push({name: "mypage"});
  });

  } else {
    alert("비밀번호 입력란이 비어있습니다. 확인해주세요!")
  }


}


</script>

<style scoped>

</style>