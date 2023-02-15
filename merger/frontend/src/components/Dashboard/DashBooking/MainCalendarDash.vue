<template>
    <div class="main-container" >
        <SideBar class="collums-1" />
        <div class="collums-2">
            <DayComponent/>
        </div>
        
    </div>
    
</template>

<style lang="scss" scoped>

.main-container{
    display: flex;
    height: 98vh;
    .collums-1{
        width: 30%;
        columns: 1;
        min-width: 14rem;

    }
    .collums-2{
        display: flex;
        justify-content: start;
        columns: 2;
    }
}   



</style>
<script>
import SideBar from './SideBar.vue'
import DayComponent from './DayComponent.vue'

export default {
    components: {
        SideBar,
        DayComponent
    }
}
</script>