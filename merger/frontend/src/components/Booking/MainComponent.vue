<template>
  <div>
    <div class="main-container">
      <div class="mb-4 border-b border-gray-200">
        <ul
          class="flex flex-wrap -mb-px text-sm font-medium text-center"
          id="myTab"
          data-tabs-toggle="#myTabContent"
          role="tablist"
        >
          <li class="mr-2" role="presentation">
            <button
              class="
                inline-block
                p-4
                rounded-t-lg
                hover:text-gray-600 hover:border-gray-300
              "
              type="button"
              :class="`${page == 'calendar' ? 'border-b-2 border-b-indigo-500 text-blue-500' : 'border-b-2 border-transparent'}`"
              @click="page = 'calendar'"
            >
              Calendario
            </button>
          </li>
          <li class="mr-2" role="presentation">
            <button
              class="
                inline-block
                p-4
                border-b-2 border-transparent
                rounded-t-lg
                hover:text-gray-600 hover:border-gray-300
              "
              type="button"
              :class="`${page == 'booking' ? 'border-b-2 border-b-indigo-500 text-blue-500' : 'border-b-2 border-transparent'}`"
              @click="page = 'booking'"
            >
              Prenotazioni
            </button>
          </li>
        </ul>
      </div>


      <div class="main-container">
        <div v-show="page == 'calendar'">
          <Calendar />
        </div>
        <div v-show="page == 'booking'">
          <BookingList />
        </div>
      </div>


    </div>
  </div>
</template>


<style lang="scss" scoped>
.main-container{
  max-width: 813px;
}

</style>


<script>
import BookingList from "./BookingList/BookingMain.vue";
import Calendar from "./Calendar/CalendarMain.vue";

export default {
  components: {
    BookingList,
    Calendar,
  },
  data() {
    return {
      page: 'calendar',
    };
  },
};
</script>
