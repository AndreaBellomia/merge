<template>
  <div>
    <header class="flex flex-col space-y-8 p-8">
        <span class="custom-title">Prenotazioni</span>
        <div class="custom-legend-container flex space-x-4">
        <span class="custom-legend flex items-center">
            <span class="custom-circle confirmed"></span>
            <span class="custom-label">Confermato</span>
        </span>
        <span class="custom-legend flex items-center">
            <span class="custom-circle waiting ml-3"></span>
            <span class="custom-label">In Attesa</span>
        </span>
        <span class="custom-legend ml-3 flex items-center">
            <span class="custom-circle canceled ml-3"></span>
            <span class="custom-label">Annullato</span>
        </span>
        </div>
    </header>
    <main class="mb-32">
        <BookingListItem v-for="booking in bookings" :key="booking" :booking="booking">
        </BookingListItem>
    </main>
    <nav class="custom-fb-container">
        <FloatingActionButton :routerLink="'/AddBookingView'" :icon="'add'" />
        <FloatingActionButton :routerLink="'/'" :icon="'filter_list'" />
    </nav>
  </div>
</template>

<script>
import axios from 'axios';
import BookingListItem from '../components/Booking/BookingListItem.vue'
import FloatingActionButton from '../components/Booking/FloatingActionButton.vue'

export default {
  components: {
    BookingListItem,
    FloatingActionButton
  },
  data() {
    return {
      bookings: [],
    }
  },
  mounted() {
    this.getHTTP_bookingList()
  },
  methods: {
    getHTTP_bookingList() {
      axios
        .get("/api/client/booking/?format=json")
        .then((response) => {
          this.bookings = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  }
}
</script>

<style scoped lang="scss">
.custom-title {
  font-style: normal;
  font-weight: 600;
  font-size: 1.75rem;
  line-height: 29px;
}

.custom-legend-container {
  margin-top: 2rem;

  .custom-legend {
    .custom-circle {
      width: 0.75rem;
      height: 0.75rem;
      border-radius: 50%;
    }

    .custom-circle.confirmed {
      background-color: #1ABD00;
    }

    .custom-circle.waiting {
      background-color: #FFB800;
    }

    .custom-circle.canceled {
      background-color: #FF1F00;
    }

    .custom-label {
      font-style: normal;
      font-weight: 300;
      font-size: 0.75rem;
      line-height: 12px;
      color: #000000;
      margin-left: 0.2rem;
    }
  }
}

.custom-fb-container {
  position: absolute;
  bottom: 8rem;
  right: 1.5rem;
  display: flex;
  flex-direction: column;
}
</style>
