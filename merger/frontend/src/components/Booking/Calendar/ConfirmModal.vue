<template>
  <div>
    <div
      class="relative z-10"
      aria-labelledby="modal-title"
      role="dialog"
      aria-modal="true"
      :class="`${popUp ? '' : 'hidden'}`"
    >
      <div
        class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
      ></div>
      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div
          class="
            flex
            min-h-full
            items-end
            justify-center
            p-4
            text-center
            sm:items-center sm:p-0
          "
        >
          <div
            class="
              relative
              transform
              overflow-hidden
              rounded-lg
              bg-white
              text-left
              shadow-xl
              transition-all
              sm:my-8 sm:w-full sm:max-w-lg
            "
          >
            <div>
              <div class="bg-white px-4 pt-5 pb-4 p-6 pb-4">
                <div class="flex flex-col items-center p-1">
                  <div
                    class="
                      mx-auto
                      flex
                      p-8
                      flex-shrink-0
                      items-center
                      justify-center
                      rounded-full
                      bg-green-100
                      h-10
                      w-10
                    "
                  >
                    <span class="material-icons scale-150"> done </span>
                  </div>
                  <div class="mt-2 text-center sm:mt-0 ml-4 text-left pt-5">
                    <h3
                      class="text-lg font-medium leading-6 text-gray-900"
                      id="modal-title"
                    >
                      Prenotazione Avvenuta!
                    </h3>
                    <div class="mt-2">
                      <p>
                        La prenotazione per <strong
                          >{{ dataFormatted.dayname }} {{ dataFormatted.day }}
                          {{ dataFormatted.month }}</strong
                        ><br>
                        dalle
                        <strong>{{ dataFormatted.starttime }}</strong> alle
                        <strong>{{ dataFormatted.endtime }}</strong
                        > è avvenuta con successo
                      </p>
                      <br>
                      <hr>
                      <br>
                      <p>
                        Attendi la conferma della prenotazione, puoi consultare
                        lo stato dalla sezione prenotazioni
                      </p>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="
                  bg-gray-50
                  px-4
                  py-3
                  sm:flex sm:flex-row-reverse sm:px-6
                  justify-center
                "
              >
                <button
                  @click="$emit('closeModal')"
                  type="button"
                  class="
                    mt-3
                    inline-flex
                    w-full
                    justify-center
                    rounded-md
                    border border-gray-300
                    bg-white
                    px-4
                    py-2
                    text-base
                    font-medium
                    text-gray-700
                    shadow-sm
                    hover:bg-gray-50
                    focus:outline-none
                    focus:ring-2
                    focus:ring-indigo-500
                    focus:ring-offset-2
                    sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm
                  "
                >
                  Chiudi
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    popUp: {
      type: Boolean,
      required: true,
    },
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