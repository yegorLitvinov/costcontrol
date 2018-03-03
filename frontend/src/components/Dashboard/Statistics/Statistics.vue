<template>
<div>
  <div class="d-flex justify-content-between">
    <div>Statistics</div>
    <div class="d-flex justify-content-end">
      <b-form-select :options="years" v-model="year" class="mx-2 px-2 py-0 round-select"></b-form-select>
      <b-form-select :options="months" v-model="month" class="mx-2 px-2 py-0 round-select"></b-form-select>
    </div>
  </div>

    <b-row>
      <b-col cols="12" class="mb-3">
        <balance-doughnut-chart v-if="spendingStatistics.length" :chartData="spendingChartData" />
      </b-col>

      <b-col cols="12" class="mb-3">
        <balance-doughnut-chart v-if="proceedStatistics.length" :chartData="proceedChartData" />
      </b-col>

      <b-col cols="12" class="mb-3">
        <balance-doughnut-chart
          v-if="spendingStatistics.length || proceedStatistics.length "
          :chartData="proceedVsSpendingChartData"
        />
      </b-col>
    </b-row>
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import * as moment from 'moment'

import BalanceDoughnutChart from './BalanceDoughnutChart.vue'
import { CategoryStatistic, FilledMonthes, ChartData } from '../../../types'

function balanceStatistics(statistics: CategoryStatistic[], label: string): ChartData {
  return {
    labels: statistics.map(category => category.name),
    datasets: [
      {
        label,
        backgroundColor: statistics.map(category => category.color),
        data: statistics.map(category => category.total)
      }
    ]
  }
}

export default Vue.extend({
  name: 'dashboard-statistics',
  components: { BalanceDoughnutChart },
  data: () => ({
    year: moment().year(),
    month: moment().month() + 1
  }),
  computed: {
    filledMonthes(): FilledMonthes {
      return this.$store.state.costcontrol.filledMonthes
    },
    years(): string[] {
      return Object.keys(this.$store.state.costcontrol.filledMonthes)
    },
    months(): {value: number, text: string}[] {
      return moment.months()
        .map((month, index) => ({ value: index + 1, text: month.substr(0, 3) }))
        .filter((month) => {
          try {
            return this.$store.state.costcontrol.filledMonthes[this.year][month.value]
          } catch (error) {
            return false
          }
        })
    },
    spendingStatistics(): CategoryStatistic[] {
      return this.$store.state.costcontrol.spendingStatistics
    },
    proceedStatistics(): CategoryStatistic[] {
      return this.$store.state.costcontrol.proceedStatistics
    },
    spendingChartData(): ChartData {
      return balanceStatistics(this.spendingStatistics, 'Spendings')
    },
    proceedChartData(): ChartData {
      return balanceStatistics(this.proceedStatistics, 'Proceeds')
    },
    proceedVsSpendingChartData(): ChartData {
      const proceedTotal = this.proceedStatistics.reduce((prev, curr) => (prev + curr.total), 0)
      const spendingTotal = this.spendingStatistics.reduce((prev, curr) => (prev + curr.total), 0)
      return {
        labels: ['Proceed', 'Spending'],
        datasets: [{
          label: 'Proceed Vs. Spending',
          backgroundColor: ['#aad962', '#ed0345'],
          data: [proceedTotal, spendingTotal],
        }]
      }
    }
  },
  methods: {
    fetchStatistics() {
      const { year, month } = this
      this.$store.dispatch('costcontrol/fetchStatistics', {year, month})
    }
  },
  mounted() {
    this.fetchStatistics()
  },
  watch: {
    year() {
      this.fetchStatistics()
    },
    month() {
      this.fetchStatistics()
    }
  }
})
</script>
