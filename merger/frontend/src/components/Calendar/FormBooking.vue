<template>
  <div class="flex-row">
    <div
      class="
        flex
        bg-sky-400
        text-slate-50
        justify-center
        px-5
        align-middle
        py-4
        text-2xl
        font-bold
        rounded-lg
        border border-sky-400
        mb-3
      "
    >
      <p>Crea Prenotazione</p>
    </div>

    <div class="custom-grid-form">
      <div class="custom-form-header">
        <div class="p-3 bg-sky-50 rounded-lg border border-sky-100">
          <div class="">
            <p class="text-2xl font-semibold">
              {{ this.dataFormatted.starttime }} -
              {{ this.dataFormatted.endtime }}
            </p>
            <p>
              {{ this.dataFormatted.dayname }} {{ this.dataFormatted.day }}
              {{ this.dataFormatted.month }}
            </p>
            <p class="text-sm">{{ this.dataFormatted.year }}</p>
          </div>
        </div>
        <div class="bg-sky-50 rounded-lg p-3 border border-sky-100">
          <label for="header" class="block mb-2 text-gray-900 font-semibold"
            >Titolo</label
          >
          <input
            type="text"
            name=""
            id="header"
            class="
              text-sm
              w-full
              rounded-lg
              p-2
              focus:ring-blue-500 focus:border-blue-500
              border border-gray-200
            "
            placeholder="Inserisci un titilo ..."
          />
        </div>
      </div>

      <div class="bg-sky-50 rounded-lg p-2 border border-sky-100">
        <label for="message" class="block mb-2 font-semibold text-gray-900"
          >Descrizione</label
        >
        <textarea
          id="message"
          rows="6"
          cols="108"
          class="
            block
            p-2.5
            w-full
            text-sm text-gray-900
            bg-neutral-50
            rounded-lg
            border border-gray-200
            focus:ring-blue-500 focus:border-blue-500
          "
          placeholder="Inserisci una descrizione ..."
        ></textarea>
      </div>
    </div>
  </div>
</template>


<style lang="scss" scoped>
.custom-grid-form {
  display: flex;
  flex-direction: column;
  
  .custom-form-header{
    display: flex;
  }
}

.prevent-select {
  -webkit-user-select: none; /* Safari */
  -ms-user-select: none; /* IE 10 and IE 11 */
  user-select: none; /* Standard syntax */
}

@media only screen and (max-width: 885px) {
  .custom-grid-form {
    .custom-form-header{
      flex-direction: column;
    }
  }
}
</style>

<script>
export default {
  props: {
    QuerrySelected: {
      type: Number,
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
  },
  data() {
    return {
      instace: Object,
      dataFormatted: undefined,
    };
  },
  methods: {
    selctAppoint: function () {
      for (let item = 0; item < this.QueryInsace.length; item++) {
        if (this.QueryInsace[item].id == this.QuerrySelected) {
          this.instace = this.QueryInsace[item];
        }
      }
    },
    formatData: function () {
      const date = new Date(this.instace.start_time);
      const date_end = new Date(this.instace.end_time);
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
  created() {
    this.selctAppoint();
    this.dataFormatted = this.formatData();
  },
};
</script>