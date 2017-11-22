<template>
  <div class="w-100 d-flex flex-column">
    <heading></heading>
    <div class="row m-0">
      <b-col cols="12" md="2" class="m-0 p-0">
        <sidebar />
      </b-col>
      <b-col cols="12" md="6" lg="7" class="bg-white m-0 p-3 scroll-content inner-h-100">
        <transition name="fade">
          <router-view></router-view>
        </transition>
      </b-col>
      <b-col cols="12" md="4" lg="3" class="m-0 p-0 scroll-content inner-h-100">
        <activity></activity>
      </b-col>
    </div>
  </div>
</template>

<script>
import Heading from './Heading'
import Sidebar from './Sidebar/Sidebar'
import Activity from './Activity/Activity'

export default {
  name: 'dashboard',
  components: { Heading, Sidebar, Activity },
  mounted() {
    const token = sessionStorage.getItem('token')
    const id = sessionStorage.getItem('userId')
    if (token && id) {
      this.$store.commit('accounts/setUser', { id, token })
    } else {
      this.$router.push('/')
      return
    }
    this.$store.dispatch('costcontrol/get', { what: 'costcontrol/category/?kind=spending', where: 'spendingCategories' })
    this.$store.dispatch('costcontrol/get', { what: 'costcontrol/category/?kind=proceed', where: 'proceedCategories' })
    this.$store.dispatch('costcontrol/get', { what: 'costcontrol/history/', where: 'history' })
    this.$store.dispatch('costcontrol/get', { what: 'costcontrol/filled-monthes/', where: 'filledMonthes' })
  }
}
</script>

<style scoped lang="scss">
@import "../../styles/constants";

.scroll-content {
  overflow-y: scroll;
  overflow-x: hidden;
  &::-webkit-scrollbar-track {
    border-radius: 10px;
    background-color: $light;
  }

  &::-webkit-scrollbar {
    width: 5px;
    background-color: $light;
  }

  &::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background-color: $primary;
  }
}
</style>
