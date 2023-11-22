<template>
  <div>
    <v-avatar class="icon" image="https://item.kakaocdn.net/do/9fc0462374fa73111ee6b47046b9ce7b8b566dca82634c93f811198148a26065" size="60"></v-avatar>
    {{ User.username }}
    메인프로필 수정중
    <RouterLink :to="{ name: 'mypageupdate' }">정보수정</RouterLink>
    <RouterLink :to="{ name: 'mypagepasswordupdate' }">비밀번호 변경</RouterLink>
    <RouterLink :to="{ name: 'mypageendmembership' }">탈퇴하기</RouterLink>
    
  </div>
  <ProfileView/>
</template>

<script setup>
import ProfileView from '../accounts/ProfileView.vue';
import { useAccountStore } from "@/stores/account";


const store = useAccountStore()

const User = store.userinfo

</script>

<style scoped>

.icon {
  box-shadow: 1px 2px 8px #cccccc;
}

</style>