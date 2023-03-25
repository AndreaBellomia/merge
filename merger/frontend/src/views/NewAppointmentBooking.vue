<template>
    <!-- Calendar -->
    <div :class="[styles.flexCenter, 'flex-col min-w-400 bg-primary shadow-md rounded-b-lg pb-16 mb-8']">
        <div :class="[styles.flexCenter, styles.paddingX, 'py-6']">
            <span @click="previousDate()"
                :class="[styles.heading1, 'text-white select-none cursor-pointer material-symbols-outlined sm:hover:text-secondary active:text-secondary mx-2']">chevron_left
            </span>
            <span>
                <span :class="[styles.heading1, 'text-white mr-3']">{{ date.getFullYear() }}</span>
                <span :class="[styles.heading1, 'text-secondary']">{{ date.toLocaleDateString("default", { month: 'long' })
                }}</span>
            </span>
            <span @click="nextDate()"
                :class="[styles.heading1, 'text-white select-none cursor-pointer material-symbols-outlined sm:hover:text-secondary active:text-secondary mx-2']">
                chevron_right
            </span>
        </div>
        <div :class="[styles.flexCenter]">
            <div class="grid grid-cols-7 gap-2">
                <div style="padding-bottom: 50%;" v-for="day in 7" :key="day"
                    :class="[styles.heading3, 'relative text-center text-white', `${day == 6 || day == 7 ? 'text-redCustom' : ''}`]">
                    {{
                        getDayName(day) }}</div>

                <div v-for="day in getDayNumberOfMonth()" :key="day"
                    :style="`${day == 1 ? 'grid-column-start: ' + getFirstDayOfMonth() : ''}`"
                    :class="[styles.flexCenter, styles.heading3, `${day == daySelected ? 'text-white bg-secondary' : ''}`, `${styleRedDay(day) ? 'text-redCustom' : ''}`, 'w-10 h-10 text-white hover:bg-primaryVariant rounded-full cursor-pointer select-none']"
                    @click="setdate(day)">{{
                        day }}
                </div>
            </div>
        </div>
    </div>
    <!-- Appointment List -->
    <h2 :class="[styles.heading2, 'text-center']">Appuntamenti</h2>
    <div :class="[styles.flexCenter, styles.paddingY, 'flex-col mb-44']">
        <CardAppointment v-for="appointment in appointmentsSelected" :key="appointment" :appointment=appointment>
        </CardAppointment>
    </div>
    <!-- Floating Action Button -->
    <div :class="[styles.flexStart, styles.margin, styles.floatingActionButtonPositionLeft]">
        <FloatingActionButton :destination="'/booking'" :icon="iconBack" />
    </div>
</template>

<script>
import axios from 'axios';
import CardAppointment from '../components/Booking/CardAppointment.vue'
import FloatingActionButton from '../components/FloatingActionButton.vue'
import { ArrowUturnLeftIcon } from '@heroicons/vue/24/solid'
import { styles } from '@/assets/css';

export default {
    components: {
        CardAppointment,
        FloatingActionButton,
    },
    data() {
        return {
            styles: styles,
            iconBack: ArrowUturnLeftIcon,
            appointments: [],
            appointmentsSelected: [],
            date: this.getCurrentDate(),
            daySelected: undefined,
        }
    },
    mounted() {
        this.getAppointments()
    },
    methods: {
        getCurrentDate: function () {
            const date = new Date()
            return date
        },
        nextDate: function () {
            this.daySelected = 1
            this.date = new Date(this.date.getFullYear(), this.date.getMonth() + 1, this.daySelected)
            this.getAppointmentsOfDateSelected()
        },
        previousDate: function () {
            this.daySelected = new Date(this.date.getFullYear(), this.date.getMonth(), -1).getDate() + 1
            this.date = new Date(this.date.getFullYear(), this.date.getMonth() - 1, this.daySelected)
            this.getAppointmentsOfDateSelected()
        },
        getDayNumberOfMonth: function () {
            return new Date(this.date.getFullYear(), this.date.getMonth() + 1, 0).getDate()
        },
        getFirstDayOfMonth: function () {
            return new Date(this.date.getFullYear(), this.date.getMonth(), 1).getUTCDay() + 1
        },
        getDayName: function (day) {
            return new Date(2022, 7, day).toLocaleString('default', { weekday: 'short' })
        },
        styleRedDay: function (day) {
            const day_week = new Date(this.date.getFullYear(), this.date.getMonth(), day).getUTCDay();
            if (day_week == 5 || day_week == 6) {
                return true;
            }
        },
        getAppointments() {
            axios
                .get("/api/client/appointments")
                .then((response) => {
                    this.appointments = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        setdate: function (day) {
            this.daySelected = day
            this.date = new Date(this.date.getFullYear(), this.date.getMonth(), day)
            this.getAppointmentsOfDateSelected()
        },
        getAppointmentsOfDateSelected: function () {
            this.appointmentsSelected = []
            this.appointments.forEach(appointment => {
                const convertInDate = new Date(appointment.start_time)
                if (convertInDate.getFullYear() == this.date.getFullYear()
                    && convertInDate.getMonth() == this.date.getMonth()
                    && convertInDate.getDate() == this.date.getDate()) {
                    this.appointmentsSelected.push(appointment)
                }
            });
        }
    }
}
</script>