import { createRouter, createWebHistory } from "vue-router";
import DepositView from "@/views/deposits/DepositView.vue"
import CurrencyCal from "@/views/deposits/CurrencyCal.vue"
import MainView from "@/views/MainView.vue"
import SignUpView from "@/views/accounts/SignUpView.vue"

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
    },
    {
      path : '/signup',
      name : 'SignUpView',
      component : SignUpView
    }
  ],
});

export default router;
