<template>
  <div class="
  flex 
  flex-col
  bg-neutral-100
  max-w-max
  md:flex-row
  prevent-select
  transition ease-in-out">
    <CalendarTable
      class=""
      :DateTime="DateTime"
      :monthName="monthName"
      :dayName="dayName"
      :holidays="holidays"
      @next-month="nextMonth()"
      @prev-month="prevMonth()"
      @day-selected="(value) => DateTime.day = value"
    />
    <calendarDay
      class="transition ease-in-out"
      :DateTime="DateTime"
      :monthName="monthName"
      :dayName="dayName"
    />
  </div>
</template>
    


<script setup>
import { reactive} from "vue";
import CalendarTable from "./CalendarTable.vue";
import CalendarDay from "./CalendarDay.vue";

const date = new Date();

const DateTime = reactive({
  year: date.getFullYear(),
  month: date.getMonth(),
  day: date.getDate(),

  current_year: date.getFullYear(),
  current_month: date.getMonth(),
  current_day: date.getDate(),
});

const monthName = [
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
];
const dayName = [
  "Lunedì",
  "Martedì",
  "Mercoledì",
  "Giovedì",
  "Venerdì",
  "Sabato",
  "Domenica",
];
// const dayName = [
//   "Lun",
//   "Mar",
//   "Mer",
//   "Gio",
//   "Ven",
//   "Sab",
//   "Dom",
// ];
const holidays = [
  { day: 25, month: 11 },
  { day: 31, month: 9 },
  { day: 15, month: 7 },
];

function updateData() {
  const formatte = new Date(
    DateTime["year"],
    DateTime["month"],
    DateTime["day"]
  );
  DateTime["year"] = formatte.getFullYear();
  DateTime["month"] = formatte.getMonth();
  DateTime["day"] = formatte.getDate();
}

function prevMonth() {
  DateTime.month--;
  DateTime.day = new Date(DateTime.year, DateTime.month + 1, 0).getDate();
  updateData();
}

function nextMonth() {
  DateTime.month++;
  DateTime.day = 1;
  updateData();
}

</script>

<style>
.prevent-select {
    -webkit-user-select: none; /* Safari */
    -ms-user-select: none; /* IE 10 and IE 11 */
    user-select: none; /* Standard syntax */
}

</style>

