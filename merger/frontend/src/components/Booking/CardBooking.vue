<template>
    <div class="flex">
        <div :class="[styles.marginY, getState('class'), 'border-l-4 border-orangeCustom -mr-1']"></div>
        <div v-if="booking.stato != 'FREE'" :class="[styles.flexCenter, styles.padding, styles.card, styles.spaceBetweenX]">
            <div class="flex flex-col">
                <h2 :class="[styles.heading2, 'mb-2']">{{ formatData() }}</h2>
                <h3 :class="[styles.heading3, 'mb-2']">{{ booking.appointments }}</h3>
                <h4 :class="[styles.heading4]">{{ booking.type }}</h4>
            </div>
            <div class='flex flex-col'>
                <h5 :class="[styles.heading5, 'mb-8']">Id {{ booking.id }}</h5>
                <RouterLink
                    :to="{ name: 'FormDetailsBooking', params: { id: booking.id, type: `${getState('routing')}` } }">
                    <span :class="[styles.arrow]">chevron_right</span>
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
        /**
         * Returns the appropriate CSS class or parameter of routing based on the current booking state.
         * 
         * @param {string} typeOfReturn The parameter of routing.
         * @returns {string} The appropriate CSS class.
         */
        getState: function (typeOfReturn) {
            const classPrefix = "border-"
            const classSuffixes = "Custom"
            const routingPrefix = "edit-"
            var bookingState = this.booking.state;
            var color

            if (bookingState === "BUSY") {
                color = "green"
            } else if (bookingState === "WAIT" || bookingState === "PAUSE") {
                color = "orange"
            } else {
                color = "red"
            }

            // Return a class if typeOfReturn is "class"
            if (typeOfReturn === "class") {
                return classPrefix + color + classSuffixes
            }
            // Return a routing string if typeOfReturn is "routing"
            else if (typeOfReturn === "routing") {
                return routingPrefix + color
            }
            else {
                return color
            }
        }
    },
}
</script>