<template>

    <div>
        <header>
            <div class="custom-header-backgroud">
                <h1>Crea un Ticket</h1>
            </div>
        </header>
        <main>
            <div class="custom-input-find-container">
                <input type="text" class="custom-input-find" placeholder="Cerca Ticket">
                <span class="material-symbols-outlined" @click="''">
                    search
                </span>
            </div>
            
            <div class="custom-header-text">
                <h2>Tipo di Ticket</h2>
            </div>

            <TicketTypeListItem v-for="type in ticketType" :key="type.id" :title="type.title" :context="type.description"/>
        </main>

        <nav class="custom-fb-container flex flex-col items-start m-1">
            <FloatingActionButton :routerLink="'/MyTicketView'" :icon="'undo'"/>
        </nav>
    </div>
    
</template>


<script>
import axios from 'axios';
import FloatingActionButton from '../components/Ticket/FloatingActionButton.vue'
import TicketTypeListItem from '../components/Ticket/TicketTypeListItem.vue'

export default {
    components: {
        FloatingActionButton,
        TicketTypeListItem
    },
    data () {
        return {
            ticketType: Object
        }
    },
    mounted() {
        this.getHTTP_ticketTypeList()
    },
    methods:{
        getHTTP_ticketTypeList() {
            axios
                .get("api/client/ticket-tipe/")
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
.custom-header-backgroud{
    position: relative;
    display: flex;
    justify-content: center;
    width: 100%;
    background-color: #1F1F1F;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.4);
    border-radius: 0px 0px 28px 28px;

    h1 {
        margin: 1rem 0rem;
        color: white;
        font-size: 2rem;
        font-weight: 600;
    }
}

main {
    position: absolute;
    top: 8.5rem;
    width: 100%;

    .custom-input-find-container{
        position: relative;
        
        .custom-input-find{
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

        .material-symbols-outlined{
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

    .custom-header-text{
        position: relative;
        display: flex;
        justify-content: center;
        left: 50%;
        transform: translate(-50%, -0%);
        
        h2 {
            font-size: 1.5rem;
            font-weight: 600;
        }
    }
}

.custom-fb-container {
  position: absolute;
  bottom: 8rem;
  left: 1.5rem;
  display: flex;
  flex-direction: column;
}

</style>