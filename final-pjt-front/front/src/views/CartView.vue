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
    <div v-if="likedArticles.length === 0">
      <p>No liked articles in the cart.</p>
    </div>
    <div v-else>
      <ul>
        <li v-for="article in likedArticles" :key="article.id">
          {{ article.title }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const likedArticles = JSON.parse(localStorage.getItem('likedArticles')) || []


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