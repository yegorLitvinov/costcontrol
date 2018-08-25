<template>
  <div ref="activity" class="bg-light scroll-content inner-h-100">
    <p class="text-uppercase p-4">Latest Activity</p>
    <activity-item v-for="record in history" :key="record.id" :record="record"></activity-item>
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
      isLoading: false,
      scrollDistance: 200
    }
  },
  computed: mapState({
    history: (state: RootState) =>
      state.costcontrol.historyOrderedIds.map(id => state.costcontrol.historyEntities[id])
  }),
  mounted() {
    this.loadHistory()
    window.addEventListener('scroll', this.scroll)
    const element = this.$refs.activity as Element
    element.addEventListener('scroll', this.scroll)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.scroll)
    const element = this.$refs.activity as Element
    element.removeEventListener('scroll', this.scroll)
  },
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
          this.page -= 1
        })
    },
    isAtBottom(): boolean {
      const BOOTSTRAP_MD_MIN = 768
      if (window.outerWidth < BOOTSTRAP_MD_MIN) {
        return (
          window.document.body.scrollHeight - window.scrollY - window.outerHeight <=
          this.scrollDistance
        )
      } else {
        const element = this.$refs.activity as Element
        return (
          element.scrollHeight - element.scrollTop - element.clientHeight <= this.scrollDistance
        )
      }
    },
    scroll() {
      const isAtBottom = this.isAtBottom()
      if (!this.isLoading && isAtBottom) {
        this.loadHistory()
      }
    }
  }
})
</script>
