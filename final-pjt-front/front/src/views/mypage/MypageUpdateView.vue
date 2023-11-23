<template>
  <div>
    <v-sheet width="300" class="mx-auto" style="margin-bottom: 50px">
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
          placeholder="추가 정보를 입력해주세요"
        ></v-text-field>
        연령대
        <v-autocomplete
          v-model="age"
          :items="['10대', '20대', '30대', '40대', '50대', '60대 이상']"
          variant="outlined"
          placeholder="추가 정보를 입력해주세요"
        ></v-autocomplete>
        가입한 금융 상품
        <v-combobox
          v-model="financialProducts"
          :items="items"
          multiple
          variant="outlined"
          placeholder="추가 정보를 입력해주세요"
        ></v-combobox>
        월별 저축 금액
        <v-combobox
          v-model="money"
          :items="moneyItems"
          variant="outlined"
          placeholder="추가 정보를 입력해주세요"
        ></v-combobox>
        연봉
        <v-combobox
          v-model="salary"
          :items="salaryItems"
          variant="outlined"
          placeholder="추가 정보를 입력해주세요"
        ></v-combobox>
        주 거래은행
        <v-combobox
          v-model="primaryBank"
          :items="primaryBankItems"
          variant="outlined"
          placeholder="추가 정보를 입력해주세요"
        ></v-combobox>
        저축 목표
        <v-combobox
          v-model="savingsGoal"
          :items="savingsGoalItmes"
          variant="outlined"
          placeholder="추가 정보를 입력해주세요"
        ></v-combobox>
        저축 기간
        <v-combobox
          v-model="savingsTerm"
          :items="savingsTermItmes"
          variant="outlined"
          placeholder="추가 정보를 입력해주세요"
        ></v-combobox>
        직종
        <v-combobox
          v-model="occupation"
          :items="occupationItmes"
          variant="outlined"
          placeholder="추가 정보를 입력해주세요"
        ></v-combobox>

        <v-btn type="submit" block class="mt-2 submit" variant="outlined"

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
const age = ref(null);
const money = ref(null);
const salary = ref(null);
const financialProducts = ref(User.financial_products);
const primaryBank = ref(User.primary_bank);
const occupation = ref(User.occupation);
const savingsGoal = ref(User.savings_goal);
const savingsTerm = ref(null);

const items = [
"우리SUPER주거래적금", "WON적금", "퍼스트가계적금", "내손안에 적금",
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
    "카카오뱅크 정기예금", "토스뱅크 먼저 이자 받는 정기예금"
];
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
console.log(financialProducts.value);
if (User.age !== null) {
  age.value = User.age + "대";
}
if (User.money !== null) {
  money.value = User.money + "만원 이상";
}
if (User.salary !== null) {
  salary.value = User.salary + "이상";
}
if (User.savings_term !== null) {
  savingsTerm.value = User.savings_term + "개월";
}
if (User.financial_products !== undefined) {
  financialProducts.value = User.financial_products.substring(
    1,
    User.financial_products.length - 1
  );
}

if (User.age !== null) {
  age.value = User.age + "대";
}
if (User.money !== null) {
  money.value = User.money + "만원 이상";
}
if (User.salary !== null) {
  salary.value = User.salary + "이상";
}
if (User.savings_term !== null) {
  savingsTerm.value = User.savings_term + "개월";
}
if (User.financial_products !== undefined) {
  financialProducts.value = User.financial_products.substring(
    1,
    User.financial_products.length - 1
  );
}

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
    // financialProducts.value.push()
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

<style scoped>

.submit {
  margin-bottom: 100px;

}
</style>
