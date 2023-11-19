<template>
    <div>
      <h1>회원가입</h1>
      <v-sheet width="300" class="mx-auto">
        <v-form @submit.prevent="signup">
          <v-text-field
            v-model.trim="username"
            :rules="rules"
            label="First name"
            variant="outlined"
          ></v-text-field>
          <v-text-field
            v-model.trim="email"
            hide-details="auto"
            label="Email address"
            placeholder="johndoe@gmail.com"
            type="email"
            hint="이메일은 선택사항이에요"
            variant="outlined"
          ></v-text-field>
          <v-text-field
            v-model.trim="password1"
            label="Password"
            type="password"
            hint="Enter your password to access this website"
            variant="outlined"
          ></v-text-field>
          <v-text-field
            v-model.trim="password2"
            label="Password"
            type="password"
            hint="Enter your password to access this website"
            variant="outlined"
          ></v-text-field>
          <p>아래는 선택사항입니다!</p>
          <p>하지만, 선택을 해주신다면 알맞은 금융 상품을 추천해드릴게요!</p>
          <v-autocomplete
            label="연령대"
            v-model="age"
            :items="['10대', '20대', '30대', '40대', '50대', '60대 이상']"
            variant="outlined"
          ></v-autocomplete>
          <v-combobox
            v-model="financialProducts"
            :items="items"
            label="가입 중인 금융상품을 선택해주세요!"
            multiple
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="money"
            :items="moneyItems"
            label="월 저축 금액을 알려주세요!!"
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="salary"
            :items="salaryItems"
            label="연봉을 선택해주세요!!"
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="primaryBank"
            :items="primaryBankItems"
            label="주거래은행을 선택해주세요!!"
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="savingsGoal"
            :items="savingsGoalItmes"
            label="저축목표를 선택해주세요!!"
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="occupation"
            :items="occupationItmes"
            label="직종을 선택해주세요!!"
            variant="outlined"
          ></v-combobox>
          <v-btn type="submit" block class="mt-2" variant="outlined"
            >Submit</v-btn
          >
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
            return "You must enter a first name.";
          },
        ],
      };
    },
  };
  </script>
  
  <script setup>
  import { ref } from "vue";
  import { useAccountStore } from "@/stores/account";
  
  const store = useAccountStore();
  
  const username = ref(null);
  const email = ref(null);
  const password1 = ref(null);
  const password2 = ref(null);
  const age = ref(null);
  const money = ref(null);
  const salary = ref(null);
  const financialProducts = ref(null);
  const primaryBank = ref(null);
  const occupation = ref(null);
  const savingsGoal = ref(null);
  
  const items = ["Programming", "Design", "Vue", "Vuetify"];
  const salaryItems = [
    "2000이상 ~ 4000미만",
    "4000이상 ~ 6000미만",
    "6000이상 ~ 8000미만",
    "8000이상 ~ 1억미만",
  ];
  const moneyItems = [
    "50만원 미만",
    "50만원 이상 ~ 100만원 미만",
    "100만원 이상 ~ 300만원 미만",
    "300만원 이상 ~ 500만원 미만",
    "500만원 이상",
  ];
  const primaryBankItems = [
    "한국은행",
    "수출입은행",
    "KDB산업은행",
    "IBK기업은행",
    "Sh수협은행",
    "NH농협은행",
    "KB국민은행",
    "신한은행",
    "우리은행",
    "KEB하나은행",
    "부산은행",
    "경남은행",
    "대구은행",
    "광주은행",
    "전북은행",
    "제주은행",
    "SC제일은행",
    "씨티은행",
    "카카오뱅크",
    "케이뱅크",
    "토스뱅크",
  ];
  const savingsGoalItmes = [
    "결혼 자금",
    "부동산",
    "은퇴 준비",
    "목돈 마련",
    "여행 경비",
  ];
  const occupationItmes = [
    "홈 프로텍터",
    "전업 주부",
    "프리랜서",
    "직장인",
    "학생",
  ];
  const signup = function () {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
    };
  
    if (email.value !== null && email.value !== "") {
      payload.email = email.value;
    }
    if (age.value !== null && age.value !== "") {
      payload.age = Number(age.value.slice(0, 2));
    }
    if (money.value !== null && money.value !== "") {
      payload.money = parseInt(money.value.slice(0, 3));
      console.log(payload.money);
    }
    if (salary.value !== null && salary.value !== "") {
      payload.salary = Number(salary.value.slice(0, 3));
    }
    if (financialProducts.value !== null && financialProducts.value !== "") {
      payload.financial_products = financialProducts.value;
    }
    if (primaryBank.value !== null && primaryBank.value !== "") {
      payload.primary_bank = primaryBank.value;
    }
    if (occupation.value !== null && occupation.value !== "") {
      payload.occupation = occupation.value;
    }
    if (savingsGoal.value !== null && savingsGoal.value !== "") {
      payload.savings_goal = savingsGoal.value;
    }
  
    store.signup(payload);
  };
  </script>
  
  <style scoped></style>
  