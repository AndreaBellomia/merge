<template>
  <body v-if="!showAddItem">
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
    <nav class="custom-fb-container flex flex-col items-end m-1">
      <span @click="showAddItem = !showAddItem" class="custom-fb flex material-symbols-outlined">
        add
      </span>
      <span class="custom-fb flex material-symbols-outlined">
        filter_list
      </span>
    </nav>
  </body>
  <AddItem :showAddItem="showAddItem" @undo-to-booking-view="showAddItem = !showAddItem" v-else>
  </AddItem>
</template>

<script>
import axios from 'axios';
import BookingListItem from '../components/Booking/BookingListItem.vue'
import AddItem from '../components/Booking/AddItem.vue'
export default {
  components: {
    BookingListItem,
    AddItem
  },
  data() {
    return {
      bookings: [],
      showAddItem: false
    }
  },
  mounted() {
    this.getHTTP_bookingList()
  },
  methods: {
    getHTTP_bookingList() {
      axios
        .get("api/booking/?format=json")
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
  position: fixed;
  bottom: 0;
  height: 25%;
  width: 100%;

  .custom-fb {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    background: #8F62DA;
    box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.5);
    color: #F8FCFF;
    font-size: xx-large;
    padding-top: 0.5rem;
    padding-left: 0.5rem;
    margin-right: 2rem;
    margin-bottom: 1rem;
    cursor: pointer;
  }
}
</style>
