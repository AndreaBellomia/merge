<template>
    <div class="flex">
        <div :class="[styles.marginY, 'border-' + getStateClass() + 'Custom', 'border-l-4 -mr-1']"></div>
        <div v-if="booking.stato != 'FREE'" :class="[styles.flexCenter, styles.padding, styles.card, styles.spaceBetweenX]">
            <div class="flex flex-col">
                <span :class="[styles.heading2, 'mb-2']">{{ formatData() }}</span>
                <span :class="[styles.heading3, 'mb-2']">{{ booking.appointments }}</span>
                <span>{{ booking.type }}</span>
            </div>

            <div class='flex flex-col'>
                <span :class="[styles.heading5, 'mb-8']">Id {{ booking.id }}</span>
                <RouterLink
                    :to="{ name: 'FormDetailsBooking', params: { id: booking.id, type: `edit-${getStateClass()}` } }">
                    <span
                        :class="[styles.heading1, ' cursor-pointer text-primary hover:text-secondary active:text-secondaryVariant material-symbols-outlined']">chevron_right</span>
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
import { styles } from '@/assets/css';
export default {
    props: {
        booking: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            styles: styles
        }
    },
    methods: {
        formatData: function () {
            const date = new Date(this.booking.start_time);
            const date_end = new Date(this.booking.end_time);
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
            return `   
                ${date.getHours() + ":" + minutes(date)} -
                ${date_end.getHours() + ":" + minutes(date_end)} | 
                ${date.toLocaleString('default', { weekday: 'long' })}
                ${date.getDate()} 
                ${date.toLocaleString('default', { month: 'long' })}`
        },
        getStateClass: function () {
            if (this.booking.stato == "BUSY") {
                return "green"
            } else if (this.booking.stato == "WAIT" || this.booking.stato == "PAUSE") {
                return "orange"
            } else {
                return "red"
            }
        }
    },
}
</script>