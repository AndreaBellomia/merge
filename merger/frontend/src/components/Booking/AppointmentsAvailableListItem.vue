<template>
    <div class="custom-card">
        <div class="custom-card-container">
            <div class="flex flex-col items-start">
                <span class="custom-card-header"> {{ formatData().starttime }} - {{ formatData().endtime }}
                </span>
                <span class="custom-card-text">{{ appointment.owner }}</span>
            </div>
            <div class="flex flex-col items-center">
                <RouterLink to="/FormBookingView">
                    <span class="custom-card-icon material-symbols-outlined">
                        chevron_right
                    </span>
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
    props: {
        appointment: {
            type: Object,
            required: true
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

<style scoped lang="scss">
.custom-card {
    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 14px;
    margin: 0.6rem;
    border-left: 8px solid #1ABD00;

    .custom-card-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 0.5rem;
    }

    .custom-card-header {
        font-style: normal;
        font-weight: 600;
        line-height: 19px;
        font-size: 1rem;
        margin: 0.5rem;
        margin-bottom: 0rem;
        color: #000000;
    }

    .custom-card-text {
        font-style: normal;
        font-weight: 400;
        font-size: 0.75rem;
        display: flex;
        align-items: center;
        text-align: center;
        margin: 0.5rem;
        color: #000000;
    }

    .custom-card-secondary-text {
        font-style: normal;
        font-weight: 300;
        font-size: 10px;
        line-height: 12px;
        color: #000000;
        margin: 0.5rem;
    }

    .custom-card-icon {
        margin: 1rem;
        font-size: 2.5rem;
        color: #5C5A60;
        -webkit-user-select: none;
        cursor: pointer;
    }
}
</style>

