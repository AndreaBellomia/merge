<template>
    <div>
        <section class="w-full h-full">
            <router-view />
        </section>
        <nav :class="[styles.paddingX, 'w-full fixed bottom-0 left-0 right-0 bg-primary sm:py-8 py-4']">
            <ul class="flex justify-center items-center flex-1 list-none">
                <li v-for="(item, index) in navLinks" :key="item.id"
                    :class="[index === navLinks.length - 1 ? 'mr-0' : 'mr-6 sm:mr-24', 'cursor-pointer']"
                    @click="active = item.id">
                    <router-link :to="item.pattern">
                        <div class="w-12 h-12 sm:w-16 sm:h-16 p-2 sm:hover:text-secondaryVariant sm:hover:border-secondaryVariant"
                            :class="[item.id === active ? 'text-secondary border-secondary border-b-4' : 'text-white border-white']">
                            <component :is="item.logo"></component>
                        </div>
                    </router-link>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
import { BellIcon, ChatBubbleBottomCenterTextIcon, CalendarDaysIcon, TicketIcon, UserIcon } from '@heroicons/vue/24/solid'
import { styles } from './assets/css';
export default {
    data() {
        return {
            styles: styles,
            navLinks: [
                {
                    id: "1",
                    pattern: "/notifications",
                    logo: BellIcon,
                },
                {
                    id: "2",
                    pattern: "/chat",
                    logo: ChatBubbleBottomCenterTextIcon,
                },
                {
                    id: "3",
                    pattern: "/booking",
                    logo: CalendarDaysIcon,
                },
                {
                    id: "4",
                    pattern: "/ticket",
                    logo: TicketIcon,
                },
                {
                    id: "5",
                    pattern: "/profile",
                    logo: UserIcon,
                },
            ],
            active: '3'
        }
    }
}
</script>