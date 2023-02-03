<template>
  <div
    class="
      bg-sky-50
      rounded-lg
      border border-sky-100
      main-container
    "
  >
    <div class="px-12">
      <div
        class="
          container-header
          text-slate-800
          font-bold
        "
      >
        <div class="header">
          <p class="text-5xl pb-1 justify-self-end prevent-select">
            {{ this.DateTime.day }}
          </p>
          <p class="pt-1 pl-1 prevent-select">
            {{ this.monthName[this.DateTime.month] }}
          </p>
          <p class="pb-1 pl-1 prevent-select">
            {{ getWeekDey(this.DateTime.day) }}
          </p>
        </div>
      </div>
      
    </div>
    <hr class="mx-5">
    
    <div class="custom-container-title">
        
        <h2 class="font-semibold text-slate-500">
          Appuntamenti
        </h2>
    
    </div>
    <div class="overflow-auto custom-container-body mb-2">
      <div v-for="(item, index) in this.QueryInsace" :key="index" class="mb-2 custom-card-app">

        <Appointment
          :item="item"
          :DateTime="DateTime"
          :monthName="monthName"
          :dayName="dayName"
          :selected="currentSelected(item)"
          @day-query="(qury) => ($emit('dayQuery', qury), this.current_select = qury)"
        />
      </div>
    </div>
    
  </div>
</template>


<style lang="scss" scoped>
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0);
}

::-webkit-scrollbar-thumb {
  background-color: #c6c6c6;
  border-radius: 20px;
}



.main-container{
  width: 100%;
  min-width: 400px;

  margin-top: 0rem;
  margin-left: 0.75rem;
  display: flex;
  flex-direction: column;

  
  .container-header{
    display: flex;
    justify-content: center;

    .header{
      display: flex;
      align-items: center;
    }


  }

  .custom-container-title{
    display: flex;
    justify-content: center;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
  }

  .custom-container-body{
    max-height: 20rem;
  }

}

@media only screen and (max-width: 768px) {
  .main-container{
    margin-top: 0.75rem;
    margin-left: 0rem;
    display: flex;
    flex-direction: column;
    justify-content: center;

    .container-header{
      display: flex;

    }
  }
}

</style>

<script>
import Appointment from "./DayAppointment.vue";

export default {
  props: {
    DateTime: {
      type: Object,
      required: true,
    },
    QueryInsace: {
      type: [Array, undefined],
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
  data(){
    return {
      current_select: Number
    }
  },
  components: {
    Appointment,
  },
  methods: {
    getWeekDey: function (day) {
      const number_of_day = new Date(
        this.DateTime["year"],
        this.QueryInsace["month"],
        day
      ).getUTCDay();
      return this.dayName[number_of_day];
    },

    currentSelected: function (item) {
      if (item.id == this.current_select.id) {
        return true
      }
      return false
    }

    
  },
};
</script>



<style scoped>



</style>
