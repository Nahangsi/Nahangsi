<template>

  <div style="height: 5050px">

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
    
    <div title="여백 박스" style="height: 230px;"></div>

    <v-container fluid style="margin: 0px; padding: 0px;">
      <!-- First Section: Deposit and Savings -->
      <v-row >
        <v-col cols="12">
          <div class="section-card">
            <div class="headline" style="background-color: #F6F7F9; padding: 50px; padding-bottom: 50px; ">
              <p data-aos="fade-up" data-aos-duration="1500" data-aos-delay="500" style="font-size: 24px;" class="video__description">
                내 수준과 목표에 딱 맞는 예금, <br>
                적금 목록을 한눈에 조회하고 <br> 한 손으로 관리하세요 <br>
                <ul>나행시와 함께라면 금융 관리도 <br>어렵지 않을거에요.</ul>
              </p>
            </div>
          </div>
        </v-col>
      </v-row>

      <!-- Second Section: Deposit and Savings Comparison -->
      <v-row >
        <v-col cols="12" md="6">
          <div class="section-card">
            <div class="headline">
              <p data-aos="fade-right" data-aos-duration="1500" data-aos-delay="500" class="video__description">
                <p style="color: #1E88E5; font-size: 20px; font-weight: 500;">예금, 적금 조회</p><br>
                <p style="font-size: 30px; font-weight: 700;">여러 은행의 조건을 <br> 1초만에 확인해보세요</p>
                <br>
                <div>
              <img src="src/assets/주식보기.jpg" alt="이미지 넣기" style="width: 100%;">
              </div> 
              <div style="font-size: 18px; font-weight: 500; margin-top: 15px;" >
                앉은 자리에서 
                은행들 간의 예,적금 비교와,<br>
                6/12/24/36개월로 기간에 따른,<br>
                기본 금리 순과 최고 금리 순으로 <br>선택하고 비교하면서,<br>
                내게 꼭 맞는 예금 적금을 찾아보세요.
              </div>

              </p>
            </div>
          </div>
        </v-col>
      </v-row>

      <div title="여백박스" style="height: 100px;"></div>

      <v-row style="padding-bottom: 0px;">
        <v-col cols="12" style="margin-top: 30px;  padding-bottom: 0px; margin-bottom: 0px;">
          <div class="section-card">
            <div class="headline" style="background-color: #F6F7F9;
            padding-top: 40px; padding-bottom: 40px; margin-top: 40px;">
              <p data-aos="fade-left" data-aos-duration="1500" data-aos-delay="2500" class="video__description">
                <h2 style="color: #1E88E5;  ">당신 근처의 은행 찾기</h2><br>
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
      <v-row data-aos="fade-right" data-aos-duration="1400" data-aos-delay="1500">
        <v-col cols="12">
          <div class="section-card">
            <div>
              <img src="src/assets/phone.jpg" alt="이미지 넣기" style="width: 100%;">
            </div>
          </div>
        </v-col>
      </v-row>

      <div title="여백박스" style="height: 230px;"></div>

      <!-- Fourth Section: Exchange Rates -->
      <v-row >
        <v-col cols="12">
          <div class="section-card">
            <div class="headline" data-aos="fade-right" data-aos-duration="1800" data-aos-delay="2000">
              <p class="video__description">
                <p style="color: #1E88E5; font-size: 20px; font-weight: 500;">환율</p><br>
                <p style="font-size: 30px; font-weight: 700;">전 세계 40개국 이상의 환율을 비교 가능해요</p>
                <br>
                <p>현금 살때, 현금 팔때의 경우를 나눠서 비교하여<br>
                더욱 더 합리적인 환전을 할 수 있어요</p>

              </p>
            </div>
          </div>
        </v-col>
      </v-row>

      <div title="여백박스" style="height: 230px;"></div>

      <!-- Fifth Section: Discussion Board -->
      <v-row data-aos="fade-left" data-aos-duration="2000" data-aos-delay="1000">
        <v-col cols="12">
          <div class="section-card">
            <div class="headline">
              <p class="video__description">
                <p style="color: #1E88E5; font-size: 20px; font-weight: 500;">게시판</p><br>
                <p style="font-size: 30px; font-weight: 700;">회원들과 자유롭게 소통해요</p> <br>
                누구든지 상관없이, <br>
                자유롭게 의견을 나누고 정보를 주고 받아요
              </p>

              <img src="src/assets/게시판.jpg" alt="이미지 넣기" style="width: 100%;">

            </div>
          </div>
        </v-col>
      </v-row>

      <div style="height: 50px; margin-top: 50px; text-align: center; ">
      <p style="font-size: 30px; font-weight: 700; color: #1E88E5;">지금 나행시와 시작해보세요!</p></div>



    </v-container>

  </div>
</template>

<script setup>

</script>


<style scoped>
.section-card {
  margin-bottom: 60px; /* 여기서 간격을 조절해주세요. */
}
</style>

