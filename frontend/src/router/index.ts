import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import InstitutesView from "@/views/InstitutesView.vue";
import InstituteView from "@/views/InstituteView.vue"
import TeachersView from "@/views/TeachersView.vue";
import TeacherView from "@/views/TeacherView.vue"

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
    component: TeachersView
  },
  {
    path: '/teacher/:id',
    name: 'teacher',
    component: TeacherView
  },
  {
    path: '/institute/:id',
    name: 'institute',
    component: InstituteView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
