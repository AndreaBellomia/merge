<template>
    <!-- Header -->
    <h1 :class="[styles.heading1, styles.padding, styles.marginY]">Prenotazioni</h1>
    <!-- Legend -->
    <div :class="[styles.padding, 'flex']">
        <span v-for="(item, index) in legend" :key="item.id" :class="[index === item.length - 1 ? 'mr-0' : 'mr-4 sm:mr-14',
        styles.flexCenter]">
            <span class="w-3 h-3 rounded-full" :class="item.color"></span>
            <span :class="[styles.heading4, 'ml-1']"> {{ item.label }}</span>
        </span>
    </div>
    <!-- Booking List -->
    <div :class="[styles.flexCenter, styles.paddingY, styles.spaceBetweenY, 'flex-col mb-44']">
        <CardBooking v-for="booking in bookings" :key="booking" :booking="booking"></CardBooking>
    </div>
    <!-- Floating Action Button -->
    <div :class="[styles.flexEnd, styles.margin, styles.floatingActionButtonPositionRight]">
        <FloatingActionButton :destination="'/booking/new'" :icon="iconPlus" />
    </div>
</template>

<script>
import axios from 'axios';
import CardBooking from '../components/Booking/CardBooking.vue'
import FloatingActionButton from '../components/FloatingActionButton.vue'
import { PlusSmallIcon } from '@heroicons/vue/24/solid'
import { styles } from '@/assets/css';

export default {
    components: {
        CardBooking,
        FloatingActionButton
    },
    data() {
        return {
            styles: styles,
            legend: [
                {
                    id: "1",
                    color: "bg-greenCustom",
                    label: "Confermato",
                },
                {
                    id: "2",
                    color: "bg-orangeCustom",
                    label: "In Attesa",
                },
                {
                    id: "3",
                    color: "bg-redCustom",
                    label: "Annullato",
                }
            ],
            iconPlus: PlusSmallIcon,
            bookings: []
        }
    },
    mounted() {
        this.getBooking()
    },
    methods: {
        getBooking() {
            axios
                .get("api/client/booking/")
                .then((response) => {
                    this.bookings = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    }
}
</script>