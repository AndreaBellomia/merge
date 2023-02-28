<template>
    <header class="custom-header flex flex-col p-8 items-center">
        <span class="custom-date">{{ formatData().formatDateString }}</span>
        <span class="custom-time"><span class="custom-time hours">{{ formatData().starttimeHours
        }}</span>:{{ formatData().starttimeMinutes }} - <span class="custom-time hours">{{ formatData().endtimeHours
}}</span>:{{ formatData().endtimeMinutes }}</span>
        <span class="custom-divider mb-2">_</span>
        <span class="custom-author">{{ bookingData.appointments }}</span>
        <span v-if="state != ''" class="custom-state-indication mt-8 px-10 py-2" :class="getColorByState(state)">{{ state
        }}</span>
    </header>
</template>

<script>
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
                return 'green'
            else if (state == "In Attesa")
                return 'orange'
            else
                return 'red'
        }
    }
}
</script>

<style scoped lang="scss">
.custom-header {
    background: #1F1F1F;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 0px 0px 28px 28px;

    .custom-date {
        color: #F8FCFF;
        font-style: normal;
        font-weight: 400;
        font-size: 1.6rem;
        line-height: 32px;
    }

    .custom-time {
        color: #F8FCFF;
        font-style: normal;
        font-weight: 500;
        font-size: 2.5rem;
        line-height: 48px;
    }

    .custom-time .hours {
        color: #A771FF;
    }

    .custom-divider {
        border-bottom: 1px solid #F8FCFF;
        width: 10rem;
    }

    .custom-author {
        font-style: normal;
        font-weight: 300;
        font-size: 1.6rem;
        line-height: 29px;
        color: #F8FCFF;
    }

    .custom-state-indication {
        background: #FFB800;
        color: #000000;
        font-style: normal;
        font-weight: 600;
        font-size: 1.2rem;
        line-height: 16px;
        border-radius: 100px;
    }

    .custom-state-indication.green {
        background: #1ABD00;
    }

    .custom-state-indication.orange {
        background: #FFB800;
    }

    .custom-state-indication.red {
        background: #FF1F00;
    }
}
</style>