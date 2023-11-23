<template>
  <div style="height: 2000px">

    <v-carousel style="max-width: 100%; height: 600px;" show-arrows="hover" cycle="true" interval="4500">
      <v-carousel-item cover>
        <img src="src/assets/장바구니.png" style="object-fit: cover; width: 100%; height: 100%;" alt="장바구니">
      </v-carousel-item>

      <v-carousel-item cover>
        <img src="src/assets/최고금리.png" style="object-fit: cover; width: 100%; height: 100%;" alt="최고금리">
      </v-carousel-item>

      <v-carousel-item cover>
        <img src="src/assets/은행찾기.png" style="object-fit: cover; width: 100%; height: 100%;" alt="은행찾기">
      </v-carousel-item>
    </v-carousel>

    <p class="video__description" data-aos="fade-left" data-aos-anchor-placement="center-center">
      Your description content here 
    </p>`
    <p class="video__description" data-aos="fade-right" data-aos-anchor-placement="center-center">
      Your description content here 
    </p>
    <p class="video__description" data-aos="fade-top" data-aos-anchor-placement="center-center">
      Your description content here 
    </p>
  </div>
</template>

<script setup></script>

<style scoped>
v-carousel {
  margin-top: 30px;
}

</style>
