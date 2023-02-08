<template>
  <div>
    <div class="p-5 rounded-lg">
      <div class="flex items-center col-span-2 justify-between px-4">
        <span
          v-if="true"
          class="material-icons cursor-pointer prevent-select text-3xl pt-1"
          @click="$emit('prevMonth')"
        >
          chevron_left
        </span>
        <div v-else class="w-5"></div>
        <h1 class="text-xl px-3 justify-self-center font-semibold capitalize">{{ data.toLocaleString('default', { month: 'long' }) }} {{  data.getFullYear() }}</h1>

        <span
          class="material-icons cursor-pointer prevent-select text-3xl pt-1"
          @click="$emit('nextMonth')"
        >
          chevron_right
        </span>
      </div>
      
    </div>
  </div>
</template>


<script>
export default {
    props: {
        data: {
            type: Object,
            required: true
        }
    },
    methods: {
      
    }
    


};
</script>