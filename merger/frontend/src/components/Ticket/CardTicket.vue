<template>
    <div class="flex flex-col">
        <div :class="[styles.flexCenter, styles.padding, styles.card, styles.spaceBetweenX]">
            <div class="flex flex-col mb-12">
                <h2 :class="[styles.heading2, 'mb-2']">{{ ticket.title }}</h2>
                <h3 :class="[styles.heading3, 'mb-2']">{{ ticket.description }}</h3>
            </div>
            <div class="flex flex-col">
                <h5 :class="[styles.heading5, 'mb-8']">Id {{ ticket.id }}</h5>
                <span
                    :class="[styles.heading1, ' cursor-pointer text-primary hover:text-secondary active:text-secondaryVariant material-symbols-outlined']">
                    chevron_right</span>
            </div>
        </div>
        <div class="custom-progres-bar-container">
            <div class="custom-progress-bar-background">
                <p>{{ state }}</p>
                <div :class="[styleStatusProgresBar(), 'custom-progress-state']">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { styles } from '@/assets/css';
export default {
    props: {
        ticket: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            styles: styles,
            state: '',
        }
    },
    methods: {
        styleStatusProgresBar: function () {
            if (this.ticket.status == "SEND") {
                this.state = 'Inviato'
                return 'bg-secondary w-1/4'
            } else if (this.ticket.status == "WAIT" || this.ticket.status == "START") {
                this.state = 'In lavorazione'
                return 'bg-orangeCustom w-2/4'
            } else if (this.ticket.status == "BUSY") {
                this.state = 'Documenti Richeisti'
                return 'bg-redCustom w-3/4'
            } else if (this.ticket.status == "COMP") {
                this.state = 'Completato'
                return 'bg-greenCustom w-4/4'
            } 
        },
    }

}
</script>


<style scoped lang="scss">
.custom-progres-bar-container {
    bottom: 1rem;
    position: relative;
    width: 100%;

    .custom-progress-bar-background {
        position: relative;
        width: calc(93% - 0.75rem);
        left: 1.2rem;
        height: 0.4rem;
        background-color: #9c9c9c;
        border-radius: 10rem;

        p {
            position: relative;
            top: -1.2rem;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .custom-progress-state {
            position: relative;
            top: -1.2rem;
            height: 0.4rem;
            border-radius: 10rem;
        }
    }
}
</style>