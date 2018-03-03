<template>
<div>
  <div class="d-flex justify-content-between">
    <div>Year Statistics</div>
    <div class="d-flex justify-content-end">
      <b-form-select :options="years" v-model="year" class="mx-2 px-2 py-0 round-select"></b-form-select>
    </div>
  </div>
    <b-row>
      <b-col cols="12" class="mb-3">
        <balance-bar-chart
          v-if="yearStatistics"
          :chartData="lineChartData"
        />
      </b-col>

      <b-col cols="12" class="mb-3">
        <balance-doughnut-chart
          v-if="yearStatistics"
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
import BalanceBarChart from './BalanceBarChart.vue'
import {
  CategoryStatistic,
  FilledMonthes,
  ChartData,
  YearStatistic,
  CategoryKind
} from '../../../types'

export function balanceStatistics(
  allStatistics: YearStatistic[],
  spendingStatistics: YearStatistic[],
  proceedStatistics: YearStatistic[],
): ChartData {
  return {
    labels: allStatistics
      .map((item) => item.month)
      .filter((elem, pos, arr) => {
        return arr.indexOf(elem) == pos;
      }),
    datasets: [
      {
        label: 'Spendings',
        backgroundColor: '#ed0345',
        data: spendingStatistics.map(item => ({
          x: item.month,
          y: item.total
        }))
      },
      {
        label: 'Proceeds',
        backgroundColor: '#aad962',
        data: proceedStatistics.map(item => ({
          x: item.month,
          y: item.total
        }))
      }
    ]
  }
}

export default Vue.extend({
  name: 'dashboard-statistics',
  components: { BalanceDoughnutChart, BalanceBarChart },
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
    months(): { value: number; text: string }[] {
      return moment
        .months()
        .map((month, index) => ({ value: index + 1, text: month.substr(0, 3) }))
        .filter(month => {
          try {
            return this.$store.state.costcontrol.filledMonthes[this.year][month.value]
          } catch (error) {
            return false
          }
        })
    },
    yearStatistics(): YearStatistic[] {
      return this.$store.state.costcontrol.yearStatistics
    },
    proceedYearStatistics(): YearStatistic[] {
      return this.yearStatistics.filter(item => item.category__kind == CategoryKind.Proceed)
    },
    spendingYearStatistics(): YearStatistic[] {
      return this.yearStatistics.filter(item => item.category__kind == CategoryKind.Spending)
    },
    lineChartData(): ChartData {
      return balanceStatistics(this.yearStatistics, this.spendingYearStatistics, this.proceedYearStatistics)
    },
    proceedVsSpendingChartData(): ChartData {
      const proceedTotal = this.proceedYearStatistics.reduce((prev, curr) => prev + curr.total, 0)
      const spendingTotal = this.spendingYearStatistics.reduce((prev, curr) => prev + curr.total, 0)
      return {
        labels: ['Proceed', 'Spending'],
        datasets: [
          {
            label: 'Proceed Vs. Spending',
            backgroundColor: ['#aad962', '#ed0345'],
            data: [proceedTotal, spendingTotal]
          }
        ]
      }
    }
  },
  methods: {
    fetchStatistics() {
      const { year } = this
      this.$store.dispatch('costcontrol/fetchYearStatistics', { year })
    }
  },
  mounted() {
    this.fetchStatistics()
  },
  watch: {
    year() {
      this.fetchStatistics()
    }
  }
})
</script>
