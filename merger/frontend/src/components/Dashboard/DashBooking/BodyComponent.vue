<template>
  <div>
    <div class="custom-day-card" :class="getCurrentDate()">
      <ul class="body-list-component">
        <li class="colum-1">
          <h1>{{ day }}</h1>
        </li>
        <li class="colum-2">
          <h2>{{ dayName }}</h2>
          <div class="custom-info">
            <ul>
              <li class="appointment">
                <span class="material-symbols-outlined"> schedule </span>
                <p>10</p>
              </li>
              <li class="booking">
                <span class="material-symbols-outlined"> task_alt </span>
                <p>10</p>
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.current-day{
  background-color: #0046d3;

  ul{
    &:hover{
      background-color: #3b7cff !important;
    }
  }
  
  h1, h2 {
    color: #ffffff;
    font-weight: bold;
  }
  .appointment {
    border: 0.15rem solid #ffffff !important;
    color: #ffffff !important;
  }

  .booking {

    border: 0.15rem solid #ffffff !important;
    background-color: #ffffff !important;
    color: #000000 !important;
  }
}



.custom-day-card {
  padding: -1rem 0rem;
  border-bottom: 1px solid #d6d6d6;

  .body-list-component{
    .colum-1{
      display: flex;
      justify-content: center;
      min-width: 4.5rem;
    }

  }

  ul {
    display: flex;
    list-style: none;

    &:hover{
      background-color: #ededed;
    }

    li {
      padding: 0rem 0.25rem;
      padding: -5rem 0rem;

      h1 {
        font-size: 3rem;
      }

      h2 {
        padding-top: 0.9rem;
        text-transform: capitalize;
      }

      .custom-info {
        font-size: 0.75rem;

        .appointment {
          margin-top: 0rem;
          padding: 0rem 0.5rem;
          border-radius: 3rem;
          border: 0.15rem solid #1d4adf;
        }

        .booking {
          margin-left: 0.5rem;
          margin-top: 0rem;
          padding: 0rem 0.5rem;
          border-radius: 3rem;
          border: 0.15rem solid #1d4adf;
          background-color: #1d4adf;
          color: white;
        }

        li {
          padding-left: 0rem;
          display: flex;

          p {
            margin-top: -0.15rem;
            margin-bottom: -0.9rem;
            padding-left: 0.25rem;
            font-size: 0.9rem;
          }

          .material-symbols-outlined {
            font-size: 1rem;
            margin-top: 0.05rem;
            padding-bottom: 0.05rem;
          }
        }
      }
    }
  }
}
</style>

<script>
export default {
  props: {
    day: {
      type: Number,
      required: true,
    },
    dayName: {
      type: String,
    },
    currentDay: {
      type: Boolean,
      default: false,
      required: false,
    }
  },
  methods: {
    getCurrentDate: function () {
      if (this.currentDay) {
        return 'current-day'
      }
    },
  }
};
</script>