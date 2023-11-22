<template>
  <v-container>
    <v-row class="mb-5">
      <v-col>
        <v-divider class="mx-auto mb-3"></v-divider>
        <h2 class="text-h5 font-weight-bold">장바구니</h2>
        <v-divider class="mx-auto mb-3"></v-divider>
      </v-col>
    </v-row>

    <!-- 예금 상품 -->
    <v-row>
      <v-col>
        <h3 class="text-h6 font-weight-bold">예금</h3>
        <v-divider class="mx-auto mb-3"></v-divider>

        <v-row v-if="likedDepositProducts.length === 0">
          <v-col>
            <p>등록된 예금 상품이 없습니다.</p>
          </v-col>
        </v-row>

        <v-row v-else>
          <v-col>
            <v-list>
              <v-list-item-group>
                <v-list-item v-for="depositProduct in likedDepositProducts" :key="depositProduct.id">
                  <v-list-item-content>
                    {{ depositProduct.fin_prdt_nm }}
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-btn @click="removeCart(depositProduct)" height="18" style="border-radius: 5px; max-width: 50px;">삭제</v-btn>
                  </v-list-item-action>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- 중앙 구분선 -->
    <v-divider class="mx-auto my-3"></v-divider>

    <!-- 적금 상품 -->
    <v-row>
      <v-col>
        <h3 class="text-h6 font-weight-bold">적금</h3>
        <v-divider class="mx-auto mb-3"></v-divider>

        <v-row v-if="likedsavingProducts.length === 0">
          <v-col>
            <p>등록된 적금 상품이 없습니다.</p>
          </v-col>
        </v-row>

        <v-row v-else>
          <v-col>
            <v-list>
              <v-list-item-group>
                <v-list-item v-for="savingProduct in likedsavingProducts" :key="savingProduct.id">
                  <v-list-item-content>
                    {{ savingProduct.fin_prdt_nm }}
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-btn @click="removeCart(savingProduct)" height="18" style="border-radius: 5px; max-width: 50px;">삭제</v-btn>
                  </v-list-item-action>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const likedDepositProducts = JSON.parse(localStorage.getItem('likedDepositProducts')) || [];
const likedsavingProducts = JSON.parse(localStorage.getItem('likedsavingProducts')) || [];

const removeCart = (product) => {
  const likedDepositProductsIndex = likedDepositProducts.findIndex((item) => item.id === product.id);
  const likedsavingProductsIndex = likedsavingProducts.findIndex((item) => item.id === product.id);

  if (likedDepositProductsIndex !== -1) {
    likedDepositProducts.splice(likedDepositProductsIndex, 1);
    localStorage.setItem('likedDepositProducts', JSON.stringify(likedDepositProducts));
  } else if (likedsavingProductsIndex !== -1) {
    likedsavingProducts.splice(likedsavingProductsIndex, 1);
    localStorage.setItem('likedsavingProducts', JSON.stringify(likedsavingProducts));
  }

  router.go()
}
</script>

<style scoped>
/* 필요한 경우에 스타일을 추가하세요. */
</style>
