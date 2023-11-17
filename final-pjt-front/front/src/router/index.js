import { createRouter, createWebHistory } from "vue-router";
import DepositView from "@/views/deposits/DepositView.vue"
import CurrencyCal from "@/views/deposits/CurrencyCal.vue"
import MainView from "@/views/MainView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'MainView',
      component : MainView
    },
    {
      path : '/deposit',
      name : 'DepositView',
      component : DepositView
    },
    {
      path : '/currency',
      name : 'CurrencyCal',
      component : CurrencyCal
    }
  ],
});

export default router;
