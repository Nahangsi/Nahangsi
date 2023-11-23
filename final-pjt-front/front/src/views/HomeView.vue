<template>
  <div style="height: 2000px">

    <v-carousel style="max-width: 100%; height: 600px; margin-bottom: 80px;" show-arrows="hover" cycle="true" interval="4500">
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

    <v-container fluid>
      <!-- First Section: Deposit and Savings -->
      <v-row data-aos="fade-up" data-aos-duration="1000" data-aos-delay="1300">
        <v-col cols="12">
          <div class="section-card">
            <div class="headline">
              <p class="video__description">
                내 수준과 목표에 딱 맞는 예금, <br>
                적금 목록을 한눈에 조회하고 한 손으로 관리하세요 <br>
                <ul>나행시와 함께라면 예,적금 관리도 어렵지 않을거에요.</ul>
              </p>
            </div>
          </div>
        </v-col>
      </v-row>

      <!-- Second Section: Deposit and Savings Comparison -->
      <v-row data-aos="fade-right" data-aos-duration="1200" data-aos-delay="1500">
        <v-col cols="12" md="6">
          <div class="section-card">
            <div class="headline">
              <p class="video__description">
                <h2 style="color: #1E88E5;">예금, 적금 조회</h2><br>
                <h3>여러 은행의 조건을 1초만에 확인해보세요</h3>
                <br>
                <div>
              <img src="src/assets/주식보기.jpg" alt="이미지 넣기" style="width: 100%;">
              </div> 
                앉은 자리에서<br>
                은행들 간의 예,적금 비교와,<br>
                6/12/24/36개월로 기간에 따른,<br>
                기본 금리 순과 최고 금리 순으로 선택하고 비교하면서<br>
                내게 꼭 맞는 예금 적금을 찾아보세요.
              </p>
            </div>
          </div>
        </v-col>
      </v-row>

      <v-row data-aos="fade-left" data-aos-duration="1200" data-aos-delay="1500">
        <v-col cols="12">
          <div class="section-card">
            <div class="headline">
              <p class="video__description">
                <h2 style="color: #1E88E5;">당신 근처의 은행 찾기</h2><br>
                <h3>언제든지, 어디서나 은행을 찾을 수 있어요</h3> <br>
                나행시만 있다면 <br>
                내 위치 기반으로 주변의 은행과 <br>
                원하는 위치에서의 원하는 은행을 찾을 수 있어요.
              </p>
            </div>
          </div>
        </v-col>
      </v-row>

      <!-- Third Section: Image Placeholder -->
      <v-row data-aos="fade-up" data-aos-duration="1400" data-aos-delay="1600">
        <v-col cols="12">
          <div class="section-card">
            <div>
              <img src="src/assets/phone.jpg" alt="이미지 넣기" style="width: 100%;">
            </div>
          </div>
        </v-col>
      </v-row>

      <!-- Fourth Section: Exchange Rates -->
      <v-row data-aos="fade-right" data-aos-duration="1800" data-aos-delay="2000">
        <v-col cols="12">
          <div class="section-card">
            <div class="headline">
              <p class="video__description">
                <h2 style="color: #1E88E5;">환율</h2><br>
                <h3>전 세계 40개국 이상의 환율을 비교 가능해요</h3><br>
                현금 살때, 현금 팔때의 경우를 나눠서 비교하여<br>
                더욱 더 합리적인 환전을 할 수 있어요
              </p>
            </div>
          </div>
        </v-col>
      </v-row>

      <!-- Fifth Section: Discussion Board -->
      <v-row data-aos="fade-left" data-aos-duration="2000" data-aos-delay="2200">
        <v-col cols="12">
          <div class="section-card">
            <div class="headline">
              <p class="video__description">
                <h2 style="color: #1E88E5;">게시판</h2><br>
                <h3>회원들과 자유롭게 소통해요</h3> <br>
                누구든지 상관없이, <br>
                자유롭게 의견을 나누고 정보를 주고 받아요
              </p>

              <img src="src/assets/게시판.jpg" alt="이미지 넣기" style="width: 100%;">

            </div>
          </div>
        </v-col>
      </v-row>

      <!-- Sixth Section: Image Placeholder -->
      <!-- <v-row data-aos="fade-up" data-aos-duration="1400" data-aos-delay="1600">
        <v-col cols="12">
          <div class="section-card">
            <div>
              <img src="src/assets/placeholder-image.png" alt="이미지 넣기" style="width: 100%;">
            </div>
          </div>
        </v-col>
      </v-row> -->

    </v-container>
  </div>
</template>

<script setup></script>

<style scoped>
.section-card {
  margin-bottom: 60px; /* 여기서 간격을 조절해주세요. */
}
</style>