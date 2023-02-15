<template>
    <div style="position: absolute"> 


        <div style="position: absolute">
            <div class="day-header">
                <h1>9</h1>
                <div class="info-header">
                    <h2>Giovedi</h2>
                    <h2>Febbraio</h2>
                </div>
            </div>
            <div v-for="index in 24" :key="index" class="background-grid">
                    <p>{{ index }}</p>
                    <div class="row-grid"></div>
            </div>
        </div>
        

        <div class="item" :style="provaItem()">
        
        </div>
    </div>
</template>

<style lang="scss" scoped>
.day-header{
    display: flex;
    left: 14rem;
    box-shadow: -0px 10px 16px -15px rgb(73, 73, 73);


    h1 {
        font-size: 3rem;
        padding: 0.35rem 0rem;
        margin-top: -0.25rem;
        margin-left: 1rem;
    }

    .info-header{
        margin-top: 1rem;
        margin-left: 0.5rem;

        h2 {
            font-size: 1.2;
            margin-top: -0.25rem;
        }
    }

    
    
}

.background-grid{
    display: flex;
    align-items: center;
    justify-content: center;
    height: calc(92vh / 24);
    min-height: 1.5rem;
    top: 4.5rem;
    margin-left: 1rem;
    

    p {
        padding-right: 1rem ;
    }

    .row-grid{
        border-bottom: 1px solid #d6d6d6;
        display: flex;
        width: 96vw;
    }
}
.item{
    display: flex;
    background-color: #ff0d0d5c;
    
    width: 96vw;
    position: absolute;
    padding-right: 1vw ;
    margin-left: calc(2vw + 0.8rem);

}



.card-component {
  width: 100%;
  direction: rtl;
  .header-list{
    height: 6vh;
    box-shadow: -0px 10px 16px -15px rgb(73, 73, 73);
  }
  .compnent-list-day{
    height: 92vh; //or whatever percentage is needed
    overflow-y: auto;
    
  }
}
/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1;
  
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 1rem;
  
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
  border-radius: 5rem;
  
  
}
</style>

<script>
export default {
    data() {
        return {
            durata: 1,
            ora: 2,
        }
    },
    methods: {
        provaItem: function () {
            return `margin-top: calc(100vh/24*${this.ora} - 2.1vh); height: calc(100vh/24*${this.durata});`
        }
    }
}
</script>