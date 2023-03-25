<template>
    <router-link :to="destination">
        <div :class="[
            'w-12',
            'h-12',
            'p-2',
            'shadow-md',
            'rounded-full',
            `bg-${bgColor}`,
            bgColor === 'secondary' ? 'hover:bg-secondaryVariant' : '',
            `text-${color}`,
            disabled ? 'cursor-default' : ''
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
            default: '/',
        },
        icon: {
            type: [Object, Function],
            required: true
        },
        bgColor: {
            type: String,
            default: 'secondary',
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