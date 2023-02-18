<template>
    <header class="custom-header flex flex-col p-8 items-center">
        <span class="custom-date">Venedri 12 Febbraio</span>
        <span class="custom-time"><span class="custom-time hours">14</span>:00 - <span
                class="custom-time hours">14</span>:00</span>
        <span class="custom-divider mb-2">_</span>
        <span class="custom-author">Nome Cognome Amm</span>
        <span v-if="stateVisibility" class="custom-state-indication mt-8 px-10 py-2">{{ state }}</span>
    </header>
</template>

<script>
export default {
    props: {
        state: {
            type: String,
            required: true
        },
        stateVisibility: {
            type: Boolean,
            required: true
        }
    }
}
</script>

<style scoped lang="scss">
.custom-header {
    background: #1F1F1F;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 0px 0px 28px 28px;

    .custom-date {
        color: #F8FCFF;
        font-style: normal;
        font-weight: 400;
        font-size: 1.6rem;
        line-height: 32px;
    }

    .custom-time {
        color: #F8FCFF;
        font-style: normal;
        font-weight: 500;
        font-size: 2.5rem;
        line-height: 48px;
    }

    .custom-time .hours {
        color: #A771FF;
    }

    .custom-divider {
        border-bottom: 1px solid #F8FCFF;
        width: 10rem;
    }

    .custom-author {
        font-style: normal;
        font-weight: 300;
        font-size: 1.6rem;
        line-height: 29px;
        color: #F8FCFF;
    }

    .custom-state-indication {
        background: #FFB800;
        color: #000000;
        font-style: normal;
        font-weight: 600;
        font-size: 1.2rem;
        line-height: 16px;
        border-radius: 100px;
    }
}
</style>