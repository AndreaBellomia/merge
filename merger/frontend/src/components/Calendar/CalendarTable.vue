<template>
    <div class="
    flex-column 
    max-h-max 
    max-w-max 
    text-slate-100 
    text-start 
    ">
        <div class="flex grid grid-cols-3 py-3 bg-violet-600 ">

            <h1 class="px-3 text-4xl font-bold">{{props.DateTime['year']}}</h1>

            
            <div class="flex items-center col-span-2 justify-between px-4">
                <span class="material-icons cursor-pointer prevent-select text-3xl pt-1" 
                    @click="$emit('prevMonth')">
                    chevron_left
                </span>
                <h1 class="text-xl px-3 justify-self-center font-semibold">{{ props.monthName[props.DateTime['month']] }}</h1>
                
                <span class="material-icons cursor-pointer prevent-select text-3xl pt-1" @click="$emit('nextMonth')">
                    chevron_right
                </span>
            </div>
        </div>
        <div class="bg-neutral-100 text-slate-500 px-10">
            <div class="grid grid-cols-7 py-2 px-1 text-center">
                <div v-for="(item, index) in props.dayName" 
                :key="index">
                <!-- item.slice(0, 3) -->
                    <p class="font-semibold custom-text">{{ item }}</p>
                </div>
            </div>
            <div class="grid grid-cols-7 text-center px-1 text-black pb-1 pt-1">
                <div v-for="(day, index) in getDaysInMonth()" 
                :style="`
                    ${day == 1 ? 'grid-column-start: ' + getFirstDayInMonth() : '' }`" 
                :key="index">
                    <TableGridDay class="transition ease-in-out"
                    :DateTime="props.DateTime" 
                    :cursor="day" 
                    :holidays="props.holidays"
                    @day-selected="(value) => $emit('daySelected', value)"/>       
                </div> 
            </div>
        </div>

    </div>


</template>


<script setup>
import { defineProps } from 'vue'
import TableGridDay from './TableGridDay.vue'

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
    },
    holidays: {
        type: Array,
        required: true
    }
})

function getDaysInMonth() {
    "Return a Nuber of day in a Month"
    return new Date(props.DateTime['year'], props.DateTime['month'] + 1, 0).getDate()
}

function getFirstDayInMonth(){
    "Calculate a col of start"
    return new Date(props.DateTime['year'], props.DateTime['month'], 1).getUTCDay()+1
}


</script>
<style lang="scss" scoped>
.custom-text{
    font-size: 0;
}
.custom-text::first-letter{
    font-size: 1rem !important;
}
</style>

