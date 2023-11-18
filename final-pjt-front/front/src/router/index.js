import { createRouter, createWebHistory } from "vue-router";
import CurrencyCal from "@/views/deposits/CurrencyCal.vue"
import MainView from "@/views/MainView.vue"
import SignUpView from "@/views/accounts/SignUpView.vue"
import BankMapView from "@/views/BankMapView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'MainView',
      component : MainView
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
    },
    {
      path : '/map',
      name : 'BankMapView',
      component : BankMapView
    }
  ],
});

export default router;
