<template>
    <div class="custom-card">
        <div class="custom-card-container">
            <div class="flex flex-col items-start">
                <span class="custom-card-header">{{ formatData() }}
                </span>
                <span class="custom-card-text mb-4">{{ booking.appointments }}</span>
                <span class="custom-card-text">{{ booking.type }}</span>
            </div>
            <div class="flex flex-col items-center">
                <span class="custom-card-secondary-text">Id {{ booking.id }}</span>
                <span class="custom-card-icon material-symbols-outlined">
                    chevron_right
                </span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        booking: {
            type: Object,
            required: true
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
    },
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
    }
}
</style>

