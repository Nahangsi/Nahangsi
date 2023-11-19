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
            :items="items"
            label="연봉을 선택해주세요!"
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="salary"
            :items="items"
            label="자산을 선택해주세요!!"
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="primaryBank"
            :items="items"
            label="주거래은행을 선택해주세요!!"
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="savingsGoal"
            :items="items"
            label="저축목표를 선택해주세요!!"
            variant="outlined"
          ></v-combobox>
          <v-combobox
            v-model="occupation"
            :items="items"
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
  import { useCounterStore } from "@/stores/counter";
  import axios from "axios";
  
  const store = useCounterStore();
  
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
  
  const signup = function () {
    console.log(username.value, password1.value, password2.value, email.value);
    console.log(store.API_URL);
  
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      // email: email.value,
      // age: age.value,
      // money: money.value,
      // salary: salary.value,
      // financial_products: financialProducts.value,
      // primary_bank: primaryBank.value,
      // occupation: occupation.value,
      // savings_goal: savingsGoal.value,
    };
  
    if (email.value !== null && email.value !== "") {
      payload.email = email.value;
    }
    if (age.value !== null && age.value !== "") {
      payload.age = age.value;
    }
    if (money.value !== null && money.value !== "") {
      payload.money = money.value;
    }
    if (salary.value !== null && salary.value !== "") {
      payload.salary = salary.value;
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
  
    axios({
      method: "post",
      url: `${store.API_URL}/accounts/signup/`,
      data: {
        username: payload.username,
        email: payload.email,
        password1: payload.password1,
        password2: payload.password2,
        age: payload.age,
        money: payload.money,
        salary: payload.salary,
        financial_products: payload.financial_products,
        primary_bank: payload.primary_bank,
        occupation: payload.occupation,
        savings_goal: payload.savings_goal,
      },
    })
      .then((res) => {
        window.alert("회원가입을 축하드려요!");
      })
      .catch((err) => {
        console.log(err);
      });
  };
  </script>
  
  <style scoped></style>