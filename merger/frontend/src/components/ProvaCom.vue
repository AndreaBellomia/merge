<template>
    <div>
        <div ref="ciao"></div>
        {{ info }}
    </div>
</template>

<script setup>

import { getAPI } from '../axios';

import { ref, onMounted } from "vue";
console.log()
const info = ref(null)
onMounted(async () => {
    await getAPI
        .get('appointments/?format=json')
        .then(response => {
            info.value = response.data
    
    })

    console.log(info.value)

})









</script>