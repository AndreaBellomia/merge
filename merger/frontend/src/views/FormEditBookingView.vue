<template>
    <div>
        <div v-if="this.$route.params.type == 'edit-green'">
            <HeaderForm :booking="booking" :state="'Confermato'" class="mb-8"></HeaderForm>
            <EditBookingContentForm :booking="booking" :formTitle="'Visualizza'">
            </EditBookingContentForm>
            <div class="custom-fb-container left">
                <FloatingActionButton :routerLink="'/MyBookingView'" :icon="'undo'"></FloatingActionButton>
            </div>
            <div class="custom-fb-container right">
                <FloatingActionButton :icon="'delete'" :bgColor="'#808080'" :color="'#B9B9B9'" :disabled="true">
                </FloatingActionButton>
            </div>
        </div>

        <div v-if="this.$route.params.type == 'edit-orange'">
            <PopUp :show="showPopUp" :icon="'edit'" :title="'Modificato!'" :buttonText="'Chiudi'"
                :content="`Modifica per ${this.formatData()} avvenuta con successo! ID: ${this.booking.id}`"
                :routerLink="'/MyBookingView'" @close-modal="showPopUp = false">
            </PopUp>
            <PopUpWithConfirmAction :show="showPopUpDelete" :icon="'delete'" :titleFirst="'Elimina'" :titleSecond="'Eliminato!'"
                :contentFirst="`Vuoi eliminare l'appuntamento per ${this.formatData()}? ID: ${this.booking.id}`"
                :contentSecond="`Appuntamento per ${this.formatData()} eliminato con successo! ID: ${this.booking.id}`"
                :buttonTextFirst="'Conferma'" :buttonTextSecond="'Chiudi'" :routerLink="'/MyBookingView'"
                @close-modal="showPopUpDelete = false" @action="deleteHTTP_bookingById()">
            </PopUpWithConfirmAction>
            <HeaderForm :booking="booking" :state="'In Attesa'" class="mb-8"></HeaderForm>
            <EditBookingContentForm :booking="booking" :formTitle="'Modifica'" :isToSend="true" :formType="'update'"
                @open-modal="showPopUp = true">
            </EditBookingContentForm>
            <div class="custom-fb-container left">
                <FloatingActionButton :routerLink="'/MyBookingView'" :icon="'undo'"></FloatingActionButton>
            </div>
            <div class="custom-fb-container right">
                <FloatingActionButton :icon="'delete'" :bgColor="'#FF1F00'" @click="showPopUpDelete = !showPopUpDelete">
                </FloatingActionButton>
            </div>
        </div>

        <div v-if="this.$route.params.type == 'edit-red'">
            <HeaderForm :booking="booking" :state="'Annullato'" class="mb-8"></HeaderForm>
            <EditBookingContentForm :booking="booking" :formTitle="'Visulizza'">
            </EditBookingContentForm>
            <div class="custom-fb-container left">
                <FloatingActionButton :routerLink="'/MyBookingView'" :icon="'undo'"></FloatingActionButton>
            </div>
            <div class="custom-fb-container right">
                <FloatingActionButton :icon="'delete'" :bgColor="'#808080'" :color="'#B9B9B9'" :disabled="true">
                </FloatingActionButton>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import HeaderForm from '../components/Booking/HeaderForm.vue'
import EditBookingContentForm from '../components/Booking/EditBookingContentForm.vue'
import PopUp from '../components/Booking/PopUp.vue';
import PopUpWithConfirmAction from '@/components/Booking/PopUpWithConfirmAction.vue';
import FloatingActionButton from '../components/FloatingActionButton.vue';
export default {
    components: {
        HeaderForm,
        EditBookingContentForm,
        PopUp,
        PopUpWithConfirmAction,
        FloatingActionButton,
    },
    data() {
        return {
            booking: [],
            showPopUp: false,
            showPopUpDelete: false,
        }
    },
    mounted() {
        this.getHTTP_bookingById()
    },
    methods: {
        formatData: function () {
            const date = new Date(this.booking.start_time);
            return `${date.toLocaleString('default', { weekday: 'long' })} ${date.getDate()} ${date.toLocaleString('default', { month: 'long' })}`
        },
        getHTTP_bookingById: function () {
            axios.get(`/api/client/booking/${this.$route.params.id}`)
                .then(response => {
                    this.booking = response.data
                })
                .catch(error => {
                    console.log(error);
                });
        },
        deleteHTTP_bookingById: function () {
            axios.delete(`/api/client/booking/${this.$route.params.id}`)
                .then(response => {
                    this.booking = response.data
                })
                .catch(error => {
                    console.log(error);
                });
        },
    }

}
</script>

<style scoped lang="scss">
.custom-fb-container {
    position: absolute;
    bottom: 8rem;
    display: flex;
    flex-direction: column;
}

.custom-fb-container.left {
    left: 1.5rem;

}

.custom-fb-container.right {
    right: 1.5rem;
    padding: .5rem .5rem;
}
</style>