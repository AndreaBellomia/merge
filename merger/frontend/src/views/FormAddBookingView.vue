<template>
    <PopUp :show="showPopUp" :icon="'check_circle'" :title="'Prenotato!'" :buttonText="'Chiudi'"
        :content="`Prenotazione per ${formatData()} avvenuta con successo! Per modificare o eliminare la prenotazione recati nella sezione Prenotazioni`"
        :routerLink="'/MyBookingView'" @close-modal="showPopUp = false">
    </PopUp>
    <HeaderForm :booking="appointment" class="mb-8"></HeaderForm>
    <AddAppointmentContentForm :booking="appointment" :formTitle="'Prenotazione'" :isToSend="true"
        @open-modal="showPopUp = true">
    </AddAppointmentContentForm>
</template>

<script>
import axios from 'axios'
import HeaderForm from '../components/Booking/HeaderForm.vue'
import AddAppointmentContentForm from '../components/Booking/AddAppointmentContentForm.vue'
import PopUp from '../components/Booking/PopUp.vue';
export default {
    components: {
        HeaderForm,
        AddAppointmentContentForm,
        PopUp,
    },
    data() {
        return {
            appointment: Object,
            showPopUp: false,
            showPopUpDelete: false,
        }
    },
    mounted() {
        this.getHTTP_appointmentById()
    },
    methods: {
        formatData: function () {
            const date = new Date(this.appointment.start_time);
            return `${date.toLocaleString('default', { weekday: 'long' })} ${date.getDate()} ${date.toLocaleString('default', { month: 'long' })}`
        },
        getHTTP_appointmentById: function () {
            axios.get(`/api/client/appointments/${this.$route.params.id}`)
                .then(response => {
                    this.appointment = response.data
                })
                .catch(error => {
                    console.log(error);
                });
        },
    }
}
</script>