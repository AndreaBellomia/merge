import { createRouter, createWebHashHistory } from 'vue-router'
import BookingView from '../views/BookingView.vue'

const routes = [
  {
    path: '/',
    name: 'Booking',
    component: BookingView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
