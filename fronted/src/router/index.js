import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../components/Login.vue'),
    },
    {
      path: '/ticket',
      name: 'Ticket',
      component: () => import('../views/TicketView.vue'),
    },
    {
      path: '/ticket/verify/:id',
      name: 'Verify',
      component: () => import('../views/VerifyView.vue'),
    },
    {
      path: '/mystickets',
      name: 'mystickets',
      component: () => import('../views/UserTicketsView.vue'),
    },
    {
      path: '/travel/:id',
      name: 'Travel',
      component: () => import('../views/TravelView.vue'),
    },
  ],
})

export default router