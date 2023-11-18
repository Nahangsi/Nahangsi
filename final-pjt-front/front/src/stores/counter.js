import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
   const articles = ref([])
   const API_URL = 'http://127.0.0.1:8000'

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
    return {articles, getArticles, API_URL}
}, {persist : true}) 
