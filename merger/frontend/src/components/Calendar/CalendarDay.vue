<template>
    <div class="
    flex-row
    md:border-l
    border-slate-300
    max-w-max
    justify-center">
        <div class="
        bg-violet-600 px-12">

            <div class="flex 
            justify-center
            items-center 
            text-slate-100 
            font-bold 
            w-80 
            px-2 mx-1">
                <div class="grid grid-cols-2 justify-center items-center py-1">
                    <p class="row-span-2 text-5xl pb-1 justify-self-end prevent-select">{{ props.DateTime.day }}</p>
                    <p class="pt-1 pl-1 prevent-select">{{ props.monthName[props.DateTime.month] }}</p>
                    <p class="pb-1 pl-1 prevent-select">{{getWeekDey(props.DateTime.day)}}</p>
                </div>
            </div>
        </div>
        <div class="flex flex-row justify-center max-w-full">

            <div class="flex flex-col max-w-max">
                <h2 class="justify-self-center font-semibold text-slate-500 py-1">Appuntamenti</h2>
            </div>
        </div>
        <div class="overflow-auto custom-height mb-2">
            <Appointment/>
        </div>
        
         
        
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
import Appointment from './DayAppointment.vue'

const props = defineProps({
    DateTime: {
        type: Object,
        required: true
    },
    monthName: {
        type: Array,
        required: true
    },
    dayName: {
        type: Array,
        required: true
    }
})

function getWeekDey(day){
    const number_of_day = new Date(props.DateTime['year'], props.DateTime['month'], day).getUTCDay()
    return props.dayName[number_of_day]
}

</script>


<style scoped>
.custom-height {
    max-height: 20rem;
}

::-webkit-scrollbar {
    width: 10px;           
  }
  
::-webkit-scrollbar-track {
background: rgba(0, 0, 0, 0);       
}
  
::-webkit-scrollbar-thumb {
    background-color: #7c3aed;   
    border-radius: 20px;;     
}
</style>
