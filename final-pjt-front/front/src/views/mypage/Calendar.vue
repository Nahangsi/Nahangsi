<template>
    <div id="app">
      <h1>Vue Calendar</h1>
      <datepicker v-model="selectedDate" :format="customFormat"></datepicker>
      <p>Selected Date: {{ selectedDate }}</p>
    </div>
  </template>
  
  <script>
  import Datepicker from 'vuejs-datepicker';
  
  export default {
    components: {
      Datepicker,
    },
    data() {
      return {
        selectedDate: null,
        customFormat: 'yyyy-MM-dd', // 날짜 형식을 지정할 수 있습니다.
      };
    },
  };
  </script>
  
  <style>
  #app {
    text-align: center;
    margin-top: 20px;
  }
  </style>
  