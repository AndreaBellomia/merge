<!-- <TicketTypeListItem :title="'730'" :context="'ciao franconi'" /> -->

<template>
    <div class="custom-card">
        <div class="custom-card-container">
            <div class="custom-card-img">
                <h3>{{ title }}</h3>
            </div>
            <div class="custom-container-content">
                <h2>{{ title }}</h2>
                <div class="custom-container-description">
                    <p>{{ context }}</p>
                </div>
                <RouterLink class="custom-btn-router"
                    :to="{ name: 'FormAddTicketView', params: {id: formId} }">
                    <p class="">
                        Richiedi
                    </p>
                    
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: true
        },
        context: {
            type: String,
            required: true
        },
        img: {
            type: String,
            required: false
        },
        formId: {
            type: Number,
            required: true
        }
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
    overflow: hidden;

    .custom-card-container {
        position: relative;
        display: flex;
        max-height: 6rem;

        
        .custom-card-img{
            width: 50%;
            max-width: 6rem;
            aspect-ratio: 1 / 1;
            display: flex;
            justify-content: center;
            align-items: center;

            background: linear-gradient(17deg, rgba(69,2,149,1) 0%, rgba(199,0,255,1) 100%);
            overflow: hidden;
            border-right: 2px solid gray ;
            
            h3{ 
                color: white;
                font-size: 4rem;
                font-weight: 600;
                transform: rotate(-30deg);
            }
        }

        .custom-container-content{
            width: auto;
            margin-left: 0.5rem;

            h2 {
                font-size: 1.5rem;
                font-weight: 600;
            }

            .custom-container-description{
                height: 40%;
                margin-right: 1rem;
                overflow: hidden;
                p{
                    font-size: 0.8rem;
                    font-weight: 400;
                }
            }
            

            .custom-btn-router {
                position: absolute;
                right: 1rem;
                color: #6A2EFF;
            }
        }
    }
}

</style>