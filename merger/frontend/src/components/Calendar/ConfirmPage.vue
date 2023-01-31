<template>
  <div>
    <div class="custom-container">
      <div class="flex items-baseline">
        <h1 class="text-xl pb-3 pr-2">Prenotazione per:</h1>
        <p class="text-xl pb-3">
          <strong
            >{{ dataFormatted.dayname }} {{ dataFormatted.day }}
            {{ dataFormatted.month }}</strong
          >
          dalle <strong>{{ dataFormatted.starttime }}</strong> alle
          <strong>{{ dataFormatted.endtime }}</strong>
        </p>
      </div>

      <p class="text-xl pb-10">Completata con <strong>successo!</strong></p>
      <span class="material-icons custom-icon text-blue-600 pb-10">
        task_alt
      </span>
      <p class="text-xl pb-10 italic">Attendi la conferma dell'appuntemento.</p>
      <h3>Torna al calendario</h3>
      <button
        @click="$emit('backHome')"
        class="
          rounded-lg
          text-white
          font-semibold
          custom-button-next
          focus:ring-2
          ring-blue-3
          custom-btn-next
          hover:bg-blue-400
          bg-blue-600
        "
      >
        Calendario
      </button>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.custom-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  .custom-icon {
    font-size: 10rem;
  }
  .custom-button-next {
    margin-top: 0.5rem;
    padding: 0.5rem 2rem 0.5rem 2rem;
    position: relative;
    float: right;
  }
  & > * {
    margin: auto;
  }
}
</style>



<script>
export default {
  props: {
    prenotation: {
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
  },

  data() {
    return {
      dataFormatted: this.formatData(),
    };
  },

  methods: {
    formatData: function () {
      const date = new Date(this.prenotation.start_time);
      const date_end = new Date(this.prenotation.end_time);
      let day = date.getDay();
      if (day == 0) {
        day = 7;
      }
      function minutes(date) {
        let minut = undefined;
        if (date.getMinutes() === 0) {
          minut = "00";
        } else {
          minut = date.getMinutes();
        }
        return minut;
      }
      return {
        dayname: this.dayName[day - 1],
        day: date.getDate(),
        month: this.monthName[date.getUTCMonth()],
        year: date.getFullYear(),
        starttime: date.getHours() + ":" + minutes(date),
        endtime: date_end.getHours() + ":" + minutes(date_end),
      };
    },
  },
};
</script>
