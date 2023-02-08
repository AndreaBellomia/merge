import { createRouter, createWebHashHistory  } from 'vue-router'
import BookingView from '../views/BookingView.vue'
import HomeView from '../views/HomeView.vue'


const routes = [
  {
    path: '/Booking',
    name: 'Booking',
    component: BookingView
  },
  {
    path: '/',
    name: 'Prova',
    component: HomeView,
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
