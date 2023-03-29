<template>
    <div>
        <!-- GREEN -->
        <div v-if="this.$route.params.type == 'edit-green'">
            <!-- Form Header -->
            <FormHeader :booking="booking" :state="'Confermato'" class="mb-8"></FormHeader>
            <!-- Form Details -->
            <FormDetails :booking="booking" :formTitle="'Visualizza'">
            </FormDetails>
            <!-- Floating Action Button -->
            <div :class="[styles.flexStart, styles.margin, styles.floatingActionButtonPositionLeft]">
                <FloatingActionButton :icon="iconBack" :destination="'/booking'" />
            </div>
            <div :class="[styles.flexStart, styles.margin, styles.floatingActionButtonPositionRight]">
                <FloatingActionButton :icon="iconDelete" :bgColor="'primaryVariant'" :bgColorHover="'primaryVariant'"
                    :disabled="true" />
            </div>
        </div>

        <!-- ORANGE -->
        <div v-if="this.$route.params.type == 'edit-orange'">
            <!-- PopUp -->
            <PopUp :show="showPopUp" :icon="'edit'" :title="'Modificato!'" :buttonText="'Chiudi'"
                :content="`Modifica per ${this.formatData()} avvenuta con successo! ID: ${this.booking.id}`"
                :destination="'/booking'" @close-modal="showPopUp = false">
            </PopUp>
            <!-- PopUp With Confirm Action -->
            <PopUpWithConfirmAction :show="showPopUpDelete" :icon="'delete'" :titleFirst="'Elimina'"
                :titleSecond="'Eliminato!'"
                :contentFirst="`Vuoi eliminare l'appuntamento per ${this.formatData()}? ID: ${this.booking.id}`"
                :contentSecond="`Appuntamento per ${this.formatData()} eliminato con successo! ID: ${this.booking.id}`"
                :buttonTextFirst="'Conferma'" :buttonTextSecond="'Chiudi'" :destination="'/booking'"
                @close-modal="showPopUpDelete = false" @action="deleteBookingById()">
            </PopUpWithConfirmAction>
            <!-- Form Header -->
            <FormHeader :booking="booking" :state="'In Attesa'" class="mb-8"></FormHeader>
            <!-- Form Deatils -->
            <FormDetails :booking="booking" :formTitle="'Modifica'" :isToSend="true" :formType="'update'"
                @open-modal="showPopUp = true">
            </FormDetails>
            <!-- Floating Action Button -->
            <div :class="[styles.flexStart, styles.margin, styles.floatingActionButtonPositionLeft]">
                <FloatingActionButton :icon="iconBack" :destination="'/booking'" />
            </div>
            <div :class="[styles.flexStart, styles.margin, styles.floatingActionButtonPositionRight]">
                <FloatingActionButton :icon="iconDelete" :bgColor="'redCustom'" :bgColorHover="'redCustomVariant'"
                    @click="showPopUpDelete = !showPopUpDelete" />
            </div>
        </div>

        <!-- RED -->
        <div v-if="this.$route.params.type == 'edit-red'">
            <!-- Form Header -->
            <FormHeader :booking="booking" :state="'Annullato'" class="mb-8"></FormHeader>
            <!-- Form Deatils -->
            <FormDetails :booking="booking" :formTitle="'Visualizza'">
            </FormDetails>
            <!-- Floating Action Button -->
            <div :class="[styles.flexStart, styles.margin, styles.floatingActionButtonPositionLeft]">
                <FloatingActionButton :icon="iconBack" :destination="'/booking'" />
            </div>
            <div :class="[styles.flexStart, styles.margin, styles.floatingActionButtonPositionRight]">
                <FloatingActionButton :icon="iconDelete" :bgColor="'primaryVariant'" :bgColorHover="'primaryVariant'"
                    :disabled="true" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import FormHeader from '../components/Booking/FormHeader.vue'
import FormDetails from '../components/Booking/FormDetails.vue'
import PopUp from '../components/PopUp.vue';
import PopUpWithConfirmAction from '@/components/PopUpWithConfirmAction.vue';
import FloatingActionButton from '../components/FloatingActionButton.vue';
import { TrashIcon, ArrowUturnLeftIcon } from '@heroicons/vue/24/solid'
import { styles } from '@/assets/css';
export default {
    components: {
        FormHeader,
        FormDetails,
        PopUp,
        PopUpWithConfirmAction,
        FloatingActionButton,
    },
    data() {
        return {
            styles: styles,
            iconDelete: TrashIcon,
            iconBack: ArrowUturnLeftIcon,
            booking: [],
            showPopUp: false,
            showPopUpDelete: false,
        }
    },
    mounted() {
        this.getBookingById()
    },
    methods: {
        formatData: function () {
            const date = new Date(this.booking.start_time);
            return `${date.toLocaleString('default', { weekday: 'long' })} ${date.getDate()} ${date.toLocaleString('default', { month: 'long' })}`
        },
        getBookingById: function () {
            axios.get(`api/client/booking/${this.$route.params.id}`)
                .then(response => {
                    this.booking = response.data
                })
                .catch(error => {
                    console.log(error);
                });
        },
        deleteBookingById: function () {
            axios.delete(`api/client/booking/${this.$route.params.id}`)
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