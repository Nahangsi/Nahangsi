import { createRouter, createWebHistory } from 'vue-router'

import CreateView from '@/views/community/CreateView.vue'
import ArticleView from '@/views/community/ArticleView.vue'
import DetailView from '@/views/community/DetailView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
  ]
})

export default router
