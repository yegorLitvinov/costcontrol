<template>
  <div class="bg-light">
    <p class="text-uppercase p-4">Latest Activity</p>
    <activity-item v-for="(record, _, index) in history" :key="index" :record="record"></activity-item>
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import { mapState } from 'vuex'

import { RootState } from '../../../types'
import ActivityItem from './Item.vue'

export default {
  name: 'activity',
  computed: mapState({
    history: (state: RootState) => state.costcontrol.history
  }),
  components: { ActivityItem }
}
</script>
