import { ref, computed } from "vue";
import { defineStore } from "pinia";


export const useCounterStore = defineStore("counter", () => {
  const deposits = ref([]);
  const API_URL = "http://127.0.0.1:8000";

  axios({
    method: 'get',
    url: `${API_URL}/api/deposits/save-deposit-products/`,
  })
    .then(response => {
      console.log(response.data);
      deposits.value = response.data;
    })
    .catch(error => {
      console.error(error);
    });
  
  return { deposits, API_URL, getDeposits };
});
