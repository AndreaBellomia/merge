<template>
  <div class="flex-row max-w-max">
    <div v-if="prenotationProgress == 0" class="">
      <div class="custom-grid-org prevent-select">
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
          class=""
          :DateTime="DateTime"
          :QueryInsace="QueryInsace"
          :monthName="monthName"
          :dayName="dayName"
          @day-query="(qury) => (QuerrySelected = qury)"
        />
      </div>
      <div class="custom-btn-container">
        <CalendarConfirm
          @next-page="prenotationProgress++"
          :nextPageBool="nextPageCeck()"
          :btnMsg="'Conferma'"
          :errorMsg="'Seleziona una data'"
        />
      </div>
    </div>
    <div v-else-if="prenotationProgress == 1">
      <FormBooking
        :QuerrySelected="QuerrySelected"
        :monthName="monthName"
        :dayName="dayName"
        @form-is-valid="(formValid) => (formValidated = formValid)"
      />
      <div class="custom-btn-container">
        <CalendarConfirm
          @next-page="confirmPrenotation(formValidated)"
          @back-page="prenotationProgress--"
          :nextPageBool="formValidated.status"
          :btnMsg="'Prenota'"
          :errorMsg="'Inserisci le informazioni richieste'"
          :backActive="true"
        />
      </div>
    </div>
    <div v-else-if="prenotationProgress == 3">
      <ConfirmPage
      :prenotation="QuerrySelected"
      :monthName="monthName"
      :dayName="dayName"
      @back-home="prenotationProgress = 0"
      />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.custom-btn-container {
  display: flex;
  justify-content: flex-end;
}

.custom-grid-org {
  display: flex;
  flex-direction: row;
}

.prevent-select {
  -webkit-user-select: none; /* Safari */
  -ms-user-select: none; /* IE 10 and IE 11 */
  user-select: none; /* Standard syntax */
}
.centered {
  position: fixed; /* or absolute */
  top: 25%;
  left: 25%;
}

@media only screen and (max-width: 885px) {
  .custom-btn-container {
    justify-content: center;
  }
  .custom-grid-org {
    display: flex;
    flex-direction: column;
  }
}
</style>


    
<script>
import axios from "axios";

import CalendarDay from "./CalendarDay.vue";
import CalendarTable from "./CalendarTable.vue";
import CalendarConfirm from "./CalendarConfirm.vue";
import FormBooking from "./FormBooking.vue";
import ConfirmPage from "./ConfirmPage.vue"

const date = new Date();

export default {
  components: {
    CalendarDay,
    CalendarTable,
    CalendarConfirm,
    FormBooking,
    ConfirmPage,
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

      QuerrySelected: undefined,

      formValidated: Object,

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
        { day: 1, month: 0 },
      ],

      prenotationProgress: 0,
    };
  },

  mounted() {
    this.getHTTP_appointment();
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

    nextPageCeck: function () {
      try {
        if (this.QuerrySelected.id) {
          return false;
        }
        return true;
      } catch (error) {
        return true;
      }
    },

    confirmPrenotation: function (form) {
      this.prenotationProgress++;
      this.postHTTP_appointment(form.body, form.title, this.QuerrySelected.id);
    },

    postHTTP_appointment: function (val_desc, val_type, val_app) {
      axios
        .post("/api/booking/", {
          description: val_desc,
          type: val_type,
          appointments: val_app,
        })
        .then((response) => {
          if (response.status == 201) {
            this.prenotationProgress++
            console.log(response)
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getHTTP_appointment: function () {
      axios
        .get("api/appointments/?format=json")
        .then((response) => {
          this.QueryInsace = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
