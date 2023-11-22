import { createRouter, createWebHistory } from "vue-router";

// deposits
import CurrencyCal from "@/views/deposits/CurrencyCal.vue"
import DepositProductView from "@/views/deposits/DepositProductView.vue"
import SavingProductView from "@/views/deposits/SavingProductView.vue"
import DepositProductDetailView from '@/views/deposits/DepositProductDetailView.vue'

// serach 
import BankMapView from "@/views/search/BankMapView.vue"
import Bank from "@/views/search/Bank.vue"
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
// mypage
import MypageMainView from "../views/mypage/MypageMainView.vue";
import MypageUpdateView from "../views/mypage/MypageUpdateView.vue";
import MypagePasswordUpdateView from "../views/mypage/MypagePasswordUpdateView.vue";
import MypageUserdeleteView from "../views/mypage/MypageUserdeleteView.vue";
import Calendar from "../views/mypage/Calendar.vue";
// cart
import CartView from '../views/CartView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    // 환율 계산
    {
      path: "/currency",
      name: "CurrencyCal",
      component: CurrencyCal,
    },
    // 게시글 메인페이지
    {
      path: "/",
      name: "ArticleView",
      component: ArticleView,
    },
    // 게시글 상세 페이지
    {
      path: "/articles/:id",
      name: "DetailView",
      component: DetailView,
    },
    // 게시글 생성 페이지
    {
      path: "/create",
      name: "CreateView",
      component: CreateView,
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
    // 회원정보 수정
    {
      path: "/mypageupdate",
      name: "mypageupdate",
      component: MypageUpdateView,
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
    },
    // bank map vuetify
    {
      path : '/bank',
      name : 'Bank',
      component : Bank

    },
     // 회원정보 수정
     {
      path: "/mypageupdate",
      name: "mypageupdate",
      component: MypageUpdateView,
    },
    // 비밀번호 수정
    {
      path: "/mypagepasswordupdate",
      name: "mypagepasswordupdate",
      component: MypagePasswordUpdateView,
    },
    // 회원 탈퇴
    {
      path: "/mypageendmembership",
      name: "mypageendmembership",
      component: MypageUserdeleteView,
    },
    // 예금 상품 
    {
      path: "/depositproduct",
      name: "depositproduct",
      component: DepositProductView,
    },
    // 적금 상품 
    {
      path: "/savingproduct",
      name: "savingproduct",
      component: SavingProductView,
    },
    // 금융상품 상세 페이지
    {
      path: "/productdetail/:id",
      name: "productdetail",
      component: DepositProductDetailView,
    },
    // 캘린더
    {
      path: "/calendar",
      name: "calendar",
      component : Calendar,
    },
],

});

export default router;
