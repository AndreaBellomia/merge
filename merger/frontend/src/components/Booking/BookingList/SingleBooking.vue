<template>
  <div>
    <div class="bg-sky-50 rounded-lg border border-sky-100 main-card">
      <div class="card-heder-contaner">
        <div class="data-title">
          <p class="pr-2 font-medium">{{ formatedData.day }}</p>
          <p class="pr-2 font-medium">{{ formatedData.month }}</p>
          <p class="font-medium">{{ formatedData.year }}</p>
        </div>
        <div class="time-title">
          <p class="text-xl font-semibold">{{ formatedData.starttime }} - {{ formatedData.endtime }}</p>
        </div>
      </div>
      <div class="card-body-contaner">
        <div class="flex flex-col left-title">
          <p class="custom-text-header font-semibold">{{this.instaceBooking.type }}</p>
          <div class="stato-infos">
            <span class="material-icons pr-2 text-slate-500">
              pending_actions
            </span>
            <p class="text-sm font-semibold px-2 py-0.5 rounded-sm" :class="`${formatedStatoColor[this.instaceBooking.stato]}`">{{ formatedStato[this.instaceBooking.stato] }}</p>   
          </div>
        </div>       
        <p class="text-sm text-slate-400 id-infos">id:{{ this.instaceBooking.id }}</p>
        
      </div>
      <button @click="$emit('deletBtn')" class="bg-red-500 text-slate-100 rounded-r-lg ml-1" v-if="this.instaceBooking.stato == 'WAIT'">
        <span class="material-icons py-6 px-2 align-top">
            delete
        </span>
      </button>

      <div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>

.main-card{
  display: flex;


  .card-heder-contaner{
    width: 30%;
    min-width: 12rem;
    max-width: 30rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-right: 1px solid black;


    .data-title{
      display: flex;
    }
    .time-title{
      padding: top;
    }
  }

  .card-body-contaner{
    display: flex;
    justify-content: space-between;
    padding: 0px 1%;
    width: 70%;
    min-width: 15rem;
    

    .left-title {
      display: flex;
      width: 100%;
      white-space: nowrap;
      overflow: hidden;
      
    }
    
    .stato-infos{
      display: flex;
      align-items: center;
      padding-top: 1rem;
      padding-bottom: 0.5rem;
    }

    .id-infos{
      display: inherit;
      align-items: end;
      padding-bottom: 0.5rem;
    }
  }
}



</style>


<script>
export default {
  props: {
    instaceBooking: {
      type: Object,
      required: true,
    },
    dayName: {
      type: Array,
      required: true,
    },
    monthName: {
      type: Array,
      required: true,
    },
  },

  data() {
    return {
      formatedData: this.formatData(),
      formatedStato: {
        FREE: 'Disponibile',
        WAIT: 'In Accetazione',
        BUSY: 'Confermato',
        BLOCK: 'Annullata',
        PAUSE: 'Sospeso',
      },
      formatedStatoColor: {
        FREE: '',
        WAIT: 'text-yellow-600 bg-yellow-100',
        BUSY: 'text-lime-600 bg-lime-100',
        BLOCK: 'text-red-500 bg-red-100',
        PAUSE: 'text-red-500 bg-red-100',
      }
    };
  },

  methods: {
    formatData: function () {
      const date = new Date(this.instaceBooking.start_time);
      const date_end = new Date(this.instaceBooking.end_time);
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