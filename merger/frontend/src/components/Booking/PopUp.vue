<!-- 
<Popup :show="prova" :icon="'check_circle'" :title="'Prova!'" :buttonText="'Chiudi'" @close-modal="prova = false">Slor content</Popup> 
    -->
<template>
    <Transition>
        <div class="custom-popup-background" v-if="show">
            <Transition name="popup">
                <div class="custom-popup-container">
                    <span class="material-symbols-outlined">
                        {{ icon }}
                    </span>
                    <h1>{{ title }}</h1>
                    <div class="custom-box-content">
                        <p>{{ content }}</p>
                        <slot></slot>
                    </div>
                    <div class="custom-box-bottom">
                        <button @click="$emit('closeModal')" class="custom-btn-bottom">{{ buttonText }}</button>
                    </div>
                </div>
            </Transition>
        </div>
    </Transition>
</template>

<script>
export default {
    props: {
        show: {
            type: Boolean,
            required: true
        },
        icon: {
            type: String,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        content: {
            type: String,
            required: false
        },
        buttonText: {
            type: String,
            required: true
        }
    }
};
</script>

<style lang="scss" scoped>
.v-enter-active,
.v-leave-active {
    transition: opacity 0.2s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}

.custom-popup-background {
    position: absolute;
    height: 100%;
    width: 100%;
    background-color: #0000008a;

    .v-enter-active,
    .v-leave-active {
        transition: opacity 0.5s ease;
    }

    .v-enter-from,
    .v-leave-to {
        opacity: 0;
    }


    .custom-popup-container {
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);

        height: auto;
        width: 50%;
        max-width: 40rem;

        background-color: #F8FCFF;
        border-radius: 14px;
        overflow: hidden;

        transition: width 0.3s;

        h1 {
            padding-top: 1.5rem;
            font-size: 2rem;
            font-weight: 500;
            text-align: center;
        }

        .material-symbols-outlined {
            position: relative;
            top: 1.5rem;
            left: 50%;
            transform: translate(-50%, 0%);

            font-size: 71px;
            color: #7432E1;
            background-color: #a770ff42;
            border-radius: 50%;
            padding: 0.3rem;
        }

        .custom-box-content {
            position: relative;
            height: 60%;
            padding: 0.75rem 10%;
            margin-bottom: 5rem;
            text-align: center;
        }

        .custom-box-bottom {
            position: absolute;
            width: 100%;
            height: 4rem;

            bottom: 0rem;

            background-color: #ffffff;

            .custom-btn-bottom {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);

                font-size: 24px;
                color: #ffffff;
                background-color: #7432E1;
                padding: 0.25rem 5%;
                border-radius: 8px;

                &:hover {
                    background-color: #5a1eb9;
                }

                &:focus {
                    background-color: #a67ee6;
                }
            }
        }

        @media screen and (max-width: 768px) {
            width: 80%;
        }

        @media screen and (max-width: 576px) {
            width: 100%;
        }
    }
}
</style>