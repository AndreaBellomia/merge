<!-- <TicketTypeListItem :title="'730'" :context="'ciao franconi'" /> -->

<template>
    <div :class="[styles.flexCenter, styles.padding, styles.card]">
        <div class="custom-card-img">
            <h3 :class="styles.heading3">{{ title }}</h3>
        </div>
        <div>
            <h2 :class="styles.heading2">{{ title }}</h2>
            <h5 :class="styles.heading5">{{ context }}</h5>
            <RouterLink :to="{ name: 'FormAddTicket', params: { id: formId } }">
                <p :class="['text-secondary hover:text-secondaryVariant']">
                    Richiedi
                </p>
            </RouterLink>
        </div>
    </div>
</template>

<script>
import { styles } from '@/assets/css';
export default {
    props: {
        title: {
            type: String,
            required: true
        },
        context: {
            type: String,
            required: true
        },
        img: {
            type: String,
            required: false
        },
        formId: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            styles: styles
        }
    },
}
</script>

<style scoped lang="scss">
.custom-card-img {
    width: 50%;
    max-width: 6rem;
    aspect-ratio: 1 / 1;
    display: flex;
    justify-content: center;
    align-items: center;

    background: linear-gradient(17deg, rgba(69, 2, 149, 1) 0%, rgba(199, 0, 255, 1) 100%);
    overflow: hidden;
    border-right: 2px solid gray;

    h3 {
        color: white;
        font-size: 4rem;
        font-weight: 600;
        transform: rotate(-30deg);
    }
}
</style>