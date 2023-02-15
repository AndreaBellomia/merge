<template>
  <div
    class="
      m-1
      rounded-md


      border border-transparent

      hover:cursor-pointer hover:bg-slate-200
      border
      cell-main-container
    "
    :class="`
        ${
          styleCurrentDay(cursor)
            ? 'ring-2 ring-offset-2 ring-sky-500'
            : null
        }
        ${
          styleSelectedDay(cursor)
            ? 'bg-sky-200 border border-sky-300 hover:bg-sky-300'
            : null
        }`"
    @click="$emit('daySelected', cursor)"
  >
    <p
      class="prevent-select"
      :class="`
            ${styleRedDay(cursor, this.DateTime.month) ? 'text-red-600' : ''}
            ${styleCurrentDay(cursor) ? 'font-semibold' : ''}`"
    >
      {{ cursor }}
    </p>

    <div class="flex justify-center">
      <div
        class="bg-emerald-400 w-1.5 h-1.5 rounded-full"
        v-if="ceckDayAppointment(cursor)"
      ></div>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.cell-main-container {
    aspect-ratio: 1 / 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: larger;

    max-height: 6rem;

    p {
        font-size: 1rem;
    }

}
</style>

<script >
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
    cursor: {
      type: Number,
      required: true,
    },
    holidays: {
      type: Array,
      required: true,
    },
  },
  methods: {
    styleCurrentDay: function (day) {
      if (
        day == this.DateTime.current_day &&
        this.DateTime.month == this.DateTime.current_month &&
        this.DateTime.year == this.DateTime.current_year
      ) {
        return true;
      }
    },

    styleSelectedDay: function (day) {
      if (day == this.DateTime.day) {
        return true;
      }
    },

    styleRedDay: function (day, month) {
      const day_week = new Date(
        this.DateTime.year,
        this.DateTime.month,
        day
      ).getUTCDay();
      if (day_week == 5 || day_week == 6) {
        return true;
      }
      for (let i = 0; i < this.holidays.length; i++) {
        const element = this.holidays[i];
        if (day == element["day"] && month == element["month"]) {
          return true;
        }
      }
    },

    ceckDayAppointment(crs) {
      const instace = this.QueryInsace;
      for (let item = 0; item < instace.length; item++) {
        const element = new Date(instace[item].start_time);
        if (
          crs == element.getDate() &&
          element.getMonth() == this.DateTime.month &&
          element.getFullYear() == this.DateTime.year
        ) {
          return true;
        }
      }
    },
  },
};
</script>