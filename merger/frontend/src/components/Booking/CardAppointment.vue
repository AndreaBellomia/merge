<template>
    <div :class="[styles.flexCenter, styles.padding, styles.card, styles.spaceBetweenX]">
        <div class="flex flex-col">
            <h2 :class="[styles.heading2,]">{{ formatData().starttime }} - {{
                formatData().endtime }}</h2>
            <h3 :class="[styles.heading3, 'mb-5']">{{ appointment.owner }}</h3>
        </div>
        <div class='flex flex-col'>
            <RouterLink :to="{
                name: 'FormAddBooking', params: {
                    id: appointment.id
                }
            }"> <span
                    :class="[styles.arrow]">chevron_right</span>
            </RouterLink>
        </div>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';
import { styles } from '@/assets/css';
export default {
    props: {
        appointment: {
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
            const date = new Date(this.appointment.start_time);
            const date_end = new Date(this.appointment.end_time);
            let day = date.getDay();
            if (day == 0) {
                day = 7;
            }
            function minutes(date) {
                let minut = undefined;
                if (date.getMinutes() === 0) {
                    minut = "00";
                }
                else {
                    minut = date.getMinutes();
                }
                return minut;
            }
            return {
                starttime: date.getHours() + ":" + minutes(date),
                endtime: date_end.getHours() + ":" + minutes(date_end),
            };
        },
    },
    components: { RouterLink }
}
</script>