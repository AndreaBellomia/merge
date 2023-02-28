
<!-- <NameComponent :routerLink="'/navigate-to'" :icon="'example'"/> -->

<template>
    <div>
        <router-link :to="routerLink" v-if="routerLink != ''">
            <div class="custom-fb-container">
                <span class="material-symbols-outlined">
                    {{ icon }}
                </span>
            </div>
        </router-link>
        <main v-else>
            <div class="custom-fb-container" @click="$emit('btnClick')">
                <span class="material-symbols-outlined">
                    {{ icon }}
                </span>
            </div>
        </main>
    </div>
</template>

<script>
export default {
    props: {
        routerLink: {
            type: String,
            default: ''
        },
        icon: {
            type: String,
            required: true
        },
    }
}
</script>

<style scoped lang="scss">
.custom-fb-container{
    display: flex;
    justify-content: center;
    align-items: center;

    border-radius: 50%;
    margin-top: 1rem;
    background: #8F62DA;
    box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.5); 
    
    .material-symbols-outlined {
        font-size: 2rem;
        color: #F8FCFF;
        padding: 0.5rem;
         
        -webkit-user-select: none;
        cursor: pointer;
    }
}
</style>