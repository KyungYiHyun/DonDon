import { useMemberStore } from '@/stores/member'
import DepositView from '@/views/DepositView.vue'
import Homeview from '@/views/Homeview.vue'
import LoginView from '@/views/LoginView.vue'
import MapView from '@/views/MapView.vue'
import RecommendDepositView from '@/views/RecommendDepositView.vue'
import RecommendSavingView from '@/views/RecommendSavingView.vue'
import SavingView from '@/views/SavingView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ArticleView from '@/views/ArticleView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import CreateArticleView from '@/views/CreateArticleView.vue'
import ProfileView from '@/views/ProfileView.vue'
import PasswordChangeView from '@/views/PasswordChangeView.vue'
import CartView from '@/views/CartView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name : 'HomeView',
      component: Homeview
    },
    {
      path: '/deposit',
      name : 'DepositView',
      component: DepositView
    },
    {
      path: '/saving',
      name : 'SavingView',
      component: SavingView
    },
    {
      path: '/recommend/deposit',
      name : 'RecommendDepositView',
      component: RecommendDepositView,
      beforeEnter: (to, from) => {
        const store = useMemberStore()
        if (!store.isLogin) {
          alert('로그인이 필요한 서비스입니다.')
          return { name: 'LoginView'}
        }
      }
    },
    {
      path: '/recommend/saving',
      name : 'RecommendSavingView',
      component: RecommendSavingView,
      beforeEnter: (to, from) => {
        const store = useMemberStore()
        if (!store.isLogin) {
          alert('로그인이 필요한 서비스입니다.')
          return { name: 'LoginView'}
        }
      }
    },
    {
      path: '/article/',
      name : 'ArticleView',
      component: ArticleView
    },
    {
      path: '/create/article/',
      name : 'CreateArticleView',
      component: CreateArticleView,
      beforeEnter: (to, from) => {
        const store = useMemberStore()
        if (!store.isLogin) {
          alert('로그인이 필요한 서비스입니다.')
          return { name: 'LoginView'}
        }
      }
    },
    {
      path: '/article/:articleId',
      name : 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/login',
      name : 'LoginView',
      component: LoginView
    },
    {
      path: '/signup',
      name : 'SignUpView',
      component: SignUpView
    },
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/cart',
      name: 'CartView',
      component: CartView,
      beforeEnter: (to, from) => {
        const store = useMemberStore()
        if (!store.isLogin) {
          alert('로그인이 필요한 서비스입니다.')
          return { name: 'LoginView'}
        }
      }
    },
    {
      path: '/passwordchange',
      name: 'PasswordChangeView',
      component: PasswordChangeView
    }
  ]
})

router.beforeEach((to, from)=>{
  const store = useMemberStore()
  if((to.name === 'SignUpView' || to.name === 'LoginView') && (store.isLogin)){
    window.alert('이미 로그인 되어있습니다.')
    return {name: 'HomeView'}
  }
})

export default router
