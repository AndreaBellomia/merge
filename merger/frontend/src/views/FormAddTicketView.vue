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
            <div class="custom-model-header">
                
                <div class="custom-model-container">
                    <label for="titolo">Titolo</label>
                    <input type="text" class="input-text" name="titolo" placeholder="Inserisci titolo del ticket..." v-model="formTitle">
                </div>

                <div class="custom-model-container">
                    <label for="description">Descrizione</label>
                    <input type="text" class="input-text" name="description" placeholder="Inserisci description del ticket..." v-model="formDescription">
                </div>
            </div>

            
            <div v-for="item in listFields" :key="item">
                <FieldsContainer :content="item" @input-change="setValueOfFields"/>
            </div>
            <div class="flex flex-row self-center space-x-4 mt-8 justify-center">
                <RouterLink to="/AddTicketView">
                    <button class="custom-button custom-button-decline">Annulla</button>
                </RouterLink>
                <button class="custom-button custom-button-confirm" @click="showPopUpConfirm = !showPopUpConfirm">Conferma</button>
            </div>
            <div class="my-10 py-10">
            
            </div>
        </main>

        <PopUpWithConfirmAction :show="showPopUpConfirm" :icon="'confirmation_number'" :titleFirst="'Crea Ticket'" :titleSecond="'Inviato!'"
            :contentFirst="`Vuoi Richieder un ticket per: ${this.ticketType}?`"
            :contentSecond="`Ticket ${this.ticketType} è stato richeisto correttamente`"
            :buttonTextFirst="'Conferma'" :buttonTextSecond="'Chiudi'" :routerLink="'/MyTicketView'"
            @close-modal="showPopUpConfirm = false" @action="postHTTP_booking()">
        </PopUpWithConfirmAction>

    </div>
</template>


<script>
import axios from 'axios';
import FieldsContainer from '../components/Ticket/FieldsContainer.vue'
import PopUpWithConfirmAction from '../components/Ticket/PopUpWithConfirmAction.vue'


export default {
    components: {
        FieldsContainer,
        PopUpWithConfirmAction
    },
    data() {
        return {
            ticketType: '',
            listFields: [],
            responseField: [],
            booking: [],
            showPopUp: false,
            showPopUpConfirm: false,
            formTitle: '',
            formDescription: '',
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
        },
        postHTTP_booking: function () {
            const data = {
                title: this.formTitle,
                description: this.formDescription,
                json_fields: this.responseField,
                type_document: 1
            }

            axios.post("/api/client/tickets/?format=json", data)

                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.log(error);
                });
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

main{
    margin: 0rem .5rem;
}

.custom-model-header {

    background-color: #313131;
    padding-bottom: .5rem;
    margin-top: 2rem;
    border-radius: 14px;

    .custom-model-container {
        position: relative;
        display: flex;
        flex-direction: column;
        margin: 0.5rem;

        label {
            margin: 1rem 0 0.5rem 0;
            font-weight: 600;
            font-size: 1.2rem;
            color: white;
        }

        input.input-text {
            padding: .5rem .5rem;
            border-radius: 8px;
            border: 1px solid #313131;
        }
    }
}


</style>