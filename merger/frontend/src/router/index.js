import { createRouter, createWebHistory } from 'vue-router'
import BookingView from '../views/BookingView.vue'

const routes = [
  {
    path: '/',
    name: 'Booking',
    component: BookingView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
