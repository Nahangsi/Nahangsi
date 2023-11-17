<template>
  <div>
    <h1>회원가입</h1>
    <form>
      <input type="text" placeholder="사용할 아이디를 입력해주세요." >
      <input type="email" name="" id="" placeholder="이메일을 입력해주세요 (선택사항)">
      <input type="password" placeholder="비밀번호">
      <input type="password" placeholder="비밀번호 확인">
      <p>아래는 선택사항입니다!</p>
      <p>하지만, 선택을 해주신다면 알맞은 금융 상품을 추천해드릴게요!</p>
      <input type="text" placeholder="나이">
      <input type="text" placeholder="연봉">
      <input type="text" placeholder="자산">
      <select name="직종" id="직종">현재 가입하신 금융상품</select>
      <select name="" id="">주 거래은행</select>
      <select name="" id="">저축 목표</select>
      <select name="" id="">직종</select>
      <v-autocomplete
  chips
  label="Autocomplete"
  :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
  multiple
  variant="outlined"
></v-autocomplete>


    </form>
    money = models.IntegerField(blank=True, null=True) # 연봉
    salary = models.IntegerField(blank=True, null=True) # 자산
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True) # 가입 상품
    primary_bank = models.CharField(blank=True, max_length=50, null=True) # 주 거래은행
    savings_goal = models.CharField(blank=True, max_length=50, null=True) # 저축 목표
    occupation = models.CharField(blank=True, max_length=50, null=True) # 직종

  </div>
  
  <v-sheet width="300" class="mx-auto">
    <v-form fast-fail @submit.prevent>
      <v-text-field
        v-model="firstName"
        label="First name"
        :rules="firstNameRules"
      ></v-text-field>

      <v-text-field
        v-model="lastName"
        label="Last name"
        :rules="lastNameRules"

        
      ></v-text-field>

      <v-btn type="submit" block class="mt-2">Submit</v-btn>
    </v-form>
  </v-sheet>
  <p>{{ lastName }}</p>


</template>

<script setup>

import { ref } from 'vue';

const lastName = ref(null)



</script>

<script>
// 여기는 유효성 검사 하는 곳
export default {
    data: () => ({
      firstName: '',
      firstNameRules: [
        value => {
          if (value?.length > 3) return true

          return 'First name must be at least 3 characters.'
        },
      ],
      lastName: '123',
      lastNameRules: [
        value => {
          if (/[^0-9]/.test(value)) return true

          return 'Last name can not contain digits.'
        },
      ],
    }),
  }
</script>

<style  scoped>


</style>