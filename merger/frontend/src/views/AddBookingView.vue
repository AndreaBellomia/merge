<template>
    <div>  
        <main>
            <div class="custom-calendar-background">
                <div class="custom-calendar-container">
                    <div class="custom-header">
                        <span @click="previousDate()" class="custom-arrow material-symbols-outlined">
                            chevron_left
                        </span>
                        <span>
                            <span class="custom-year mr-3">{{ date.getFullYear() }}</span>
                            <span class="custom-month">{{ date.toLocaleDateString("default", { month: 'long' }) }}</span>
                        </span>
                        <span @click="nextDate()" class="custom-arrow material-symbols-outlined">
                            chevron_right
                        </span>
                    </div>
                    <div class="custom-calendar-main">

                        <div class="custom-grid-calendar">
                            <div class="custom-header-col" v-for="day in 7" :key="day"
                                :class="`${day == 6 || day == 7 ? 'custom-holiday' : ''}`">{{ getDayName(day) }}</div>

                            <div class="custom-item" v-for="day in getDayNumberOfMonth()" :key="day"
                                :style="`${day == 1 ? 'grid-column-start: ' + getFirstDayOfMonth() : ''}`"
                                :class="`${day == daySelected ? 'custom-select' : ''}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ${styleRedDay(day) ? 'custom-holiday' : ''}`"
                                @click="setdate(day)">{{
                                    day }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex flex-col mt-6 mb-32">
                <span class="custom-tilte-appointments">Appuntamenti</span>
                <AppointmentsAvailableListItem v-for="appointment in appointmentsSelected" :key="appointment"
                    :appointment=appointment>
                </AppointmentsAvailableListItem>
            </div>
        </main>
        <nav class="custom-fb-container flex flex-col items-start m-1">
            <FloatingActionButton :routerLink="'/MyBookingView'" :icon="'undo'"/>
        </nav>
    </div>
</template>

<script>
import axios from 'axios';
import AppointmentsAvailableListItem from '../components/Booking/AppointmentsAvailableListItem.vue'
import FloatingActionButton from '../components/Booking/FloatingActionButton.vue'

export default {
    components: {
        AppointmentsAvailableListItem,
        FloatingActionButton,
    },
    data() {
        return {
            appointments: [],
            date: this.getCurrentDate(),
            daySelected: undefined,
            appointmentsSelected: [],
        }
    },
    mounted() {
        this.getHTTP_appointmentsList()
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
            this.daySelected = new Date(this.date.getFullYear(), this.date.getMonth(), -1).getDate()+1
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
        getHTTP_appointmentsList() {
            axios
                .get("api/client/appointments/")
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

<style scoped lang="scss">
.custom-calendar-background {
    display: flex;
    min-width: 400px;
    justify-content: center;
    background: #1F1F1F;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.4);
    border-radius: 0px 0px 28px 28px;
    padding-bottom: 4rem;
    padding-right: 4rem;
    padding-left: 4rem;

    .custom-calendar-container {
        .custom-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem;

            .custom-arrow {
                font-size: 2.2rem;
                color: #F8FCFF;
                -webkit-user-select: none;
                cursor: pointer;
            }

            .custom-year {
                font-style: normal;
                font-weight: 500;
                font-size: 1.8rem;
                line-height: 29px;
                color: #F8FCFF;
            }

            .custom-month {
                font-style: normal;
                font-weight: 500;
                font-size: 1.8rem;
                line-height: 29px;
                color: #A771FF;
            }
        }

        .custom-calendar-main {
            display: flex;
            justify-content: center;

            .custom-grid-calendar {
                display: grid;
                gap: 0.5rem;
                grid-template-columns: repeat(7, auto);

                .custom-header-col {
                    aspect-ratio: 2 / 1;
                    text-align: center;
                    font-style: normal;
                    font-weight: 300;
                    font-size: 1rem;
                    line-height: 18px;
                    color: #F8FCFF;
                }

                .custom-item {
                    aspect-ratio: 1 / 1;
                    width: 2.5rem;
                    color: #F8FCFF;
                    display: flex;
                    justify-content: center;
                    align-items: center;

                    border-radius: 10rem;

                    font-weight: 500;
                    font-size: 1rem;
                    cursor: pointer;


                    &:hover {
                        background-color: #313131;
                    }
                }

                .custom-holiday {
                    color: #ff0000;
                }

                .custom-select {
                    background-color: #8C60D4;
                    color: #ffffff;
                }
            }
        }
    }
}

.custom-tilte-appointments {
    color: #000000;
    font-style: normal;
    font-weight: 600;
    font-size: 1.4rem;
    line-height: 19px;
    text-align: center;
}

.custom-fb-container {
  position: absolute;
  bottom: 8rem;
  left: 1.5rem;
  display: flex;
  flex-direction: column;
}
</style>