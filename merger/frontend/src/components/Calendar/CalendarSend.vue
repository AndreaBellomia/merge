<template>
  <div>
    <button 
    @click="$emit('nextPage')"
    :disabled="ceckDataSelected()"
    :class="`${!ceckDataSelected() ? 'hover:bg-blue-400 bg-blue-600': 'bg-blue-300'}`"
    class="
    rounded-lg
    text-white
    font-semibold
    align-middle
    custom-button-next
    focus:ring-2 ring-blue-3
    ">Conferma
    </button>
    <p class="text-sm pl-3" v-if="ceckDataSelected()">*Seleziona unda data</p>
    
  </div>

 
</template>

<script>
export default {
  props: {
    QuerrySelected: {
      type: [Number, undefined]
    }
  },
  methods: {
    ceckDataSelected(){
      if (this.QuerrySelected === undefined) {
        return true
      }
      return false
    }
  }
};
</script>

<style lang="scss" scoped>
.custom-button-next {
  margin: 0.25rem 0.5rem 0.25rem 0.5rem;
  padding: 0.5rem 2rem 0.5rem 2rem;
}
</style>

