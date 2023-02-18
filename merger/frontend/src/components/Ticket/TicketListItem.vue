<template>
    <div class="custom-card" >
        <div class="custom-card-container">
            <div class="flex flex-col items-start">
                <span class="custom-card-header">{{ ticket.type_document.title }}</span>
                <span class="custom-card-text">{{ ticket.object }}</span>
            </div>
            <div class="flex flex-col items-center">
                <span class="custom-card-secondary-text">Id {{ ticket.id }}</span>
                <span class="custom-card-icon material-symbols-outlined">
                    chevron_right
                </span>
            </div>
        </div>
        <div class="custom-progres-bar-container">
            <div class="custom-progress-bar-background">
                <p>{{ state }}</p>
                <div class="custom-progress-state" :style="styleStatusProgresBar()"/>
                
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        ticket: {
            type: Object,
            required: true
        }
    },
    data () {
        return {
            state: String,
        }
    },
    methods: {
        styleStatusProgresBar: function () {
            if (this.ticket.status == "SEND") {
                this.state = 'Inviato'
                return 'background-color: #8F62DA; width: 5%;'
            } else if (this.ticket.status == "WAIT" || this.ticket.status == "START" ) {
                this.state = 'In lavorazione'
                return 'background-color: #FFB800; width: 70%'
            } else if (this.ticket.status == "BUSY") {
                this.state = 'Documenti Richeisti'
                return 'background-color: #FF1F00; width: 35%'
            } else if (this.ticket.status == "COMP") {
                this.state = 'Completato'
                return 'background-color: #1ABD00; width: 100%'
            }
        },
    }

}
</script>


<style scoped lang="scss">
.custom-card {
    position: relative;
    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 14px;
    margin: 0.6rem;

    .custom-status-bar{
        position: absolute;
        top: 50%;
        transform: translate(0%, -50%);
        height: 80%;
        width: 0.35rem;
        border-radius: 0.5rem;
        background-color: #686868;
    }

    .custom-card-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 0.5rem;
        margin-left: 0.25rem;
    }

    .custom-card-header {
        font-style: normal;
        font-weight: 600;
        line-height: 19px;
        font-size: 1.25rem;
        margin: 0.5rem;
        margin-bottom: 0rem;
        color: #000000;
    }

    .custom-card-text {
        font-style: normal;
        font-weight: 400;
        font-size: 0.85rem;
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
        -webkit-user-select: none;
        cursor: pointer;
    }

    .custom-progres-bar-container{
        bottom: 1rem;
        position: relative;
        width: 100%;

        .custom-progress-bar-background{
            position: relative;
            width:calc(93% - 0.75rem );
            left: 1.2rem;
            height: 0.4rem;
            background-color: #9c9c9c;
            border-radius: 10rem;

            p {
                position: relative;
                top: -1.2rem;
                font-size: 0.8rem;
                font-weight: 500;
            }

            .custom-progress-state {
                position: relative;
                top: -1.2rem;
                height: 0.4rem;
                border-radius: 10rem;
                background-color: #575757;
            }
        }
    }
}


</style>