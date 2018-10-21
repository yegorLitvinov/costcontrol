<template>
  <div ref="activity" class="bg-light scroll-content inner-h-100">
    <p class="text-uppercase p-4">Latest Activity</p>
    <b-form-group class="m-4">
      <b-input placeholder="Search" v-model="search" @change="handleSearchChange" />
    </b-form-group>
    <activity-item v-for="record in history" :key="record.id" :record="record"></activity-item>
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import { mapState } from 'vuex'

import { RootState, BalanceRecord, PaginatedResults } from '../../../types'
import ActivityItem from './ActivityItem.vue'

export default Vue.extend({
  name: 'activity',
  components: { ActivityItem },
  data() {
    return {
      page: 0,
      search: '',
      count: Infinity,
      isLoading: false,
      scrollDistance: 200,
    }
  },
  computed: {
    history(): BalanceRecord[] {
      const state: RootState = this.$store.state
      return state.costcontrol.historyOrderedIds.map(id => state.costcontrol.historyEntities[id])
    },
    category(): number | undefined {
      const category: string | undefined = this.$route.params.category
      return category ? parseInt(category, 10) : undefined
    },
  },
  watch: {
    category(val) {
      this.clearHistory()
      this.loadHistory()
    },
  },
  mounted() {
    this.loadHistory()
    window.addEventListener('scroll', this.scroll)
    const element = this.$refs.activity as Element
    element.addEventListener('scroll', this.scroll)
  },
  beforeDestroy() {
    this.clearHistory()
    window.removeEventListener('scroll', this.scroll)
    const element = this.$refs.activity as Element
    element.removeEventListener('scroll', this.scroll)
  },
  methods: {
    loadHistory() {
      if (this.history.length === this.count) {
        return
      }
      this.page += 1
      this.isLoading = true
      const { category, search } = this
      this.$store
        .dispatch('costcontrol/getHistory', { page: this.page, category, search })
        .then((data: PaginatedResults<BalanceRecord>) => {
          this.isLoading = false
          this.count = data.count
        })
        .catch(() => {
          this.isLoading = false
          this.page -= 1
        })
    },
    clearHistory() {
      this.page = 0
      this.count = Infinity
      this.$store.commit('costcontrol/clearHistory')
    },
    handleSearchChange() {
      this.clearHistory()
      this.loadHistory()
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
    },
  },
})
</script>
