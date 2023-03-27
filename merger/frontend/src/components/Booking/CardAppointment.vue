<template>
    <div :class="[styles.flexCenter, styles.padding, 'space-x-20 sm:space-x-96 shadow-md rounded-xl']">
        <div class="flex flex-col">
            <span :class="[styles.heading2,]">{{ formatData().starttime }} - {{
                formatData().endtime }}</span>
            <span :class="[styles.heading3, 'mb-5']">{{ appointment.owner }}</span>
        </div>
        <div class='flex flex-col'>
            <RouterLink :to="{
                name: 'FormAddBooking', params: {
                    id: appointment.id
                }
            }"> <span
                    :class="[styles.heading1, 'w-8 h-8 cursor-pointer text-primary hover:text-secondary active:text-secondaryVariant material-symbols-outlined']">chevron_right</span>
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