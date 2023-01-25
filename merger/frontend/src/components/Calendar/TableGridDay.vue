<template>
    <div class="
    pt-1.5 
    m-1 
    rounded-md 
    text-center 
    w-10 
    h-10 
    border
    border-transparent
    text-center 
    hover:cursor-pointer
    hover:bg-indigo-100 border" 
    :class="`
        ${styleCurrentDay(cursor)  ? 'ring-2 ring-offset-2 ring-indigo-500': null}
        ${styleSelectedDay(cursor) ? 'bg-indigo-200 border border-indigo-300' : null}`"
    @click="$emit('daySelected', cursor)">
        <p class="
        prevent-select" 
        :class="`
            ${styleRedDay(cursor, props.DateTime.month) ? 'text-red-600' : '' }
            ${styleCurrentDay(cursor) ? 'font-semibold' : '' }`">
            {{cursor}}
        </p>

        <div class="flex justify-center">
            <div class="bg-emerald-400 w-1.5 h-1.5 rounded-full">
            </div>
        </div>
        
        
        
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    DateTime: {
        type: Object,
        required: true
    },
    cursor: {
        type: Number,
        required: true
    },
    holidays: {
        type: Array,
        required: true
    }

})

function styleCurrentDay(day){
    if (day == props.DateTime.current_day && 
        props.DateTime.month == props.DateTime.current_month && 
        props.DateTime.year == props.DateTime.current_year) {
        return true
    }
}

function styleSelectedDay(day){
    if (day == props.DateTime.day) {
        return true
    }
}

function styleRedDay(day, month){
    const day_week = new Date(props.DateTime.year, props.DateTime.month, day).getUTCDay()
    if (day_week == 5 || day_week == 6) {
        return true
    }
    for (let i = 0; i < props.holidays.length; i++) {
        const element = props.holidays[i];
        if (day == element['day'] && month == element['month']) {
            return true
        }
        
    }
}
    
</script>