<template>
  <div
    class="
      pt-1.5
      m-1
      rounded-md
      text-center
      w-10
      h-10
      border border-transparent
      text-center
      hover:cursor-pointer hover:bg-indigo-100
      border
    "
    :class="`
        ${
          styleCurrentDay(cursor)
            ? 'ring-2 ring-offset-2 ring-indigo-500'
            : null
        }
        ${
          styleSelectedDay(cursor)
            ? 'bg-indigo-200 border border-indigo-300'
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