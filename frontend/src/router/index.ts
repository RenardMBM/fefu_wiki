import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import InstitutesView from "@/views/InstitutesView.vue";
import TeachersViews from "@/views/TeachersViews.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/institutes',
    name: 'institutes',
    component: InstitutesView
  },
  {
    path: '/teachers',
    name: 'teachers',
    component: TeachersViews
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
