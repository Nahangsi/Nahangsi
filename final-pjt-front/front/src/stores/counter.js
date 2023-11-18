
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore("counter", () => {
 
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

  const deposits = ref([]);
  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/deposits/deposit-products/`,
    })
    .then((res) => {
      console.log(res)
      deposits.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const articles = ref([])

 //  DRF 서버로 요청 보내고 응답 데이터 처리하는 getArticles 함수
  const getArticles = function () {
   axios({
     method: 'get',
     url: `${API_URL}/api/v1/articles/`
   })
   .then((res)=> {
     // store에 게시글 목록 데이터 저장s
     articles.value = res.data
   })
   .catch(err => console.log(err))
   }

  return { gogo, deposits, API_URL, getDeposits, articles, getArticles}
}, {persist : true}
);



