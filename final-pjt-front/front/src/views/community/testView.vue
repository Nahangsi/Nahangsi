<template>
  <!-- 게시글 생성 -->
  <div>
    <h2>게시글 작성</h2>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title" /><br />
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea
      ><br />
      <label for="category">카테고리</label>
      <select id="category" v-model="category">
        <option value="예금">예금</option>
        <option value="적금">적금</option>
        <option value="기타">기타</option></select
      ><br />
      <input type="submit" id="submit" />
    </form>
  </div>
</template>

<script setup>

</script>

<style  scoped>

</style>