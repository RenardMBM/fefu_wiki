import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import InstitutesView from "@/views/InstitutesView";
import TeachersViews from "@/views/TeachersViews";

const routes = [
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
