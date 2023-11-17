<template>
  <div @submit.prevnet="getDeposits">
    <h1>검색하기</h1>
    <p v-if="search">검색 조건을 입력하세요</p>
   
    <div>
      <p>은행을 선택하세요</p>
      <select v-model="bank">
        <option v-for="deposit in deposits" :key="deposit" :value="deposit">
          {{ deposit }}
        </option>
      </select>
    </div>

    <div>
      <p>예치기간</p>
      <select v-model="period">

      </select>
    </div>

  </div>
</template>

<script setup>
import axios from "axios";
import {ref, onMounted} from "vue"
import {useCounterStore} from "@/stores/counter"

const store = useCounterStore();

const bank = ref("");
const period = ref("");
const deposits = ref([]);

onMounted(() => 
  getDeposits()
)
</script>

<style scoped></style>
