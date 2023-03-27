<template>
    <!-- Header -->
    <div :class="[styles.flexCenter, 'bg-primary shadow-md rounded-b-lg mb-12']">
        <h1 :class="[styles.heading1, styles.paddingX, 'text-white py-6']">Crea un Ticket</h1>
    </div>
    <!-- Search Bar -->
    <div :class="[styles.marginX, 'custom-input-find-container']">
        <input type="text" class="custom-input-find" placeholder="Cerca Ticket">
        <span class="material-symbols-outlined" @click="''">
            search
        </span>
    </div>
    <!-- Ticket List -->
    <h2 :class="[styles.heading2, styles.paddingX, 'text-center']">Tipo di Ticket</h2>
    <div :class="[styles.flexCenter, styles.paddingY, 'flex-col mb-44']">
        <CardTicketType v-for="ticketTypeItem in ticketType" :key="ticketTypeItem.id" :title="ticketTypeItem.title"
            :context="ticketTypeItem.description" :formId="ticketTypeItem.id" />
    </div>
    <!-- Floating Action Button -->
    <div :class="[styles.flexEnd, styles.margin, styles.floatingActionButtonPositionRight]">
        <FloatingActionButton :destination="'/ticket'" :icon="iconBack" />
    </div>
</template>


<script>
import axios from 'axios';
import FloatingActionButton from '../components/FloatingActionButton.vue'
import CardTicketType from '../components/Ticket/CardTicketType.vue'
import { ArrowUturnLeftIcon } from '@heroicons/vue/24/solid'
import { styles } from '@/assets/css';

export default {
    components: {
        FloatingActionButton,
        CardTicketType
    },
    data() {
        return {
            styles: styles,
            iconBack: ArrowUturnLeftIcon,
            ticketType: []
        }
    },
    mounted() {
        this.getTicketType()
    },
    methods: {
        getTicketType() {
            axios
                .get("api/client/ticket-type/")
                .then((response) => {
                    this.ticketType = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    }

}
</script>

<style scoped lang="scss">
.custom-input-find-container {
    position: relative;
    top: -3rem;

    .custom-input-find {
        position: relative;
        left: 50%;
        transform: translate(-50%, -0%);
        height: 2.5rem;
        width: 90%;
        background-color: white;
        padding: 0rem 1rem;
        border-radius: 8px;
        border: 1px solid #313131;
        margin: 2rem 0rem;
    }

    .material-symbols-outlined {
        position: absolute;
        bottom: 2.45rem;
        right: 6%;
        cursor: pointer;

        &:hover {
            font-weight: 600;
        }

        &:focus {
            font-weight: 600;
        }
    }
}
</style>