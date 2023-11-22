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
          v-model="savingsTerm"
          :items="savingsTermItmes"
          label="저축기간 선택해주세요!!"
          variant="outlined"
        ></v-combobox>
        <v-combobox
          v-model="occupation"
          :items="occupationItmes"
          label="직종을 선택해주세요!!"
          variant="outlined"
        ></v-combobox>
        <v-btn  type="submit" block class="mt-2 submit" variant="outlined"
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
const savingsTerm = ref(null)

const items = [ "우리SUPER주거래적금", "WON적금", "퍼스트가계적금", "내손안에 적금",
    "마이(My)적금", "영플러스적금", "내가만든 보너스적금", "IM스마트적금",
    "2030부산월드엑스포적금", "펫 적금", "저탄소 실천\n적금",
    "내맘대로 \n적금", "너만Solo\n적금", "해피라이프_여행스케치적금V",
    "여행스케치_남도투어적금", "VIP플러스적금", "텔레파시적금", "jBANK 저금통적금", 
    "더탐나는적금3", "MZ플랜적금", "탐이나요적금", "JB 다이렉트적금(자유적립식)",
    "JB 카드 재테크 적금\n(정기적립식)", "행복Dream적금", "BNK더조은자유적금",
    "BNK 위더스(With-us)자유적금", "주거래프리미엄적금", "IBK썸통장(자유적립식)",
    "IBK D-day적금(자유적립식)", "IBK탄소제로적금(자유적립식)", "IBK중기근로자우대적금\n(자유적립식)",
    "KDBdream 자유적금", "정기적금", "KDB Hi 자유적금", "KB국민프리미엄적금(정액)",
    "KB반려행복적금", "KB 특★한 적금", "신한 알.쏠 적금", "NH올원e 미니적금",
    "NH1934월복리적금", "NH내가Green초록세상적금", "NH고향사랑기부적금",
    "NH직장인월복리적금", "주거래하나 월복리적금", "내맘적금", "코드K 자유적금",
    "주거래우대 자유적금", "Sh평생주거래우대적금", "Sh해양플라스틱Zero!적금\n(정액적립식)", "헤이(Hey)적금(정액적립식)",
    "Sh월복리자유적금", "Sh해양플라스틱Zero!적금\n(자유적립식)", "헤이(Hey)적금(자유적립식)",
    "Sh수산물을좋아海적금", "카카오뱅크 자유적금", "카카오뱅크 26주적금", "토스뱅크 키워봐요 적금",
    "토스뱅크 굴비 적금", "토스뱅크 자유 적금", "토스뱅크 아이 적금",

    "WON플러스예금", "e-그린세이브예금", "DGB주거래우대예금(첫만남고객형)",
    "DGB행복파트너예금(일반형)", "DGB함께예금", "IM스마트예금", "LIVE정기예금",
    "더(The) 특판 정기예금", "더(The) 레벨업 정기예금", "미즈월복리정기예금", "스마트모아Dream정기예금",
    "굿스타트예금", "The플러스예금", "제주Dream\n정기예금\n(개인/만기\n지급식)",   
    "J정기예금\n(만기지급식)", "JB 다이렉트예금통장\n(만기일시지급식)", "JB 123 정기예금\n (만기일시지급식)",
    "BNK더조은정기예금", "BNK주거래우대정기예금", "IBK평생한가족통장(실세금리정기예금)",
    "i-ONE놀이터예금", "1석7조통장(정기예금)", "정기예금", "KDB 정기예금",
    "KB Star 정기예금", "쏠편한 정기예금", "NH왈츠회전예금 II", "NH내가Green초록세상예금",
    "NH올원e예금", "NH고향사랑기부예금", "하나의정기예금", "코드K 정기예금", "Sh평생주거래우대예금\n(만기일시지급식)",
    "Sh해양플라스틱Zero!예금\n(만기일시지급식)", "헤이(Hey)정기예금", "Sh첫만남우대예금",
    "카카오뱅크 정기예금", "토스뱅크 먼저 이자 받는 정기예금"];
    
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
const savingsTermItmes = [
  "6개월",
  "12개월",
  "24개월",
  "36개월"
]
const signup = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    // age: Number(age.value.replace(/[^0-9]/g, '')) || "",
    // money: Number(money.value.replace(/([^0-9].*)$/g, '')) || "",
    // financial_products: financialProducts.value|| "",
    // primary_bank: primaryBank.value|| "",
    // occupation: occupation.value|| "",
    // savings_goal: savingsGoal.value|| ""
  };


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
  store.signup(payload);
};
</script>

<style scoped>

.submit {
  margin-bottom: 100px;
}
</style>