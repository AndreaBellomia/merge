<template>
    <!-- PopUp -->
    <PopUp :show="showPopUp" :icon="'check_circle'" :title="'Prenotato!'" :buttonText="'Chiudi'"
        :content="`Prenotazione per ${formatData()} avvenuta con successo! Per modificare o eliminare la prenotazione recati nella sezione Prenotazioni`"
        :destination="'/booking'" @close-modal="showPopUp = false">
    </PopUp>
    <!-- Form Header -->
    <FormHeader :booking="appointment" class="mb-8"></FormHeader>
    <!-- Form Add Booking -->
    <div :class="[styles.flexCenter, 'flex-col']">
        <h2 :class="[styles.heading2, 'text-center']">
            Prenotazione
        </h2>
        <form :class="[styles.padding, 'shadow-md rounded-lg w-full']">
            <div class="mb-8">
                <label :class="[styles.heading3]" for="type">* Titolo</label>
                <input v-model="type" class="w-full border-2 p-2 rounded-lg focus:outline-none focus:border-secondary"
                    :class="validOrInvalidTypeClass" type="text" placeholder="Titolo Inserito dal Cliente" id="type" />
            </div>
            <div class="mb-8">
                <label :class="[styles.heading3]" for="description">* Descrizione</label>
                <textarea v-model="description"
                    class="w-full border-2 border-gray-200 p-2 rounded-lg focus:outline-none focus:border-indigo-500"
                    :class="validOrInvalidDescriptionClass" rows="7" type="text"
                    placeholder="Descrizione inserita dal Cliente" id="description"></textarea>
            </div>
            <div :class="[styles.flexCenter, styles.spaceBetweenX]">
                <RouterLink to="/booking/new">
                    <button
                        :class="[styles.heading3, styles.paddingButton, 'border-2 text-secondary border-secondary rounded-lg hover:border-secondaryVariant hover:text-secondaryVariant']">Annulla</button>
                </RouterLink>
                <button :class="[styles.heading3, styles.paddingButton, validOrInvalidTypeClass.length > 0 && validOrInvalidDescriptionClass.length > 0 ? 'bg-secondary border-secondary hover:bg-secondaryVariant hover:border-secondaryVariant' : 'bg-primaryVariant  border-primaryVariant cursor-default opacity-50',
                    'border-2 text-white rounded-lg']" @click="confirm()">Conferma</button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
import FormHeader from '../components/Booking/FormHeader.vue'
import PopUp from '../components/PopUp.vue';
import { styles } from '@/assets/css';
export default {
    components: {
        FormHeader,
        PopUp,
    },
    data() {
        return {
            styles: styles,
            appointment: [],
            type: '',
            description: '',
            validOrInvalidTypeClass: '',
            validOrInvalidDescriptionClass: '',
            showPopUp: false,
        }
    },
    watch: {
        type(newValue) {
            this.validOrInvalidTypeClass = newValue.length > 0 ? 'border-greenCustom' : 'border-redCustom'
        },
        description(newValue) {
            this.validOrInvalidDescriptionClass = newValue.length > 0 ? 'border-greenCustom' : 'border-redCustom'
        }
    },
    mounted() {
        this.getAppointmentById()
    },
    methods: {
        formatData: function () {
            const date = new Date(this.appointment.start_time);
            return `${date.toLocaleString('default', { weekday: 'long' })} ${date.getDate()} ${date.toLocaleString('default', { month: 'long' })}`
        },
        getAppointmentById: function () {
            axios.get(`api/client/appointments/${this.$route.params.id}`)
                .then(response => {
                    this.appointment = response.data
                })
                .catch(error => {
                    console.log(error);
                });
        },
        confirm() {
            if (this.validateForm()) {
                this.postBooking()
                this.showPopUp = true
            }
        },
        validateForm() {
            if (this.type != '' && this.description != '')
                return true
            else
                return false
        },
        postBooking: function () {
            const data = {
                appointments: this.appointment.id,
                type: this.type,
                description: this.description
            };
            axios.post("api/client/booking/", data)
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