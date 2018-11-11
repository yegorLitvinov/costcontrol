<template>
<div>
  <div class="d-flex justify-content-between">
    <div>Statistics</div>
    <div class="d-flex justify-content-end">
      <b-select :options="years" v-model="year" class="mx-2 px-2 py-0 round-select"></b-select>
      <b-select :options="months" v-model="month" class="mx-2 px-2 py-0 round-select"></b-select>
    </div>
  </div>

    <b-row>
      <b-col cols="12" class="mb-3">
        <balance-doughnut-chart
          v-if="spendingStatistics.length"
          :onSectorClick="onSectorClick"
          :items="spendingStatistics"
          label="Spendings"
        />
      </b-col>

      <b-col cols="12" class="mb-3">
        <balance-doughnut-chart
          v-if="proceedStatistics.length"
          :onSectorClick="onSectorClick"
          :items="proceedStatistics"
          label="Proceed"
        />
      </b-col>

      <b-col cols="12" class="mb-3">
        <balance-doughnut-chart
          v-if="spendingStatistics.length || proceedStatistics.length "
          :items="proceedVsSpendingStatistics"
          label="Proceed"
        />
      </b-col>
    </b-row>
  </div>
</template>


<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import Component from 'vue-class-component'
import { Watch } from 'vue-property-decorator'
import * as moment from 'moment'

import BalanceDoughnutChart, { BalanceDoughnutChartItem } from './BalanceDoughnutChart.vue'
import { CategoryStatistic, FilledMonthes, ChartData } from '../../../types'

@Component({
  name: 'dashboard-statistics',
  components: { BalanceDoughnutChart },
})
export default class Statistics extends Vue {
  year = moment().year()
  month = moment().month() + 1

  get filledMonthes(): FilledMonthes {
    return this.$store.state.costcontrol.filledMonthes
  }

  get years(): string[] {
    return Object.keys(this.filledMonthes)
  }

  get months(): { value: number; text: string }[] {
    return moment
      .months()
      .map((month, index) => ({ value: index + 1, text: month.substr(0, 3) }))
      .filter(month => {
        try {
          return this.filledMonthes[this.year][month.value]
        } catch (error) {
          return false
        }
      })
  }

  get spendingStatistics(): CategoryStatistic[] {
    return this.$store.state.costcontrol.spendingStatistics
  }

  get proceedStatistics(): CategoryStatistic[] {
    return this.$store.state.costcontrol.proceedStatistics
  }

  get proceedVsSpendingStatistics(): BalanceDoughnutChartItem[] {
    const proceedTotal = this.proceedStatistics.reduce((prev, curr) => prev + curr.total, 0)
    const spendingTotal = this.spendingStatistics.reduce((prev, curr) => prev + curr.total, 0)
    return [
      { id: 1, name: 'Proceed', color: '#aad962', total: proceedTotal },
      { id: 2, name: 'Spending', color: '#ed0345', total: spendingTotal },
    ]
  }

  fetchStatistics() {
    const { year, month } = this
    this.$store.dispatch('costcontrol/fetchStatistics', { year, month })
  }

  onSectorClick(id: number) {
    this.$router.push(`/dashboard/categories/${id}/`)
  }

  mounted() {
    this.fetchStatistics()
  }

  @Watch('year')
  onYearChange() {
    this.fetchStatistics()
  }

  @Watch('month')
  onMonthChange() {
    this.fetchStatistics()
  }
}
</script>
