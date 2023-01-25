<template>
    <div class="flex bg-violet-600 text-slate-100 justify-end px-5 align-middle py-4 text-2xl" @click="$emit('nextPage')">
        <div v-if="appSelected">
            <p>Prosegui</p>
        </div>
        <div v-else>
            <p>Seleziona un appuntamento...</p>
        </div>
        <div v-if="appSelected">
            <span class="material-icons scale-150 pl-3 pt-1">
                chevron_right
            </span>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            appSelected: false,
        }
    }
}
</script>


