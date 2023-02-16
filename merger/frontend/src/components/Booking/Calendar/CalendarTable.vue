<template>

  
  <div class="flex-column text-slate-800 text-start main-container">
    <div
      class="
        flex
        grid grid-cols-3
        py-3
        bg-sky-50
        rounded-lg
        border border-sky-100
        mb-3
      "
    >
      <h1 class="px-3 text-4xl font-bold">{{ this.DateTime["year"] }}</h1>

      <div class="flex items-center col-span-2 justify-between px-4">
        <span
          v-if="buttonPrevMonth()"
          class="material-icons cursor-pointer prevent-select text-3xl pt-1"
          @click="$emit('prevMonth')"
        >
          chevron_left
        </span>
        <div v-else class="w-5">
        </div>
        <h1 class="text-xl px-3 justify-self-center font-semibold">
          {{ this.monthName[this.DateTime["month"]] }}
        </h1>

        <span
          class="material-icons cursor-pointer prevent-select text-3xl pt-1"
          @click="$emit('nextMonth')"
        >
          chevron_right
        </span>
      </div>
    </div>


    <div
      class="
        bg-sky-50
        rounded-lg
        border border-sky-100
        container-calendar
      "
    >
      <div class="grid-calendar-container py-3 px-1 text-center">
        <div v-for="(item, index) in this.dayName" :key="index">
          <!-- item.slice(0, 3) -->
          <p class="font-semibold custom-text">{{ item }}</p>
        </div>
      </div>
      <hr />
      <div class="grid-calendar-container text-center px-1 text-black pb-1">
        <div
          v-for="(day, index) in getDaysInMonth()"
          :style="`${day == 1 ? 'grid-column-start: ' + getFirstDayInMonth(): ''}`"
          :key="index"
        >
          <TableGridDay
            class="transition ease-in-out"
            :DateTime="DateTime"
            :QueryInsace="QueryInsace"
            :cursor="day"
            :holidays="holidays"
            @day-selected="(value) => $emit('daySelected', value)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>



.main-container {
  width: 100%;
  min-width: 400px;
  .container-calendar{
    display: flex;
    flex-direction: column;
    padding: 0rem 2rem;
    padding-bottom: 1rem;

    .grid-calendar-container{
      padding-top: 1rem;
      display: grid;
      grid-template-columns: repeat(7, auto);
    }
  }
}

.custom-text {
  font-size: 0;
}
.custom-text::first-letter {
  font-size: 1rem !important;
}


</style>


<script>
import TableGridDay from "./TableGridDay.vue";
export default {
  props: {
    DateTime: {
      type: Object,
      required: true,
    },
    QueryInsace: {
      type: Object,
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
    holidays: {
      type: Array,
      required: true,
    },
  },
  components: {
    TableGridDay,
  },
  methods: {
    getDaysInMonth: function () {
      "Return a Nuber of day in a Month";
      return new Date(
        this.DateTime["year"],
        this.DateTime["year"] + 1,
        0
      ).getDate();
    },

    getFirstDayInMonth: function () {
      "Calculate a col of start";
      return (
        new Date(this.DateTime["year"], this.DateTime["month"], 1).getUTCDay() +
        1
      );
    },

    buttonPrevMonth: function () {
      if (this.DateTime["year"] == this.DateTime["current_year"] && this.DateTime["month"] == this.DateTime["current_month"]){
        return false
      }
      return true
    }
  },
};
</script>


