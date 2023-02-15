<template>
  <div>
    <div class="card-component">
      <HeaderDate
        class="header-list"
        :data="Time"
        @prev-month="datePreMonth()"
        @next-month="dateNexMonth()"
      />

      <div class="list-contaner">
        <div class="compnent-list-day">
          <div v-for="day in dateDaysInMonth()" :key="day">
            <BodyDate
              :date="Time"
              :day="day"
              :currentDay="dateGetCurrentDate(day)"
              :dayName="dateDayName(day)"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.card-component {
  width: 100%;
  min-width: 14rem;
  box-shadow: -0px -5px 10px 0px rgb(73, 73, 73);
  
  .header-list {
    box-shadow: 10px 10px 1rem -15px rgb(73, 73, 73);
  }

  .list-contaner{
    overflow-y: auto;
    direction: rtl;
    height: 92.5vh;

    .compnent-list-day {
      direction: ltr;
    }
  }
  
}
/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 1rem;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
  border-radius: 5rem;
}
</style>







<script>
import HeaderDate from "./HeaderYear.vue";
import BodyDate from "./BodyComponent.vue";

const date = new Date();

export default {
  components: {
    HeaderDate,
    BodyDate,
  },
  data() {
    return {
      Time: date,
      SelectYear: date.getFullYear(),
    };
  },
  computed: {},

  watch: {
    SelectYear() {
      this.Time = new Date(
        this.SelectYear,
        this.Time.getMonth(),
        this.Time.getDate()
      );
    },
  },

  methods: {
    dateNexMonth: function () {
      this.Time = new Date(this.Time.getFullYear(), this.Time.getMonth() + 1);
    },

    datePreMonth: function () {
      this.Time = new Date(this.Time.getFullYear(), this.Time.getMonth() - 1);
    },

    dateDaysInMonth: function () {
      return new Date(
        this.Time.getFullYear(),
        this.Time.getMonth() + 1,
        0
      ).getDate();
    },

    dateDayName: function (day) {
      return new Date(
        this.Time.getFullYear(),
        this.Time.getMonth(),
        day
      ).toLocaleString("default", { weekday: "long" });
    },

    dateGetCurrentDate: function (day) {
      const instace = new Date(
        this.Time.getFullYear(),
        this.Time.getMonth(),
        day
      );
      if (
        instace.getFullYear() == date.getFullYear() &&
        instace.getMonth() == date.getMonth() &&
        instace.getDate() == date.getDate()
      ) {
        return true;
      }
    },
  },
};
</script>