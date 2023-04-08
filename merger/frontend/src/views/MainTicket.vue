<template>
    <div>
        <h1 :class="[styles.heading1, styles.padding, styles.marginY]">I miei Ticket</h1>
        <!-- Ticket List -->
        <div :class="[styles.flexCenter, styles.paddingY, styles.spaceBetweenY, 'flex-col mb-44']">
            <CardTicket v-for="ticket in tickets" :key="ticket.id" :ticket="ticket" />
        </div>
        <!-- Floating Action Button -->
        <div
            :class="[styles.flexEnd, styles.margin, styles.floatingActionButtonPositionRight, styles.spaceBetweenY, 'flex-col']">
            <FloatingActionButton :destination="'/ticket/new'" :icon="iconPlus" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import FloatingActionButton from '../components/FloatingActionButton.vue'
import CardTicket from '../components/Ticket/CardTicket.vue'
import { PlusSmallIcon, FunnelIcon } from '@heroicons/vue/24/solid'
import { styles } from '@/assets/css';

export default {
    components: {
        FloatingActionButton,
        CardTicket
    },
    data() {
        return {
            styles: styles,
            iconPlus: PlusSmallIcon,
            iconFilter: FunnelIcon,
            tickets: [],
        }
    },
    mounted() {
        this.getTicket()
    },
    methods: {
        getTicket() {
            axios
                .get("api/client/tickets/")
                .then((response) => {
                    this.tickets = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    }
}
</script>