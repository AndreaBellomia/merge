<template>
    <router-link :class="disabled ? 'pointer-events-none' : ''" :to="destination">
        <div :class="[
            'w-12',
            'h-12',
            'p-2',
            'shadow-md',
            'rounded-full',
            `bg-${bgColor}`,
            `hover:bg-${bgColorHover}`,
            `text-${color}`,
            disabled ? 'opacity-50' : ''
        ]">
            <component :is="icon"></component>
        </div>
    </router-link>
</template>

<script>
export default {
    props: {
        destination: {
            type: String,
            default: '',
        },
        icon: {
            type: [Object, Function],
            required: true
        },
        bgColor: {
            type: String,
            default: 'secondary',
        },
        bgColorHover: {
            type: String,
            default: 'secondaryVariant',
        },
        color: {
            type: String,
            default: 'white',
        },
        disabled: {
            type: Boolean,
            default: false,
        }
    }
}
</script>