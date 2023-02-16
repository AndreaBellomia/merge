<template>
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
        <div class="custom-calendar-main flex flex-col">

            <div class="grid-calendar-container">
                <div class="custom-header-col" v-for="day in 7" :key="day">{{ getDayName(day) }}</div>

                <div class="custom-col" v-for="day in getDayNumberOfMonth()" :key="day"
                    :style="`${day == 1 ? 'grid-column-start: ' + getFirstDayOfMonth() : ''}`">{{ day }}</div>
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
            date: this.getCurrentDate()
        }
    },
    methods: {
        getCurrentDate: function () {
            const date = new Date()
            return date
        },
        nextDate: function () {
            this.date = new Date(this.date.getFullYear(), this.date.getMonth() + 1, 1)
        },
        previousDate: function () {
            this.date = new Date(this.date.getFullYear(), this.date.getMonth() - 1, this.getDayNumberOfMonth())
        },
        getDayNumberOfMonth: function () {
            return new Date(this.date.getFullYear(), this.date.getMonth(), 0).getDate()
        },
        getFirstDayOfMonth: function () {
            return new Date(this.date.getFullYear(), this.date.getMonth(), 1).getUTCDay() + 1
        },
        getDayName: function (day) {
            return new Date(2022, 7, day).toLocaleString('default', { weekday: 'short' })
        }
    }
}
</script>

<style scoped lang="scss">
.custom-calendar-container {
    display: flex;
    flex-direction: column;
    background: #1F1F1F;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.4);
    border-radius: 0px 0px 28px 28px;
    padding-bottom: 4rem;
    padding-right: 4rem;
    padding-left: 4rem;

    .custom-header {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-right: 2rem;
        margin-left: 2rem;
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

        .custom-header-col {
            text-align: center;
            font-style: normal;
            font-weight: 300;
            font-size: 1rem;
            line-height: 18px;
            color: #F8FCFF;
            padding: 1rem;
            border-radius: 50%;
        }

        .custom-header-col.holiday {
            color: #CF4E4E;
        }

        .custom-col {
            text-align: center;
            color: #F8FCFF;
            padding: 1rem;
            border-radius: 50%;
            cursor: pointer;
            font-style: normal;
            font-weight: 500;
            font-size: 1rem;
            line-height: 18px;
        }

        .custom-col.holiday {
            color: #CF4E4E;
        }

        .custom-col:hover {
            border-bottom: 1px solid;
            border-radius: 50%;
        }

        .custom-col.active {
            background-color: #8C60D4;
        }
    }

    .grid-calendar-container {
        display: grid;
        grid-template-columns: repeat(7, auto);
    }

}
</style>