import { createRouter, createWebHistory } from "vue-router";

// deposits
import CurrencyCal from "@/views/deposits/CurrencyCal.vue"

// serach 
import BankMapView from "@/views/search/BankMapView.vue"

// community
import CreateView from '@/views/community/CreateView.vue'
import ArticleView from '@/views/community/ArticleView.vue'
import DetailView from '@/views/community/DetailView.vue'
import UpdateView from '@/views/community/UpdateView.vue'

// home 
import HomeView from "../views/HomeView.vue";
// accounts
import SignupView from "../views/accounts/SignupView.vue";
import LoginView from "../views/accounts/LoginView.vue";
import ProfileView from "../views/accounts/ProfileView.vue"
// mypage
import MypageMainView from "../views/mypage/MypageMainView.vue"
// cart
import CartView from '../views/CartView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 환율 계산
    {
      path : '/currency',
      name : 'CurrencyCal',
      component : CurrencyCal
    },
    // 게시글 메인페이지
    { 
      path:'/',
      name:'ArticleView',
      component: ArticleView
    },
    // 게시글 상세 페이지
    {
      path:'/articles/:id',
      name:'DetailView',
      component: DetailView
    },
    // 게시글 생성 페이지
    {
      path:'/create',
      name:'CreateView',
      component: CreateView
    },
    // 게시글 수정 페이지
    {
      path:'/articles/:id/update',
      name:'UpdateView',
      component: UpdateView
    },
    // 메인 홈페이지
    {  
      path: "/",
      name: "home",
      component: HomeView,
    },
    // 회원가입
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    // 로그인
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    // 마이페이지 메인
    {
      path: "/mypage",
      name: "mypage",
      component: MypageMainView,
    },
    // 프로필
    {
      path: "/profile",
      name: "profile",
      component: ProfileView,
    },
    // 가까운 은행 찾기
    {
      path : '/bankmap',
      name : 'bankmap',
      component : BankMapView
    },
    // 찜한 상품으로 이동
    {
      path: '/cart',
      name: 'cart',
      component: CartView
    }
  ],
});

export default router;
