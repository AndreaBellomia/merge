<template>
  <div
    class="
      flex-row
      max-w-max
      justify-center
      m-2
      bg-sky-50
      rounded-lg
      border border-sky-100
    "
  >
    <div class="px-12">
      <div
        class="
          flex
          justify-center
          items-center
          text-slate-800
          font-bold
          w-80
          px-2
          mx-1
        "
      >
        <div class="grid grid-cols-2 justify-center items-center py-1">
          <p class="row-span-2 text-5xl pb-1 justify-self-end prevent-select">
            {{ this.DateTime.day }}
          </p>
          <p class="pt-1 pl-1 prevent-select">
            {{ this.monthName[this.DateTime.month] }}
          </p>
          <p class="pb-1 pl-1 prevent-select">
            {{ getWeekDey(this.DateTime.day) }}
          </p>
        </div>
      </div>
    </div>
    <hr class="mx-3" />
    <div class="flex flex-row justify-center max-w-full">
      <div class="flex flex-col max-w-max">
        <h2 class="justify-self-center font-semibold text-slate-500 py-1">
          Appuntamenti
        </h2>
      </div>
    </div>
    <div class="overflow-auto custom-height mb-2">
      <div v-for="(item, index) in this.QueryInsace" :key="index" class="mb-2">

        <Appointment
          
          :item="item"
          :DateTime="DateTime"
          :monthName="monthName"
          :dayName="dayName"
          :selected="currentSelected(item)"
          @day-query="(qury) => ($emit('dayQuery', qury), this.current_select = qury)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Appointment from "./DayAppointment.vue";

export default {
  props: {
    DateTime: {
      type: Object,
      required: true,
    },
    QueryInsace: {
      type: [Array, undefined],
      required: true,
    },
    monthName: {
      type: Array,
      required: true,
    },
    dayName: {
      type: Array,
      required: true,
    },
  },
  data(){
    return {
      current_select: Number
    }
  },
  components: {
    Appointment,
  },
  methods: {
    getWeekDey: function (day) {
      const number_of_day = new Date(
        this.DateTime["year"],
        this.QueryInsace["month"],
        day
      ).getUTCDay();
      return this.dayName[number_of_day];
    },

    currentSelected: function (item) {
      if (item.id == this.current_select.id) {
        return true
      }
      return false
    }

    
  },
};
</script>



<style scoped>
.custom-height {
  max-height: 20rem;
}

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(59, 57, 201, 0);
}

::-webkit-scrollbar-thumb {
  background-color: #4b48ff;
  border-radius: 20px;
}
</style>
