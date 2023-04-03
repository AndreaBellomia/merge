<template>
    <div :class="[styles.flexCenter, 'flex-col']">
        <h2 :class="[styles.heading2, 'text-center']">
            {{ formTitle }}
        </h2>
        <form :class="[styles.padding, 'rounded-lg w-full']">
            <div class="mb-8">
                <label :class="[styles.heading3]" for="type">* Titolo</label>
                <input v-model="type" class="w-full border-2 p-2 rounded-lg focus:outline-none focus:border-secondary"
                    :class="validOrInvalidTypeClass" type="text" placeholder="Titolo Inserito dal Cliente" id="type"
                    :disabled="!isToSend" />
            </div>
            <div class="mb-8">
                <label :class="[styles.heading3]" for="description">* Descrizione</label>
                <textarea v-model="description"
                    class="w-full border-2 border-gray-200 p-2 rounded-lg focus:outline-none focus:border-indigo-500"
                    :class="validOrInvalidDescriptionClass" rows="7" type="text"
                    placeholder="Descrizione inserita dal Cliente" id="description" :disabled="!isToSend"></textarea>
            </div>
            <div v-if="isToSend" :class="[styles.flexCenter, styles.spaceBetweenX]">
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
import { styles } from '@/assets/css';
export default {
    props: {
        booking: {
            type: Object,
            required: true
        },
        formTitle: {
            type: String,
            required: true
        },
        isToSend: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            styles: styles,
            type: '',
            description: '',
            validOrInvalidTypeClass: '',
            validOrInvalidDescriptionClass: ''
        }
    },
    watch: {
        booking(newValue) {
            this.type = newValue.type
            this.description = newValue.description
        },
        type(newValue) {
            this.validOrInvalidTypeClass = newValue.length > 0 ? 'valid' : 'invalid'
        },
        description(newValue) {
            this.validOrInvalidDescriptionClass = newValue.length > 0 ? 'valid' : 'invalid'
        }
    },
    methods: {
        confirm() {
            if (this.validateForm()) {
                this.updateBooking()
                this.$emit('openModal');
            }
        },
        validateForm() {
            if (this.type != '' && this.description != '')
                return true
            else
                return false
        },
        updateBooking: function () {
            const data = {
                type: this.type,
                description: this.description
            };
            console.log(data)
            axios.patch(`api/client/booking/${this.booking.id}`, data)
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.log(error);
                });
        },
    }
}
</script>