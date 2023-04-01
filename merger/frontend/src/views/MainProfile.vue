<template>
    <!-- Header -->
    <div class="flex items-center">
        <h1 :class="[styles.heading1, styles.padding, styles.marginY]">Profilo</h1>
        <span :class="[styles.heading2, getColorByState(state), 'text-black rounded-full px-6 h-fit']">{{
            state
        }}</span>
    </div>

    <!-- Container Card -->
    <div :class="[styles.flexCenter, styles.paddingY, styles.spaceBetweenY, 'flex-col mb-44']">

        <!-- Card Profile -->
        <div :class="[styles.padding, styles.card, styles.spaceBetweenX, 'sm:!space-x-0']">
            <div :class="[styles.flexStart]">
                <div class="flex">
                    <component :class="['sm:w-36 sm:h-36 w-20 h-20']" :is="iconUser">
                    </component>
                </div>
                <div :class="[styles.padding, 'flex flex-col']">
                    <h2 :class="[styles.heading2]">Nome</h2>
                    <h2 :class="[styles.heading2]">Cognome</h2>
                </div>
            </div>
            <div v-if="!cardProfileCollapse" :class="[styles.flexCenter]">
                <form :class="[styles.padding, 'w-full']">
                    <div class="mb-8">
                        <label :class="[styles.heading4]" for="address">Indirizzo di residenza</label>
                        <input v-model="address"
                            class="w-full border-2 p-2 rounded-lg focus:outline-none focus:border-secondary" type="text"
                            id="address" />
                    </div>
                    <h3 :class="[styles.heading3, 'text-center mb-2']">Anagrafica</h3>
                    <div class="mb-4">
                        <label :class="[styles.heading4]" for="birthplace">Luogo di nascita</label>
                        <input v-model="birthplace"
                            class="w-full border-2 p-2 rounded-lg focus:outline-none focus:border-secondary" type="text"
                            id="birthplace" />
                    </div>
                    <div>
                        <label :class="[styles.heading4]" for="birthdate">Data di nascita</label>
                        <input v-model="birthdate"
                            class="w-full border-2 p-2 rounded-lg focus:outline-none focus:border-secondary" type="text"
                            id="birthdate" />
                    </div>
                </form>
            </div>
            <div :class="[styles.flexEnd]">
                <span :class="[styles.arrow]" @click="cardProfileCollapse = !cardProfileCollapse">{{
                    iconCardProfile }}</span>
            </div>
        </div>

        <!-- Card Documentation -->
        <div :class="[styles.card, styles.padding, 'flex flex-col w-full sm:!space-x-0']">
            <h2 :class="[styles.heading2, 'text-center mb-2']">Documenti</h2>
            <div v-if="cardDocumentsCollapse" :class="[styles.flexStart, 'flex-col']">
                <h3 :class="[styles.heading3]">Carta di identità</h3>
                <h3 :class="[styles.heading3]">Codice Fiscale</h3>
            </div>
            <div v-else :class="[styles.flexCenter, 'flex-col']">

                <!-- Card Document -->
                <div
                    :class="[styles.padding, styles.margin, 'flex border-2 border-primary, rounded-3xl sm:space-x-40 space-x-4']">
                    <div :class="[styles.flexStart, 'flex-col']">
                        <h3 :class="[styles.heading3]">Carta di identità</h3>
                        <h4 :class="[styles.heading4]">N.: CA12365</h4>
                        <h5 :class="[styles.heading5, 'mt-4']">Rilascata: 01/01/2020</h5>
                    </div>
                    <div :class="[styles.flexEnd, 'flex-col']">
                        <span :class="[styles.arrow, 'mb-8 sm:mb-4']">edit</span>
                        <h5 :class="[styles.heading5, 'mt-4']">Scadenza: 01/01/2020</h5>
                    </div>
                </div>
                <button :class="[styles.heading3, styles.paddingButton, 'text-primary hover:text-white border-primary hover:bg-primaryVariant hover:border-primaryVariant',
                    'border-2 rounded-lg']">Aggiungi</button>
            </div>
            <div :class="[styles.flexEnd]">
                <span :class="[styles.arrow]" @click="cardDocumentsCollapse = !cardDocumentsCollapse">{{
                    iconCardDocumentation }}</span>
            </div>
        </div>

    </div>
</template>

<script>
import { styles } from '@/assets/css';
import { UserCircleIcon } from '@heroicons/vue/24/solid'

export default {
    data() {
        return {
            styles: styles,
            iconUser: UserCircleIcon,
            state: 'Attivo',
            cardProfileCollapse: true,
            cardDocumentsCollapse: true,
            iconCardProfile: "expand_more",
            iconCardDocumentation: "expand_more"
        }
    },
    watch: {
        cardProfileCollapse(newValue) {
            if (newValue) {
                this.iconCardProfile = "expand_more"
            } else {
                this.iconCardProfile = "expand_less"
            }
        },
        cardDocumentsCollapse(newValue) {
            if (newValue) {
                this.iconCardDocumentation = "expand_more"
            } else {
                this.iconCardDocumentation = "expand_less"
            }
        }
    },
    methods: {
        getColorByState(state) {
            if (state == "Attivo")
                return 'bg-greenCustom'
            else
                return 'bg-redCustom'
        }
    }
}
</script>