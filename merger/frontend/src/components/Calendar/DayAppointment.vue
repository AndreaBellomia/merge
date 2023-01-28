<template>
  <div>
    <div
    
    v-if="ceckData(this.item['start_time'])"
    @click="$emit('dayQuery', this.item)"
    class="
      flex
      bg-sky-100
      border border-sky-200
      max-w-full
      mt-2
      mx-2
      rounded-lg
      hover:cursor-pointer hover:bg-sky-200
    "
  >
    <div class="flex-row">
      <div class="flex px-2 pt-1 text-xl font-semibold">
        <p>{{ dataFormattTime(this.item["start_time"]) }}</p>
        <p class="px-2 text-violet-800">-</p>
        <p>{{ dataFormattTime(this.item["end_time"]) }}</p>
      </div>
      <p class="px-2 pb-1 text-sm font-semibold text-neutral-600">
        {{ dataFormattDate(this.item["start_time"]) }}
      </p>
    </div>
    <div class="flex max-w-full items-center">
      <p class="pl-20 ml-10 font-semibold text-xl text-emerald-600" v-if="this.item['stato']">
        Disponibile
      </p>
    </div>
  </div>
  </div>
  
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
    DateTime: {
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
  methods: {
    dataFormattTime: function (date_time) {
      const date = new Date(date_time);
      let minut = "";
      if (date.getMinutes() === 0) {
        minut = "00";
      } else {
        minut = date.getMinutes();
      }
      return `${date.getHours()}:${minut}`;
    },
    dataFormattDate: function (date_time) {
      const date = new Date(date_time);
      return `${date.getDate()} ${this.monthName[date.getMonth()]}`;
    },

    ceckData: function (date_time) {
      const date = new Date(date_time);
      if (
        this.DateTime.day == date.getDate() &&
        this.DateTime.month == date.getMonth() &&
        this.DateTime.year == date.getFullYear()
      ) {
        return true;
      }
    },
  },
};
</script>