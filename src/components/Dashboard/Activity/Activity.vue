<template>
  <div class="bg-light inner-h-100 activity">
    <p class="text-uppercase p-4">Latest Activity</p>
    <activity-item v-for="(record, _, index) in history" :key="index" :record="record"></activity-item>
  </div>
</template>

<script>
import Vuex from 'vuex'

import ActivityItem from './Item'

export default {
  name: 'activity',
  computed: Vuex.mapState({
    history: state => state.history
  }),
  components: { ActivityItem },
  mounted() {
    this.$store.dispatch('get', { what: '/api/history/20/', where: 'history' })
  }
}
</script>

<style scoped lang="scss">
.activity {
  overflow-y: scroll;
  overflow-x: hidden;
}
</style>
