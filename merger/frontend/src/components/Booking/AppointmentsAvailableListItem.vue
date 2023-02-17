<template>
    <div class="custom-card">
        <div class="custom-card-container">
            <div class="flex flex-col items-start">
                <span class="custom-card-header"> 14:00 - 16:00
                </span>
                <span class="custom-card-text">nome cognome amm</span>
            </div>
            <div class="flex flex-col items-center">
                <span class="custom-card-icon material-symbols-outlined">
                    chevron_right
                </span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
}
</script>

<style scoped lang="scss">
.custom-card {
    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 14px;
    margin: 0.6rem;
    border-left: 8px solid #1ABD00;

    .custom-card-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 0.5rem;
    }

    .custom-card-header {
        font-style: normal;
        font-weight: 600;
        line-height: 19px;
        font-size: 1rem;
        margin: 0.5rem;
        margin-bottom: 0rem;
        color: #000000;
    }

    .custom-card-text {
        font-style: normal;
        font-weight: 400;
        font-size: 0.75rem;
        display: flex;
        align-items: center;
        text-align: center;
        margin: 0.5rem;
        color: #000000;
    }

    .custom-card-secondary-text {
        font-style: normal;
        font-weight: 300;
        font-size: 10px;
        line-height: 12px;
        color: #000000;
        margin: 0.5rem;
    }

    .custom-card-icon {
        margin: 1rem;
        font-size: 2.5rem;
        color: #5C5A60;
    }
}
</style>

