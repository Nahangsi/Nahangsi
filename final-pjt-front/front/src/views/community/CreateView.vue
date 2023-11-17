<!-- 게시글 작성하는 vue -->
<template>
    <div>
        <h2>게시글 작성</h2>
        <!-- submit 이벤트의 기본 동작(새로고침) 취소 -->
        <form @submit.prevent="createArticle">
            <label for="title">제목 : </label>
            <!-- v-model 사용해 사용자 입력 데이터 양방향 -->
            <!-- , trim 수식어 사용해 데이터 공백 제거 -->
            <input type="text" id="title" v-model.trim="title"><br>
            <label for="content">내용 : </label>
            <textarea id="content" cols="30" rows="10" v-model.trim="content"></textarea><br>
            <!-- <label for="category">카테고리</label>
            <select id="category" v-model="category">
                <option value="예금">예금</option>
                <option value="적금">적금</option>
                <option value="기타">기타</option>
            </select><br> -->
            <input type="submit" id="submit">
        </form>
    </div>
</template>

<script setup>
// import { ref } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter';
import router from '../../router';

const store = useCounterStore()
const route = useRoute()

// const title = ref(null)
// const content = ref(null)

// 게시글 생성 요청 담당 하는 createArticle함수 

const createArticle = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles`,
      data: {
        title: title.value,
        content: content.value
      },
    // -> 게시글 생성 성공하면 ArticleView 컴포넌트로
    }).then(()=> {
      router.push({name: 'ArticleView'})
    }).catch(err => console.log(err))
    }
</script>

<style scoped>

</style>