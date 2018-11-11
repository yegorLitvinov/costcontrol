<template>
<div>
  <div class="d-flex justify-content-between">
    <div>Statistics</div>
  </div>
    <b-row>
      <b-col cols="12" class="mb-3">
        <balance-line-chart
          v-if="statistics.length"
          :chartData="chartData"
          label="Spendings"
        />
      </b-col>
    </b-row>
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import axios from 'axios'
import Component from 'vue-class-component'
import { Watch } from 'vue-property-decorator'
import * as moment from 'moment'

import BalanceLineChart from './BalanceLineChart.vue'
import {
  CategoryStatistic,
  FilledMonthes,
  ChartData,
  Category,
  RootState,
  CategoryYearStatistics
} from '../../../types'

@Component({
  name: 'category-statistics',
  components: { BalanceLineChart }
})
export default class Statistics extends Vue {
  statistics: CategoryYearStatistics[] = []

  get filledMonthes(): FilledMonthes {
    return this.$store.state.costcontrol.filledMonthes
  }

  get years(): string[] {
    return Object.keys(this.filledMonthes)
  }

  get id(): number {
    return parseInt(this.$route.params.category, 10)
  }

  get category(): Category {
    const state = (this.$store.state as RootState).costcontrol
    return state.spendingCategoriesEntities[this.id] || state.proceedCategoriesEntities[this.id] || {}
  }

  get chartData(): ChartData {
    return {
      labels: this.statistics.map(item => item.year_month),
      datasets: [
        {
          label: this.category.name,
          backgroundColor: this.category.color,
          data: this.statistics.map(item => item.total)
        }
      ]
    }
  }

  fetchStatistics() {
    axios
      .get<CategoryYearStatistics[]>(`/costcontrol/categories/${this.id}/year_statistics/`)
      .then(response => {
        this.statistics = response.data
      })
  }

  mounted() {
    this.fetchStatistics()
  }

  @Watch('year')
  onYearChange() {
    this.fetchStatistics()
  }
}
</script>
