<template>
    <router-link :to="routerLink">
        <div class="custom-fb-container" :style="{ background: bgColor }">
            <span class="material-symbols-outlined" :style="{ color: color, cursor: `${getCursorByDisabled(disabled)}` }">
                {{ icon }}
            </span>
        </div>
    </router-link>
</template>

<script>
export default {
    props: {
        routerLink: {
            type: String,
            default: '',
        },
        icon: {
            type: String,
            required: true
        },
        bgColor: {
            type: String,
            default: '#8F62DA',
        },
        color: {
            type: String,
            default: '#F8FCFF',
        },
        disabled: {
            type: Boolean,
            default: false,
        }
    },
    methods: {
        getCursorByDisabled(disabled) {
            if (!disabled) {
                return 'pointer'
            } else {
                return 'default'
            }
        }
    }
}
</script>

<style scoped lang="scss">
.custom-fb-container {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    margin-top: 1rem;
    box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.5);

    .material-symbols-outlined {
        font-size: 2rem;
        padding: 0.5rem;
        -webkit-user-select: none;
    }
}
</style>