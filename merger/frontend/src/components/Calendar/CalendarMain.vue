<template>
  <div class="flex-row max-w-max">
    <div v-if="prenotationProgress == 0" class="transition ease-in-out">
      <div
        class="
          flex flex-col
          bg-neutral-100
          max-w-max
          md:flex-row
          prevent-select
          transition
          ease-in-out
        "
      >
        <CalendarTable
          class=""
          :DateTime="DateTime"
          :QueryInsace="QueryInsace"
          :monthName="monthName"
          :dayName="dayName"
          :holidays="holidays"
          @next-month="nextMonth()"
          @prev-month="prevMonth()"
          @day-selected="(value) => (DateTime.day = value)"
        />

        <calendarDay
          class="transition ease-in-out"
          :DateTime="DateTime"
          :QueryInsace="QueryInsace"
          :monthName="monthName"
          :dayName="dayName"
        />
      </div>
      <CalendarConfirm @next-page="prenotationProgress ++"/>
    </div>
    <div v-else-if="prenotationProgress == 1">
      <FormBooking/>
    </div>
    
  </div>
</template>
    
<script>
import { getAPI } from "../../axios";

import CalendarDay from "./CalendarDay.vue";
import CalendarTable from "./CalendarTable.vue";
import CalendarConfirm from "./CalendarConfirm.vue";
import FormBooking from "./FormBooking.vue";

const date = new Date();

export default {
  components: {
    CalendarDay,
    CalendarTable,
    CalendarConfirm,
    FormBooking,
  },
  data() {
    return {
      DateTime: {
        year: date.getFullYear(),
        month: date.getMonth(),
        day: date.getDate(),

        current_year: date.getFullYear(),
        current_month: date.getMonth(),
        current_day: date.getDate(),
      },

      QueryInsace: [],

      monthName: [
        "Gennaio",
        "Febbraio",
        "Marzo",
        "Aprile",
        "Maggio",
        "Giuno",
        "Luglio",
        "Agosto",
        "Settembre",
        "Ottobre",
        "Novembre",
        "Dicenbre",
      ],

      dayName: [
        "Lunedì",
        "Martedì",
        "Mercoledì",
        "Giovedì",
        "Venerdì",
        "Sabato",
        "Domenica",
      ],

      holidays: [
        { day: 25, month: 11 },
        { day: 31, month: 9 },
        { day: 15, month: 7 },
      ],

      prenotationProgress: 0,
    };
  },

  methods: {
    updateData: function () {
      const formatte = new Date(
        this.DateTime["year"],
        this.DateTime["month"],
        this.DateTime["day"]
      );
      this.DateTime["year"] = formatte.getFullYear();
      this.DateTime["month"] = formatte.getMonth();
      this.DateTime["day"] = formatte.getDate();
    },

    prevMonth: function () {
      this.DateTime.month--;
      this.DateTime.day = new Date(
        this.DateTime.year,
        this.DateTime.month + 1,
        0
      ).getDate();
      this.updateData();
    },

    nextMonth: function () {
      this.DateTime.month++;
      this.DateTime.day = 1;
      this.updateData();
    },

    getHTTP_appointment: function () {
      getAPI("appointments/?format=json").then((response) => {
        this.QueryInsace = response.data;
      });
    },
  },

  created() {
    this.getHTTP_appointment();
  },
};
</script>


<style>
.prevent-select {
  -webkit-user-select: none; /* Safari */
  -ms-user-select: none; /* IE 10 and IE 11 */
  user-select: none; /* Standard syntax */
}
</style>

