<template>
    <div>
        <div :class="[dropActive ? 'active' : '', 'custom-filter-background']">
            <div :class="[dropActive ? 'active' : '', 'custom-filter-dropdown']">
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
                            <div class="custom-input-dropwdon"  @click="stateTicket = true">
                                <p>Stato Ticket</p>
                                <span :class="[stateTicket ? 'active': '', 'material-symbols-outlined']">
                                    arrow_drop_down
                                </span>
                            </div>
                            <div :class="[stateTicket ? 'active': '', 'custom-dropdown-menu']" @mouseleave="stateTicket = false">
                                <ul>
                                    <li>Completato </li>
                                    <li>In Lavorazione </li>
                                    <li>Documenti Richiesti </li>
                                    <li>Inviato </li>
                                </ul>
                            </div>
                        </div> 

                        <div class="mt-5">
                            <div class="custom-input-dropwdon" @click="typeTiket = true">
                                <p>Tipo Ticket</p>
                                <span :class="[typeTiket ? 'active': '', 'material-symbols-outlined']">
                                    arrow_drop_down
                                </span>
                            </div>
                            <div :class="[typeTiket ? 'active': '', 'custom-dropdown-menu']" @mouseleave="typeTiket = false">
                                <ul class="scroll">
                                    <li v-for="item in ticketType" :key="item" @click="''">
                                    <span class="material-symbols-outlined">
                                        done
                                    </span>
                                    {{ item.title }}
                                    </li>
                                </ul>
                            </div>

                            <div class="custom-container-date">
                                <h2>Filtra Data</h2>
                                <div class="flex flex-col items-start w-full">
                                    <h3 class="">Da data</h3>
                                    <input type="date" class="mt-2">
                                </div>
                                
                                <div class="flex flex-col items-start w-full mt-3">
                                    <h3 class="">A data</h3>
                                    <input type="date" class="mt-2">
                                </div>
                            </div>

                            <div class="custom-find-container mt-10">
                                
                                <input type="text" class="custom-input-find" placeholder="Cerca per titolo...">
                                <span class="material-symbols-outlined">
                                    search
                                </span>
                            </div>

                            <div class="custom-container-close">
                                <h2 @click="$emit('filterClose')">chiudi</h2>
                            </div>
                        </div> 
                    </div>
                </main>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default  {
    props: {
        dropActive: {
            type: Boolean,
            required: true
        }
    },
    data () {
        return {
            stateTicket: false,
            typeTiket: false,
            ticketType: Object,

        }
    },
    mounted() {
        this.getHTTP_ticketTypeList()
    },
    methods: {
        
        getHTTP_ticketTypeList: function () {
            axios
                .get("api/client/ticket-tipe/")
                .then((response) => {
                    this.ticketType = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

    }
}
    
</script>



<style scoped lang="scss">

.custom-filter-background{
    display: none;
    position: absolute;
    background-color: #00000073;
    height: 100%;
    width: 100%;
    top: 0px;

    &.active {
        display: block;
    }

    

    .custom-filter-dropdown{
        top: -100%;
        position: relative;
        background-color: #1F1F1F;
        width: 100%;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.4);
        border-radius: 0px 0px 28px 28px;

        transition: top 0.5s ease-out;

        &.active {
            top: 0%;
            transition: top 0.5s ease-out;
        }

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
                
                user-select: none;

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
            position: relative;
            display: flex;
            width: 100%;
            justify-content: space-between;
            color: white;
            background-color: #444444;
            padding: 0.5rem 0.75rem;
            border: 1px solid #BCBCBC;
            border-radius: 8px;

            user-select: none;
            cursor: pointer;
            
            p{
                position: inherit;
                font-weight: 300;
            }

            .material-symbols-outlined{
                transition: transform 0.2s ease-in;
            }

            .material-symbols-outlined.active{
                transform: rotate(180deg);
                transition: transform 0.2s ease-in;

            }
        }

        .custom-dropdown-menu{
            position: absolute;
            width: 100%;
            z-index: 10;

            margin-top: 0.3rem;
            background-color: #2e2e2e;
            border-radius: 8px;
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.4);
            transition: visibility 0.2s, opacity 0.2s ease;

            visibility: hidden;
            opacity: 0;

            ul {
                width: 100%;
                margin: 0.25rem 0rem;
                

                &.scroll {
                    max-height: 10rem;
                    overflow-y: scroll;
                }

                li {
                    display: flex;
                    align-items: center;
                    color: white;
                    padding: 0.25rem 0rem;
                    padding-left: 1rem;
                    user-select: none;
                    cursor: pointer;

                    .material-symbols-outlined{
                        font-size: 1rem;
                        margin-right: 0.25rem;
                        opacity: 0;

                        &.active {
                            opacity: 1;
                        }
                    }
                    
                    &:hover {
                        background-color: #5c5c5c;
                    }
                }
            }

            &.active {
                visibility: visible;
                opacity: 1;
                transition: visibility 0s, opacity 0.2s linear;
            }
            
        }

        .custom-container-date{
            position: relative;
            display: flex;
            flex-direction: column;
            width: 100%;
            align-items: center;

            h2{ 
                margin-top: 2rem;
                color: white;
                font-weight: 600;
            }

            h3{
                color: #fff;
            }

            input {
                color: #fff;
                width: 100%;
                background-color: #444444;
                padding: 0.5rem 0.75rem;
                border: 1px solid #BCBCBC;
                border-radius: 8px;
                color-scheme: dark;
            }
        }

        .custom-container-close{
            position: relative;
            display: flex;
            flex-direction: column;
            width: 100%;
            align-items: center;

            h2{ 
                color: white;
                font-weight: 400;
                margin-bottom: 0.5rem;
                user-select: none;
            }
        }
    }

    .custom-find-container{
        .custom-input-find{
            position: inherit;
            color: white;
            width: 100%;
            border: 1px solid #bcbcbc;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            padding-right: 2.5rem;
            background-color: #444444;

            
        }

        .material-symbols-outlined {
            position: relative;
            color: white;
            top: -2rem;
            left: calc(100% - 2rem);
            user-select: none;
            cursor: pointer;
        }
    }
        


}

/* width */
::-webkit-scrollbar {
    width: 4px;
  }
  
  /* Track */
  ::-webkit-scrollbar-track {
    background: #444444;
    border-radius: 1rem;
  }
  
  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 1rem;
  }
  
  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #555;
  }

</style>