<template>
    <div>
        <!-- PopUp With Confirm Action -->
        <PopUpWithConfirmAction :show="showPopUpConfirm" :icon="'confirmation_number'" :titleFirst="'Crea Ticket'"
            :titleSecond="'Inviato!'" :contentFirst="`Vuoi Richieder un ticket per: ${this.ticketType}?`"
            :contentSecond="`Ticket ${this.ticketType} è stato richeisto correttamente`" :buttonTextFirst="'Conferma'"
            :buttonTextSecond="'Chiudi'" :destination="`/ticket`" @close-modal="showPopUpConfirm = false"
            @action="postBooking()">
        </PopUpWithConfirmAction>
        <!-- Header -->
        <div :class="[styles.flexCenter, styles.header, 'bg-primary mb-12']">
            <h1 :class="[styles.heading1, styles.paddingX, 'text-white py-6']">Crea un Ticket</h1>
        </div>
        <!-- Form -->
        <form :class="[styles.padding, 'shadow-md rounded-lg w-90', 'overflow-y-auto mb-20']">
            <div class="mb-8">
                <label :class="[styles.heading3]" for="title">* Titolo</label>
                <input v-model="formTitle" class="w-full border-2 p-2 rounded-lg focus:outline-none focus:border-secondary"
                    :class="validOrInvalidTitleClass" type="text" placeholder="Inserisci titolo del ticket..." id="title" />
            </div>
            <div class="mb-8">
                <label :class="[styles.heading3]" for="description">* Descrizione</label>
                <input v-model="formDescription"
                    class="w-full border-2 p-2 rounded-lg focus:outline-none focus:border-secondary"
                    :class="validOrInvalidDescriptionClass" type="text" placeholder="Inserisci descrizione del ticket..."
                    id="description" />
            </div>
            <!-- Fields Container -->
            <FieldsContainer v-for="item in listFields" :key="item" :content="item" @input-change="setValueOfFields" />
            <div :class="[styles.flexCenter, styles.spaceBetweenX]">
                <RouterLink to="/ticket/new">
                    <button
                        :class="[styles.heading3, styles.paddingButton, 'border-2 text-secondary border-secondary rounded-lg hover:border-secondaryVariant hover:text-secondaryVariant']">Annulla</button>
                </RouterLink>
                <button :class="[styles.heading3, styles.paddingButton, validOrInvalidTitleClass.length > 0 && validOrInvalidDescriptionClass.length > 0 ? 'bg-secondary border-secondary hover:bg-secondaryVariant hover:border-secondaryVariant' : 'bg-primaryVariant  border-primaryVariant cursor-default opacity-50 pointer-events-none',
                    'border-2 text-white rounded-lg']" @click="showPopUpConfirm = !showPopUpConfirm">Conferma</button>
            </div>
        </form>
    </div>
</template>


<script>
import axios from 'axios';
import FieldsContainer from '../components/Ticket/FieldsContainer.vue'
import PopUpWithConfirmAction from '../components/PopUpWithConfirmAction.vue'
import { styles } from '@/assets/css';

export default {
    components: {
        FieldsContainer,
        PopUpWithConfirmAction
    },
    data() {
        return {
            styles: styles,
            ticketType: '',
            listFields: [],
            responseField: [],
            booking: [],
            showPopUp: false,
            showPopUpConfirm: false,
            formTitle: '',
            formDescription: '',
            validOrInvalidTitleClass: '',
            validOrInvalidDescriptionClass: '',
        }
    },
    watch: {
        formTitle(newValue) {
            this.validOrInvalidTitleClass = newValue.length > 0 ? 'border-greenCustom' : 'border-redCustom'
        },
        formDescription(newValue) {
            this.validOrInvalidDescriptionClass = newValue.length > 0 ? 'border-greenCustom' : 'border-redCustom'
        }
    },
    mounted() {
        this.getTicketTypeRelated()

    },
    methods: {
        getTicketTypeRelated() {
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
                            id: element.id,
                            primary_key: element.primary_key,
                            type_field: element.type_field,
                            value: ''
                        })
                        pk++
                    })

                }
            }

            // Sort in order of index a filde object
            fields.sort(function (a, b) {
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
        postBooking: function () {
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
