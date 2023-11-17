import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from "axios";
import { useRouter } from 'vue-router';


export const useAccountStore = defineStore('account', () => {
  const API_URL = "http://127.0.0.1:8000";
  const token = ref(null);
  const router = useRouter();

  const signup = function(payload) {
    

    const { username, email, password1, password2, age, money, salary, financial_products, primary_bank, occupation, savings_goal } = payload;

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, email, password1, password2, age, money, salary, financial_products, primary_bank, occupation, savings_goal,
      },
    })
    .then((res) => {
      window.alert('회원가입을 축하드려요!')
      router.push('/')
    })
    .catch((err) => {
      console.log(err)
    })
  };

  return { signup, API_URL }
})
