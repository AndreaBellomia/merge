<template>
    <section class="flex flex-col">
        <span class="custom-form-title mb-4">
            {{ formTitle }}
        </span>
        <form class="custom-form">
            <div class="flex flex-col px-12 mb-8">
                <label class="custom-label mb-2">Titolo</label>
                <input v-model="type" class="custom-input" type="text" :class="validOrInvalidTypeClass"
                    placeholder="Titolo Inserito dal Cliente" :disabled="!isToSend">
            </div>
            <div class="flex flex-col px-12">
                <label class="custom-label mb-2">Descrizione</label>
                <textarea v-model="description" class="custom-input" :class="validOrInvalidDescriptionClass" rows="7"
                    type="text" placeholder="Descrizione inserita dal Cliente" :disabled="!isToSend"></textarea>
            </div>

            <div v-if="isToSend" class="flex flex-row self-center space-x-4 mt-8 justify-center">
                <RouterLink to="/MyBookingView">
                    <button class="custom-button custom-button-decline">Annulla</button>
                </RouterLink>
                <button class="custom-button custom-button-confirm" @click="confirm()">Conferma</button>
            </div>
        </form>
    </section>
</template>

<script>
import axios from 'axios'
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
                this.updateHTTP_booking()
                this.$emit('openModal');
            }
        },
        validateForm() {
            if (this.type != '' && this.description != '')
                return true
            else
                return false
        },
        updateHTTP_booking: function () {
            const data = {
                appointments: this.booking.id,
                type: this.type,
                description: this.description
            };
            axios.put("/api/client/booking/?format=json", data)
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

<style scoped lang="scss">
.custom-form-title {
    font-style: normal;
    font-weight: 600;
    font-size: 22px;
    line-height: 27px;
    color: #000000;
    text-align: center;
}

.custom-input {
    background: #FFFFFF;
    border: 1px solid #1F1F1F;
    border-radius: 8px;
    padding: 0.4rem;
}

.custom-input.valid {
    border: 2px solid #1ABD00;
}

.custom-input.invalid {
    border: 2px solid #FF1F00;
}

.custom-label {
    font-style: normal;
    font-weight: 500;
    font-size: 22px;
    line-height: 27px;
    color: #000000;
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
}

.custom-button.custom-button-decline {
    border: 2px solid #8F62DA;
    color: #8F62DA;
    background: #F8FCFF;
}

.custom-button.custom-button-confirm {
    color: #F8FCFF;
    background: #8F62DA;
}
</style>