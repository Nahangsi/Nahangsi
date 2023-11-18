import { createRouter, createWebHistory } from "vue-router";
import CurrencyCal from "@/views/deposits/CurrencyCal.vue"
import MainView from "@/views/MainView.vue"
import SignUpView from "@/views/accounts/SignUpView.vue"
import BankMapView from "@/views/BankMapView.vue"



import CreateView from '@/views/community/CreateView.vue'
import ArticleView from '@/views/community/ArticleView.vue'
import DetailView from '@/views/community/DetailView.vue'


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
    
    },
    {
      path:'/',
      name:'ArticleView',
      component: ArticleView
    },
    {
      path:'/articles/:id',
      name:'DetailView',
      component: DetailView
    },
    {
      path:'/create',
      name:'CreateView',
      component: CreateView
    },
  ],
});


export default router;
