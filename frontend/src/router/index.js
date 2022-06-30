import Vue from 'vue'
import VueRouter from 'vue-router'
import IntroView from '../views/IntroView.vue'
import SignupView from '../views/SignupView'
import LoginView from '../views/LoginView'
import MyPageView from '../views/MyPageView.vue'
import RecipeDetailView from '../views/RecipeDetailView.vue'
import RecipeListView from '../views/RecipeDetailView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'intro',
    component: IntroView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/MyPage',
    name: 'MyPage',
    component: MyPageView
  },
  {
    path: '/RecipeDetail',
    name: 'RecipeDetail',
    component: RecipeDetailView
  },
  {
    path: '/RecipeListView',
    name: 'RecipeListView',
    component: RecipeListView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
