<template>
    <div>
        <header class="flex">
            <h1>I miei Ticket</h1>
        </header>
        <main>
            <TicketListItem v-for="ticket in tickets" :key="ticket.id" :ticket="ticket" />
        </main>
        <nav class="custom-fb-container">
            <FloatingActionButton :routerLink="'/AddTicketView'" :icon="'add'" />
            <FloatingActionButton :icon="'filter_list'" @btnClick="dropDownMenu = !dropDownMenu"/>
        </nav>
        <DropDownFilter :dropActive="dropDownMenu" @filterClose="dropDownMenu = !dropDownMenu"/>

    </div>
</template>

<script>
import axios from 'axios';
import FloatingActionButton from '../components/FloatingActionButton.vue'
import TicketListItem from '../components/Ticket/TicketListItem.vue'
import DropDownFilter from '../components/Ticket/DropDownFilter.vue'

export default {
    components: {
        FloatingActionButton,
        TicketListItem,
        DropDownFilter
    },
    data() {
        return {
            tickets: Object,
            dropDownMenu: false
        }
    },
    mounted() {
        this.getHTTP_ticketList()
    },
    methods: {
        getHTTP_ticketList() {
            axios
                .get("/api/client/tickets/?format=json")
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

<style scoped lang="scss">
.prova {
    background-color: red;
    height: 10rem;
    width: 10rem;
}

header {
    h1 {
        font-weight: 600;
        font-size: 1.75rem;
        line-height: 29px;
        margin-top: 2rem;
        margin-left: 2rem;
    }
}

main {
    position: absolute;
    top: 8.5rem;
    left: 50%;
    transform: translate(-50%, -0%);
    width: 100%;

}

nav {
    position: absolute;
    bottom: 8rem;
    right: 1.5rem;
    display: flex;
    flex-direction: column;
}
</style>