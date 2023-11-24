<template>
  <div>
    <canvas id="myChart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js/auto";

export default {
  props: {
    forchart: Array,
  },

  mounted() {
    const ctx = document.getElementById("myChart");

    const myChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: [
          "너만Solo 적금",
          "IBK탄소제로적금",
          "Sh수산물을좋아海적금",
          "BNK 위더스(With-us)자유적금",
        ],
        datasets: [
          {
            label: "상품 최고 금리 비교",
            data: [9, 7, 7, 7, 6.75],
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
    myChart;
  },
};
</script>

<style scoped>
v-carousel {
  margin-top: 30px;
}
</style>
