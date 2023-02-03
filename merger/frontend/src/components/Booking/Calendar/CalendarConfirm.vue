<template>
  <div class="flex flex-col">
    <div class="flex flex-row-reverse">
      <button
        @click="$emit('nextPage')"
        :disabled="ceckDataSelected()"
        :class="`${
          !ceckDataSelected() ? 'hover:bg-blue-400 bg-blue-600' : 'bg-blue-300'
        }`"
        class="
          rounded-lg
          text-white
          font-semibold
          custom-button-next
          focus:ring-2
          ring-blue-3
          custom-btn-next
        "
      >
        {{ btnMsg }}
      </button>
      <button
        v-if="backActive"
        @click="$emit('backPage')"
        class="
          rounded-lg
          text-blue-600
          font-semibold
          custom-button-next
          focus:ring-2
          ring-blue-3
          border-2
          border-blue-600
          custom-btn-next
          hover:bg-blue-100 
          mr-4
        "
      >
      Indietro
      </button>
      
    </div>
    <p class="text-sm pl-3 mr-2" v-if="ceckDataSelected()">*{{ errorMsg }}</p>
    
  </div>
</template>

<style lang="scss" scoped>
.custom-button-next {
  margin-top: 0.5rem;
  padding: 0.5rem 2rem 0.5rem 2rem ;
  position: relative;
  float: right;
}
</style>

<script>
export default {
  props: {
    nextPageBool: {
      type: Boolean,
    },
    btnMsg: {
      type: String,
      required: true,
    },
    errorMsg: {
      type: String,
      required: true,
    },
    backActive: Boolean
  },
  methods: {
    ceckDataSelected() {
      if (this.nextPageBool) {
        return true;
      }
      return false;
    },
  },
};
</script>
