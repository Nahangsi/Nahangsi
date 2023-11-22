<template>
  <div>
    <h1>회원 정보 수정</h1>
    <v-sheet width="300" class="mx-auto">
      <v-form @submit.prevent="updateinfo">
        <label for="">아이디</label>
        <v-text-field
          v-model.trim="username"
          variant="outlined"
          disabled
        ></v-text-field>

        <label for="">이메일</label>
        <v-text-field
          v-model.trim="email"
          type="email"
          variant="outlined"
        ></v-text-field>
        연령대
        <v-autocomplete
          v-model="age"
          :items="['10대', '20대', '30대', '40대', '50대', '60대 이상']"
          variant="outlined"
        ></v-autocomplete>
        가입한 금융 상품
        <v-combobox
          v-model="financialProducts"
          :items="items"
          multiple
          variant="outlined"
        ></v-combobox>
        월별 저축 금액
        <v-combobox
          v-model="money"
          :items="moneyItems"
          variant="outlined"
        ></v-combobox>
        연봉
        <v-combobox
          v-model="salary"
          :items="salaryItems"
          variant="outlined"
        ></v-combobox>
        주 거래은행
        <v-combobox
          v-model="primaryBank"
          :items="primaryBankItems"
          variant="outlined"
        ></v-combobox>
        저축 목표
        <v-combobox
          v-model="savingsGoal"
          :items="savingsGoalItmes"
          variant="outlined"
        ></v-combobox>
        저축 기간
        <v-combobox
          v-model="savingsTerm"
          :items="savingsTermItmes"
          variant="outlined"
        ></v-combobox>
        직종
        <v-combobox
          v-model="occupation"
          :items="occupationItmes"
          variant="outlined"
        ></v-combobox>
        <v-btn type="submit" block class="mt-2" variant="outlined"
          >수정완료</v-btn
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

const User = store.userinfo;

const username = ref(User.username);
const email = ref(User.email);
const age = ref(User.age + "대");
const money = ref(User.money + "만원 이상");
const salary = ref(User.salary + "이상");
const financialProducts = ref(User.financial_products);
const primaryBank = ref(User.primary_bank);
const occupation = ref(User.occupation);
const savingsGoal = ref(User.savings_goal);
const savingsTerm = ref(User.savings_term + "개월");

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
const savingsTermItmes = ["6개월", "12개월", "24개월", "36개월"];

const updateinfo = () => {
  const payload = {};

  if (email.value !== null && email.value !== "") {
    payload.email = email.value;
  }
  if (age.value !== null && age.value !== "") {
    payload.age = Number(age.value.slice(0, 2));
  }
  if (money.value !== null && money.value !== "") {
    payload.money = parseInt(money.value.slice(0, 3));
  }
  if (salary.value !== null && salary.value !== "") {
    payload.salary = Number(salary.value.slice(0, 4));
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
  if (savingsTerm.value !== null && savingsTerm.value !== "") {
    payload.savings_term = parseInt(savingsTerm.value);
  }

  axios({
    method: "put",
    url: `${store.API_URL}/accounts/user_detail/`,
    data: {
      email: payload.email,
      age: payload.age,
      money: payload.money,
      salary: payload.salary,
      financial_products: payload.financial_products,
      primary_bank: payload.primary_bank,
      occupation: payload.occupation,
      savings_goal: payload.savings_goal,
      savings_term: payload.savings_term,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      alert("회원정보가 수정되었습니다!");
      store.Getuserinfo();
      router.push({ name: "mypage" });
    })
    .catch((err) => {
      console.log(err);
      alert("회원정보 수정에 실패했습니다. 다시 시도해주세요!");
      router.push({ name: "mypage" });
    });
};
</script>

<style scoped></style>
