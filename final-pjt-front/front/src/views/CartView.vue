<template>
    <!-- <div>
        <h1>찜한 상품</h1>
        <div v-if="cartItems" class="product-list">
            <div v-for="product in cartItems" :key="product.id" class="product-card">
                <img :src="product.image" alt="">
                <strong>{{ product.title }}</strong>
                <p>상품 설명 : ${{ product.content }}</p>
                <button @click="goDetail(product)">상세페이지로 이동</button>
                <button @click="removeCart(product)">찜한 상품 삭제</button>  
            </div>
        </div>
        <div v-else>
        <strong>찜한 상품이 없습니다.</strong>
        </div>
    </div> -->
    <div>
    <h2>Cart View</h2>
    <hr>
    <p class="font-weight-bold">예금!</p>
    <div v-if="likedDepositProducts.length === 0">
      <p>동록된 상품이 없습니다.</p>
    </div>
    <div v-else>
      <ul>
        <li v-for="depositProduct in likedDepositProducts" :key="depositProduct.id">
          {{ depositProduct.fin_prdt_nm }}
        </li>
      </ul>
    </div>

    <hr>
    <hr>
    <p class="font-weight-bold">적금!</p>
    <div v-if="likedsavingProducts.length === 0">
      <p>동록된 상품이 없습니다.</p>
    </div>
    <div v-else>
      <ul>
        <li v-for="savingProduct in likedsavingProducts" :key="savingProduct.id">
          {{ savingProduct.fin_prdt_nm }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const likedDepositProducts = JSON.parse(localStorage.getItem('likedDepositProducts')) || [];
const likedsavingProducts = JSON.parse(localStorage.getItem('likedsavingProducts')) || [];


// const router = useRouter()

// const cartItems = ref(null)

// cartItems.value = JSON.parse(localStorage.getItem('cart'))

// const goDetail = (product) => {
//   router.push(`/${product.id}`)
// }

// const removeCart = (product) => {
//   // localStoage 에서 삭제

//   // 삭제할 아이템 index 검색
//   const itemIdx = cartItems.value.findIndex((item) => item.id === product.id)
 
//   // 데이터 삭제
//   cartItems.value.splice(itemIdx, 1)

//   // 삭제된 데이터를 기준으로 데이터를 반영
//   localStorage.setItem('cart', JSON.stringify(cartItems.value))
// }

</script>

<style scoped>

</style>