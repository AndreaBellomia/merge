import { createRouter, createWebHashHistory } from 'vue-router'
import MyBookingView from '../views/MyBookingView.vue'
import AddBookingView from '../views/AddBookingView.vue'
import FormBookingView from '../views/FormBookingView.vue'

const routes = [
  {
    path: '/MyBookingView',
    name: 'MyBookingView',
    component: MyBookingView
  },
  {
    path: '/AddBookingView',
    name: 'AddBookingView',
    component: AddBookingView
  },
  {
    path: '/FormBookingView',
    name: 'FormBookingView',
    component: FormBookingView
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
