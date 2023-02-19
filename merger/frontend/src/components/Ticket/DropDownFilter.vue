<template>
    <div>
        <div class="custom-filter-background">
            <div class="custom-filter-dropdown">
                <header>
                    <div class="custom-header-container">
                        <h1>Filtra</h1>
                        <span class="material-symbols-outlined">
                            filter_list
                        </span>
                    </div>
                    
                    <button class="custom-btn-filter-delete">Cancella FIltri</button>
                </header>
                <main>
                    <div class="custom-filter-body-form">
                        <div>
                            <div class="custom-input-dropwdon">
                                <p>Stato Ticket</p>
                                <span class="material-symbols-outlined" :class="`${stateTicket ? 'active': ''}`"  @click="styleDropDownButtonState()">
                                    arrow_drop_down
                                </span>
                            </div>
                            <div class="custom-dropdown-menu" :class="`${stateTicket ? 'active': ''}`">
                                <ul>
                                    <li>Completato </li>
                                    <li>In Lavorazione </li>
                                    <li>Documenti Richiesti </li>
                                    <li>Inviato </li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div class="custom-input-dropwdon mt-5">
                                <p>Tipo Ticket</p>
                                <span class="material-symbols-outlined " :class="`${typeTciket ? 'active': ''}`"  @click="styleDropDownButtonType()">
                                    arrow_drop_down
                                </span>
                            </div>
                            <div class="custom-dropdown-menu" :class="`${typeTciket ? 'active': ''}`">
                                <ul>
                                    <li>730 </li>
                                    <li>ISEE </li>
                                </ul>
                            </div>
                        </div>


                        <div class="mt-6 mb-2">
                            <div class="custom-section-container">
                                <h2 class="mb-2">Filtra Data</h2>
                            </div>

                            <div class="custom-container-date">
                                <input type="date" class="custom-input-date" placeholder="Da data">
                                <span class="material-symbols-outlined">
                                    chevron_right
                                </span>
                                <input type="date" class="custom-input-date" placeholder="A data">
                            </div>
                            
                            
                        </div>
                        
                        <div>
                            <input type="text" class="custom-input-find" placeholder="Ricerca personalizzata">

                            
                        </div>

                        <div>
                            <p>Chiudi</p>
                        </div>
                        
                        
                    </div>
                </main>
                
            </div>
        </div>
    </div>
</template>

<script>
export default  {
    data () {
        return {
            stateTicket: false,
            typeTciket: false,

        }
    },
    methods: {
        styleDropDownButtonState: function () {
            this.typeTciket = false
            this.stateTicket = !this.stateTicket
        },
        styleDropDownButtonType: function () {
            this.typeTciket = !this.typeTciket
        },
    }
}
    
</script>



<style scoped lang="scss">

.custom-filter-background{
    position: absolute;
    background-color: #00000073;
    height: 100%;
    width: 100%;
    top: 0px;

    .custom-filter-dropdown{
        position: relative;
        background-color: #1F1F1F;
        width: 100%;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.4);
        border-radius: 0px 0px 28px 28px;

        header {
            margin: 0rem 5%;

            .custom-header-container{
                display: flex;
                justify-content: space-between;
                align-items: center;

                h1 {
                    font-size: 2.2rem;
                    color: white;
                    font-weight: 600;
                }

                .material-symbols-outlined {
                    color: white;
                    font-size: 3.5rem;
                    margin-top: 0.75rem;
                }
            }

            .custom-btn-filter-delete{
                color: white;
                font-weight: 500;
                padding: 0.15rem 0.75rem;
                border: solid 2px white;
                border-radius: 8px;

                &:hover {
                    background-color: #ffffff77;
                }

                &:focus {
                    background-color: #ffffff;
                    color: #000000;
                }
            
            }
        }

        
        
    }

    .custom-filter-body-form {
        position: relative;
        margin: 1rem 5%;

        .custom-input-dropwdon{
            position: inherit;
            display: flex;
            height: 2.5rem;
            justify-content: space-between;
            align-items: center;
            color: white;
            background-color: #444444;
            padding: 0% 2%;
            border: 1px solid #BCBCBC;
            border-radius: 8px;
            
            p{
                position: inherit;
                font-weight: 300;
            }

            .material-symbols-outlined{
                transition: transform 0.2s ease-in;
                user-select: none;
                cursor: pointer;
            }

            .material-symbols-outlined.active{
                transform: rotate(180deg);
                transition: transform 0.2s ease-in;

            }
        }

        .custom-dropdown-menu{
            position: absolute;
            width: 100%;
            visibility: hidden;
            opacity: 0;

            margin-top: 0.25rem;
            background-color: #444444;
            border: 1px solid #BCBCBC;
            border-radius: 8px;
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.4);
            transition: visibility 0.2s, opacity 0.2s ease;


            ul {
                position: relative;
                width: 100%;
                li {
                    position: relative;
                    width: 100%;
                    color: white;
                    padding: 0.25rem 0rem;
                    padding-left: 0.5rem;
                    margin: 0.25rem 0rem;
                    user-select: none;
                    cursor: pointer;
                    
                    &:hover {
                        background-color: #7a7a7a;
                    }
                }
            }
            
        }

        .custom-dropdown-menu.active {
            visibility: visible;
            opacity: 1;
            transition: visibility 0s, opacity 0.2s linear;

        }

        .custom-section-container{
            margin: 0px;
            padding: 0px;
            display: flex;
            justify-content: center;
            h2 {
                
                position: inherit;
                color: white;
            }
        }

        
    }

    .custom-container-date {
        position: inherit;
        display: flex;
        justify-content: space-between;
        .custom-input-date{
            color: white;
            width: 45%;
            border: 1px solid #bcbcbc;
            border-radius: 8px;
            padding: 0.25rem 1rem;
            background-color: #444444;
        }
        .material-symbols-outlined{
            color: white;
            margin-top: 0.25rem;
        }
    }

    .custom-input-find{
        position: inherit;
        color: white;
        width: 100%;
        border: 1px solid #bcbcbc;
        border-radius: 8px;
        padding: 0.25rem 1rem;
        background-color: #444444;
        margin-top: 3rem;
        margin-bottom: 1rem;
    }


}


</style>