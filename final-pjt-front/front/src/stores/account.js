import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAccountStore = defineStore(
  "account",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const token = ref(null);
    const userinfo = ref(null)
    const router = useRouter();

    const signup = (payload) => {
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
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
          savings_term: payload.savings_term
        },
      })
        .then((res) => {
          window.alert("회원가입을 축하드려요!");
          router.push("/");
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    const login = (payload) => {
      const { username, password } = payload;
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: { username, password },
      })
        .then((res) => {
          token.value = res.data.key;
          // localStorage.setItem("isLogin", isLogin.value);
        })
        .then((res) => {
          axios({
            method: "get",
            url: `${API_URL}/accounts/user_info/`,
            headers: {
              Authorization: `Token ${token.value}`,
            },
          })
          .then((res) => {
            userinfo.value = res.data
          })
          .then((res) => {
            alert("환영합니다! 자유롭게 이용해주세요!");
            router.push("/");
          })
          .catch((err) => {
            console.log(err);
            alert("로그인에 실패하였습니다. 아이디와 비밀번호를 확인해주세요!!");
          });
          })
    };

    const logout = () => {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          localStorage.removeItem("account");
          alert("로그아웃 되었습니다!");
          // isLogin.value = false;
          token.value = null;
          router.push("/");
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const UserInfo = (context) => {
      const token = context.state.token
      const userinfo = ref(null)
      axios({
        methods : "get",
        url : `${API_URL}/accounts/user/`,
        headers : {
          Authorization : `Token ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        userinfo = res.data
      })
      .catch((err) => {
        console.log(err)
      })

    }

    return { API_URL, signup, login, token, isLogin, logout, UserInfo };
  },
  { persist: true }
);