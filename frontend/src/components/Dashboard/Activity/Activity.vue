<template>
  <div class="bg-light" v-infinite-scroll="loadHistory" infinite-scroll-disabled="busy" infinite-scroll-distance="10">
    <p class="text-uppercase p-4">Latest Activity</p>
    <activity-item v-for="(record, _, index) in history" :key="index" :record="record"></activity-item>
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import { mapState } from 'vuex'

import { RootState } from '../../../types'
import ActivityItem from './ActivityItem.vue'

export default Vue.extend({
  name: 'activity',
  components: { ActivityItem },
  data() {
    return {
      page: 0,
      isLoading: false
    }
  },
  computed: mapState({
    history: (state: RootState) =>
      state.costcontrol.historyOrderedIds.map(id => state.costcontrol.historyEntities[id])
  }),
  methods: {
    loadHistory() {
      this.page += 1
      this.isLoading = true
      this.$store
        .dispatch('costcontrol/getHistory', { page: this.page })
        .then(() => {
          this.isLoading = false
        })
        .catch(() => {
          this.isLoading = false
        })
    }
  }
})
</script>
