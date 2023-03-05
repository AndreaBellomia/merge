<template>
    <Transition>
        <div class="custom-popup-background" v-if="show">
            <Transition name="popup">
                <div class="custom-popup-container">
                    <span class="material-symbols-outlined custom-material-symbols-outlined">
                        {{ icon }}
                    </span>
                    <h1>{{ titleCurrent }}</h1>
                    <div class="custom-box-content">
                        <p>{{ contentCurrent }}</p>
                        <slot></slot>
                    </div>
                    <div class="custom-box-bottom flex flex-row justify-center space-x-4">
                        <button v-if="isFirstPopUp" @click="$emit('closeModal')"
                            class="custom-btn-bottom back flex self-center"><span class="material-symbols-outlined">
                                arrow_back
                            </span></button>
                        <button v-if="isFirstPopUp" @click="isFirstPopUp = false"
                            class="custom-btn-bottom flex self-center">{{
                                buttonTextCurrent
                            }}</button>
                        <routerLink :to="routerLink">
                            <button v-if="!isFirstPopUp" @click="$emit('closeModal'), isFirstPopUp = true, $emit('action')"
                                class="custom-btn-bottom flex self-center close">{{
                                    buttonTextCurrent
                                }}</button>
                        </routerLink>
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
        titleFirst: {
            type: String,
            required: true
        },
        titleSecond: {
            type: String,
            required: true
        },
        contentFirst: {
            type: String,
            required: false
        },
        contentSecond: {
            type: String,
            required: true
        },
        buttonTextFirst: {
            type: String,
            required: true
        },
        buttonTextSecond: {
            type: String,
            required: true
        },
        routerLink: {
            type: String,
            default: ''
        }
    },
    data() {
        return {
            titleCurrent: '',
            contentCurrent: '',
            buttonTextCurrent: '',
            isFirstPopUp: true
        }
    },
    updated() {
        this.titleCurrent = this.titleFirst
        this.contentCurrent = this.contentFirst
        this.buttonTextCurrent = this.buttonTextFirst
    },
    watch: {
        isFirstPopUp(newValue) {
            if (newValue) {
                this.titleCurrent = this.titleFirst
                this.contentCurrent = this.contentFirst
                this.buttonTextCurrent = this.buttonTextFirst
            } else {
                this.titleCurrent = this.titleSecond
                this.contentCurrent = this.contentSecond
                this.buttonTextCurrent = this.buttonTextSecond
            }
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
    top: 0;
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

        .custom-material-symbols-outlined {
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
            height: 3rem;
            bottom: 0rem;
            margin-bottom: 0.5rem;

            .custom-btn-bottom {
                font-size: 24px;
                color: #ffffff;
                background-color: #7432E1;
                padding: .25rem 5%;
                border-radius: 8px;

                &:hover {
                    background-color: #5a1eb9;
                }

                &:focus {
                    background-color: #a67ee6;
                }
            }

            .custom-btn-bottom.back {
                color: #8F62DA;
                background-color: #FFFFFF;
                border: 2px solid #8F62DA;
                padding: .5rem 1rem;

                &:hover {
                    color: #5a1eb9;
                    border: 2px solid #5a1eb9;
                }

                &:focus {
                    color: #a67ee6;
                    border: 2px solid #5a1eb9;
                }
            }

            .custom-btn-bottom.close {
                padding-left: 1rem;
                padding-right: 1rem;
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