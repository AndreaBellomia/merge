<template>
    <div>
        <header>
            <div class="custom-header-backgroud">
                <h1>Crea un Ticket</h1>
                <div class="custom-line"/>
                <h1>{{ ticketType }}</h1>
            </div>
        </header>
        <main>
            <div v-for="item in listFields" :key="item">
                <FieldsContainer :content="item" @input-change="setValueOfFields"/>
            </div>
            <div class="flex flex-row self-center space-x-4 mt-8 justify-center">
                <RouterLink to="/AddTicketView">
                    <button class="custom-button custom-button-decline">Annulla</button>
                </RouterLink>
                <button class="custom-button custom-button-confirm" @click="'confirm()'">Conferma</button>
            </div>
        </main>
        

        <button @click="prova">prova</button>
    </div>
</template>


<script>
import axios from 'axios';
import FieldsContainer from '../components/Ticket//FieldsContainer.vue'


export default {
    components: {
        FieldsContainer
    },
    data() {
        return {
            ticketType: '',
            listFields: [],
            responseField: []
        }
    },
    mounted() {
        this.getHTTP_ticketTypeRelatedList()
        
    },
    methods: {
        getHTTP_ticketTypeRelatedList() {
            axios
                .get(`api/client/ticket-type/${this.$route.params.id}`)
                .then((response) => {
                    this.unpackTicketType(response.data)
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        unpackTicketType: function (object) {

            // List of fields to exclude
            const excludedFields = ['title', 'description', 'id'];
            const fields = [];
            let pk = 0

            this.ticketType = object.title

            // Extract fields from http resposne
            for (const [key, value] of Object.entries(object)) {
                if (!excludedFields.includes(key)) {
                    value.forEach((element) => {
                        element.primary_key = pk
                        fields.push(element)
                        this.responseField.push({
                            id : element.id,
                            primary_key : element.primary_key,
                            type_field : element.type_field,
                            value : ''
                        })
                        pk++
                    })
                    
                }
            }

            // Sort in order of index a filde object
            fields.sort(function(a, b){
                if (a.index < b.index) {
                    return -1
                }
                if (a.index > b.index) {
                    return 1
                }
                return 0
                })
            
            // Sett globaly a sorted list of filds
            this.listFields = fields
        },
        setValueOfFields: function (object) {
            // Find in responseField fields 
            this.responseField.forEach(element => {
                if (object.primary_key == element.primary_key) {
                    element.value = object.value
                }
            })

            console.log(object)
        },
        prova: function () {
            console.log(this.responseField)
        }
    }
}
</script>


<style scoped lang="scss">
.custom-header-backgroud{
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
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

    .custom-line {
        border: 1px solid white;
        width: 95%;
    }
}

.custom-button {
    border-radius: 8px;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    padding-left: 1.4rem;
    padding-right: 1.4rem;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;

    &.custom-button-decline {
        border: 2px solid #8F62DA;
        color: #8F62DA;
        background: #F8FCFF;
    }

    &.custom-button-confirm {
        color: #F8FCFF;
        background: #8F62DA;
    }

}
</style>