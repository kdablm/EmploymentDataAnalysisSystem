import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserInfoView from '@/views/userInfoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/user',
      name: 'user',
      children: [
        {
          path: 'info',
          name: 'userInfo',
          component: UserInfoView
        }
      ]
    }
  ],
})

export default router
