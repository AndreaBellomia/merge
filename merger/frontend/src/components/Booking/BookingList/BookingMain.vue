<template>
    <div>
        <BookingModal
        :popUpId="popUpId"
        :popUpState="popUpState"
        :popUp="popUp"
        @close-modal="closePopUpModify()"
        @delete-modal="(value) => (deleteHTTP_booking(value))"
        />
        <div v-for="(item, index) in QueryInstace" :key="index" class="mb-3">
            <SingleBooking
            :instaceBooking="item"
            :dayName="dayName"
            :monthName="monthName"
            @delet-btn="openPopUpModify(item)"
            />
        </div>
        
    </div>
</template>

<style>

</style>


<script>
import axios from "axios";

import BookingModal from './BookingModal.vue'
import SingleBooking from './SingleBooking.vue'


export default {

    components: {
        SingleBooking,
        BookingModal,
    },
    
    data() {
        return {
            QueryInstace: [],
            monthName: [
                "Gennaio",
                "Febbraio",
                "Marzo",
                "Aprile",
                "Maggio",
                "Giuno",
                "Luglio",
                "Agosto",
                "Settembre",
                "Ottobre",
                "Novembre",
                "Dicenbre",
            ],

            dayName: [
                "Lunedì",
                "Martedì",
                "Mercoledì",
                "Giovedì",
                "Venerdì",
                "Sabato",
                "Domenica",
            ],
            popUp: false,
            popUpId: Object,
            popUpState: true

        }
    },
    mounted() {
        this.getHTTP_bookingList();
    },
    methods: {

        openPopUpModify: function(id) {
            this.popUp = true
            this.popUpId = id
        },

        closePopUpModify: function() {
            this.popUp = false
            this.popUpState = true
            window.location.reload()
        },

        deleteHTTP_booking: function (id) {
            axios
                .delete(`/api/booking/${id}`)
                .then((response) => {
                    if (response.status == 204) {
                        this.popUpState = false
                        this.getHTTP_bookingList()
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        getHTTP_bookingList: function () {
            axios
                .get("api/booking/?format=json")
                .then((response) => {
                    this.QueryInstace = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    }
}
</script>