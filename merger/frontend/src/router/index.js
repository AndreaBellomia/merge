import { createRouter, createWebHashHistory } from 'vue-router'
import MyBookingView from '../views/MyBookingView.vue'
import NewBookingView from '../views/NewBookingView.vue'
import FormEditBookingView from '../views/FormEditBookingView.vue'
import FormAddBookingView from '../views/FormAddBookingView.vue'
import MyTicketView from '../views/MyTicketView.vue'
import AddTicketView from '../views/AddTicketView.vue'
import FormAddTicketView from '../views/FormAddTicketView.vue'

const routes = [
  {
    path: '/MyBookingView',
    name: 'MyBookingView',
    component: MyBookingView
  },
  {
    path: '/NewBookingView',
    name: 'NewBookingView',
    component: NewBookingView
  },
  {
    path: '/FormEditBookingView/:id/:type',
    name: 'FormEditBookingView',
    component: FormEditBookingView
  },
  {
    path: '/FormAddBookingView/:id',
    name: 'FormAddBookingView',
    component: FormAddBookingView
  },
  {
    path: '/MyTicketView',
    name: 'MyTicketView',
    component: MyTicketView
  },
  {
    path: '/AddTicketView',
    name: 'AddTicketView',
    component: AddTicketView
  },
  {
    path: '/FormAddTicketView/:id',
    name: 'FormAddTicketView',
    component: FormAddTicketView
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
