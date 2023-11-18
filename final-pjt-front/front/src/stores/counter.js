import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const API_URL = "http://127.0.0.1:8000";

    const deposits = ref([]);
    const getDeposits = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/deposits/deposit-products/`,
      })
        .then((res) => {
          console.log(res);
          deposits.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const articles = ref([]);

    //  DRF 서버로 요청 보내고 응답 데이터 처리하는 getArticles 함수
    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/`,
      })
        .then((res) => {
          // store에 게시글 목록 데이터 저장s
          articles.value = res.data;
        })
        .catch((err) => console.log(err));
    };

    return { deposits, API_URL, getDeposits, articles, getArticles };
  },
  { persist: true }
);
