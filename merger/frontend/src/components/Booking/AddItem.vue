<template>
    <section>
        <CalendarPick></CalendarPick>
    </section>
    <section>
    </section>
    <nav class="custom-fb-container flex flex-col items-start m-1">
        <span @click="$emit('undoToBookingView')" class="custom-fb flex material-symbols-outlined">
            undo
        </span>
    </nav>
</template>

<script>
import CalendarPick from '../Booking/CalendarPick.vue'
export default {
    components: {
        CalendarPick,
    },
    props: {
        showAddItem: {
            type: Boolean,
            required: true
        }
    }
}
</script>

<style scoped lang="scss">
.custom-fb-container {
    position: fixed;
    bottom: 0;
    height: 18%;
    width: 100%;

    .custom-fb {
        width: 3rem;
        height: 3rem;
        border-radius: 50%;
        background: #8F62DA;
        box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.5);
        color: #F8FCFF;
        font-size: xx-large;
        padding-top: 0.5rem;
        padding-left: 0.5rem;
        margin-left: 2rem;
        margin-bottom: 1rem;
        cursor: pointer;
    }
}
</style>