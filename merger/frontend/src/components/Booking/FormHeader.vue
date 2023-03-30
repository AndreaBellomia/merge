<template>
    <div :class="[styles.flexCenter, styles.header, styles.padding, 'flex-col bg-primary']">
        <span :class="[styles.heading1, 'text-white']">{{ formatData().formatDateString }}</span>
        <span :class="[styles.heading2, 'text-white']"><span :class="[styles.heading2, 'text-secondary']">{{
            formatData().starttimeHours
        }}</span>:{{ formatData().starttimeMinutes }} - <span :class="[styles.heading2, 'text-secondary']">{{
    formatData().endtimeHours
}}</span>:{{ formatData().endtimeMinutes }}</span>
        <span class="border-b border-white w-40 mb-2">_</span>
        <span :class="[styles.heading2, 'text-white']">{{ bookingData.owner }}</span>
        <span v-if="state != ''"
            :class="[styles.heading2, getColorByState(state), 'text-black rounded-full mt-8 px-10 py-2']">{{ state
            }}</span>
    </div>
</template>

<script>
import { styles } from '@/assets/css';
export default {
    props: {
        booking: {
            type: Object,
            required: true
        },
        state: {
            type: String,
            default: ''
        }
    },
    data() {
        return {
            styles: styles,
            bookingData: ''
        }
    },
    watch: {
        booking(newValue) {
            this.bookingData = newValue
        },
    },
    methods: {
        formatData: function () {
            const date = new Date(this.bookingData.start_time);
            const date_end = new Date(this.bookingData.end_time);
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
                formatDateString: `${date.toLocaleString('default', { weekday: 'long' })} ${date.getDate()} ${date.toLocaleString('default', { month: 'long' })}`,
                starttimeHours: date.getHours(),
                starttimeMinutes: minutes(date),
                endtimeHours: date_end.getHours(),
                endtimeMinutes: minutes(date_end)
            };
        },
        getColorByState(state) {
            if (state == "Confermato")
                return 'bg-greenCustom'
            else if (state == "In Attesa")
                return 'bg-orangeCustom'
            else
                return 'bg-redCustom'
        }
    }
}
</script>