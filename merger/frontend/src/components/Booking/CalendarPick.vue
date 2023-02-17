<template>
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
                    <div class="custom-header-col" v-for="day in 7" :key="day" :class="`${styleRedDay(day+-2) ? 'custom-holiday': ''}`">{{ getDayName(day) }}</div>

                    <div class="custom-item" v-for="day in getDayNumberOfMonth()" :key="day"
                        :style="`${day == 1 ? 'grid-column-start: ' + getFirstDayOfMonth() : ''}`"
                        :class="`${day == select_day ? 'custom-select': ''}
                                 ${styleRedDay(day) ? 'custom-holiday': ''}`"
                        @click="select_day = day"
                        >{{ day }}</div>
                </div>
            </div>
        </div>
    </div>

    <div class="flex flex-col items-center">
        <span>Appuntamenti</span>
        <div class="flex flex col items-center">
            <ListItem></ListItem>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            date: this.getCurrentDate(),
            select_day: undefined,            
        }
    },
    methods: {
        getCurrentDate: function () {
            const date = new Date()
            return date
        },
        nextDate: function () {
            this.date = new Date(this.date.getFullYear(), this.date.getMonth() + 1, 1)
            this.select_day = 1
        },
        previousDate: function () {
            this.date = new Date(this.date.getFullYear(), this.date.getMonth() - 1, this.getDayNumberOfMonth())
            this.select_day = this.getDayNumberOfMonth()
        },
        getDayNumberOfMonth: function () {
            return new Date(this.date.getFullYear(), this.date.getMonth(), 0).getDate()
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


    .custom-calendar-container{
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
</style>