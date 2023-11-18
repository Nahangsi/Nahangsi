<template>
  <!-- 게시글 생성 -->
    <div>
      <h2>게시글 작성</h2>
      <form @submit.prevent="createArticle">
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="title"><br>
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
        <label for="category">카테고리</label>
        <select id="category" v-model="category">
          <option value="예금">예금</option>
          <option value="적금">적금</option>
          <option value="기타">기타</option>
        </select><br>
        <input type="submit" id="submit">
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  const API_URL = 'http://127.0.0.1:8000'
  
  export default {
    name: 'CreateView',
    data() {
      return {
        title: null,
        content: null,
        category: null,
      }
    },
    methods: {
      createArticle() {
        const title = this.title
        const content = this.content
        const category = this.category
  
        if (!title) {
          alert('제목을 입력해주세요')
          return
        } else if (!content){
          alert('내용을 입력해주세요')
          return
        } else if (!category) {
          alert('카테고리를 지정해주세요')
        }
        axios({
          method: 'POST',
          url: `${API_URL}/api/v1/articles/`,
          data: { title, content, category },
          // headers: {
          //   Authorization: `Token ${this.$store.state.token}`
          // }
        })
        .then((res) => {
          this.$router.push({ name: 'ArticleView' })
        })
        .catch((err) => {
          console.log(err)
        })
      }
    }
  }
  </script>
  
  <style>
  
  </style>