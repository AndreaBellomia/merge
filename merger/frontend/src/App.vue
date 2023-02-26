<template>
  <div>
    <section>
      <router-view />
    </section>
    <nav class="custom-navbar">
      <router-link to="/">
        <span @click="selectItem('notifications')" :class="{ 'custom-item-selected': selected['notifications'] }"
          class="custom-item px-3 py-2 flex material-symbols-outlined">
          notifications
        </span>
      </router-link>
      <router-link to="/">
        <span @click="selectItem('chat')" :class="{ 'custom-item-selected': selected['chat'] }"
          class="custom-item px-3 py-2 flex material-symbols-outlined">
          chat
        </span>
      </router-link>
      <router-link to="/MyBookingView">
        <span @click="selectItem('booking')" :class="{ 'custom-item-selected': selected['booking'] }"
          class="custom-item px-3 py-2 flex material-symbols-outlined">
          calendar_month
        </span>
      </router-link>
      <router-link to="/MyTicketView">
        <span @click="selectItem('ticket')" :class="{ 'custom-item-selected': selected['ticket'] }"
          class="custom-item px-3 py-2 flex material-symbols-outlined">
          confirmation_number
        </span>
      </router-link>
      <router-link to="/">
        <span @click="selectItem('profile')" :class="{ 'custom-item-selected': selected['profile'] }"
          class="custom-item px-3 py-2 flex material-symbols-outlined">
          account_circle
        </span>
      </router-link>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selected: {
        ['notifications']: false,
        ['chat']: false,
        ['booking']: true,
        ['ticket']: false,
        ['profile']: false
      }
    }
  },
  methods: {
    selectItem(id) {
      //initial state of selected
      this.selected = {
        ['notifications']: false,
        ['chat']: false,
        ['booking']: false,
        ['ticket']: false,
        ['profile']: false
      }
      //select item
      this.selected[id] = !this.selected[id]
    }
  }
}
</script>

<style scoped lang="scss">
.custom-navbar {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  position: fixed;
  bottom: 0;
  width: 100%;
  background: #1F1F1F;
  border-top: 2px solid #E3E3E3;
  padding: 1rem;

  .custom-item {
    color: #F8FCFF;
    font-size: xx-large;
    -webkit-user-select: none;
    cursor: pointer;
  }

  .custom-item-selected {
    color: #A771FF !important;
    border-bottom: 4px solid #A771FF;
    box-shadow: 0px 4px 2px rgba(0, 0, 0, 0.5);
  }

  .custom-item-selected-undo {
    color: #A771FF !important;
    border-bottom: 4px solid #A771FF;
    box-shadow: 0px 4px 2px rgba(0, 0, 0, 0.5);
  }
}
</style>