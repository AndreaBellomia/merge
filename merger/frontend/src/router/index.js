import { createRouter, createWebHashHistory } from 'vue-router'
import BookingView from '../views/BookingView.vue'

const routes = [
  {
    path: '/booking',
    name: 'booking',
    component: BookingView
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
