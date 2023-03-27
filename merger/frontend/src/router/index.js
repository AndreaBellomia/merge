import { createRouter, createWebHashHistory } from 'vue-router'

/* Booking */
import MainBooking from '../views/MainBooking.vue'
import NewAppointmentBooking from '../views/NewAppointmentBooking.vue'
import FormDetailsBooking from '../views/FormDetailsBooking.vue'
import FormAddBooking from '../views/FormAddBooking.vue'

/* Ticket */
import MainTicket from '../views/MainTicket.vue'
import NewTicket from '../views/NewTicket.vue'
import FormAddTicket from '../views/FormAddTicket.vue'

const routes = [
  /* Booking */
  {
    name: 'MainBooking',
    path: '/booking',
    component: MainBooking
  },
  {
    name: 'NewAppointmentBooking',
    path: '/booking/new',
    component: NewAppointmentBooking
  },
  {
    name: 'FormAddBooking',
    path: '/booking/new/form/:id',
    component: FormAddBooking
  },
  {
    name: 'FormDetailsBooking',
    path: '/booking/details/:id/:type',
    component: FormDetailsBooking
  },

  /* Ticket */
  {
    name: 'MainTicket',
    path: '/ticket',
    component: MainTicket
  },
  {
    name: 'NewTicket',
    path: '/ticket/new',
    component: NewTicket
  },
  {
    name: 'FormAddTicket',
    path: '/ticket/new/form/:id',
    component: FormAddTicket
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
