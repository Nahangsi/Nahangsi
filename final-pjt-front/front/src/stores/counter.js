import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore("counter", () => {
  const deposits = ref([]);
  const API_URL = "http://127.0.0.1:8000";

  const gogo = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2

  axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })

  }


  return { gogo, deposits, API_URL}
}, {persist : true}
);
