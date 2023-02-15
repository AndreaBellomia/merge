<template>
  <div class="main-container">
    <div
      class="
        bg-sky-50
        text-slate-700
        rounded-lg
        border border-sky-100
        mb-3
        contaner-headers
      "
    >
      <div class="text-2xl font-bold">
        <p>Crea Prenotazione</p>
      </div>
      <div class="headers-information">
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

    <div class="custom-grid-form">
      <div class="bg-sky-50 rounded-lg p-2 border border-sky-100 mb-2">
        <label for="header" class="block mb-2 text-gray-900 font-semibold">Titolo</label>
        <input
          @keyup="formValidateTitle()"
          :class="`${
            title.status || title.status == undefined ? '' : 'ring ring-red-500'
          }`"
          type="text"
          name=""
          id="header"
          class="w-full text-sm rounded-lg p-2 border border-gray-200"
          placeholder="Inserisci un titilo ..."
          v-model="title.content"
        />
        <p :class="`${title.status || title.status == undefined ? 'invisible' : 'visible'}`"
        class="text-red-500 font-semibold pt-1 text-sm">
          *Inserisci un titolo maggiore 15 caratteri
        </p>

        <label for="message" class="block mb-2 font-semibold text-gray-900">Descrizione</label>
        <textarea
          @keyup="formValidateText()"
          :class="`${
            bodycontent.status || bodycontent.status == undefined
              ? ''
              : 'ring ring-red-500'
          }`"
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
          v-model="bodycontent.content"
        ></textarea>
        <p
          :class="`${
            bodycontent.status || bodycontent.status == undefined
              ? 'invisible'
              : 'visible'
          }`"
          class="text-red-500 font-semibold pt-1 text-sm"
        >
          *Inserisci una descrizione
        </p>
      </div>
    </div>
  </div>
</template>


<style lang="scss" scoped>

.main-container{
  width: 100vw;
  max-width: 814px;

  .contaner-headers {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.25rem 1rem;

    .headers-information {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
    }
  }

  .custom-grid-form {
    display: flex;
    flex-direction: column;

    .custom-form-header {
      display: flex;
    }
  }

  .custom-container-lablel {
    width: 100%;
    padding: 0.75rem;
    margin-bottom: 0.75rem;
  }

  .custom-container-booking {
    display: flex;
    min-width: 32%;
    margin-bottom: 0.75rem;
    margin-right: 0.75rem;
  }

  .prevent-select {
    -webkit-user-select: none; /* Safari */
    -ms-user-select: none; /* IE 10 and IE 11 */
    user-select: none; /* Standard syntax */
  }
}

</style>

<script>
export default {
  emits: ["formIsValid"],
  props: {
    QuerrySelected: {
      type: Object,
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
      title: {
        content: "",
        status: undefined,
      },
      bodycontent: {
        content: "",
        status: undefined,
      },
    };
  },
  watch: {
    formIsValidated() {},
  },

  computed: {
    formIsValidated: function () {
      if (this.title.status === true && this.bodycontent.status === true) {
        return this.$emit("formIsValid", {
          title: this.title.content,
          body: this.bodycontent.content,
          status: false,
        });
      }
      return this.$emit("formIsValid", { status: true });
    },
  },

  methods: {
    formValidateTitle: function () {
      if (this.title.content.length <= 15) {
        this.title.status = false;
      } else {
        this.title.status = true;
      }
    },

    formValidateText: function () {
      if (this.bodycontent.content.length <= 15) {
        this.bodycontent.status = false;
      } else {
        this.bodycontent.status = true;
      }
    },

    formatData: function () {
      const date = new Date(this.QuerrySelected.start_time);
      const date_end = new Date(this.QuerrySelected.end_time);
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
  setup() {},
  created() {
    this.dataFormatted = this.formatData();
    this.formValideStatus;
  },
};
</script>