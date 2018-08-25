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
          v-if="yearStatistics.length"
          :items="proceedVsSpendingStatistics"
          label="Proceed vs Spending"
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

import BalanceDoughnutChart,{ BalanceDoughnutChartItem } from './BalanceDoughnutChart.vue'
import BalanceBarChart from './BalanceBarChart.vue'
import {
  CategoryStatistic,
  FilledMonthes,
  ChartData,
  YearStatistic,
  CategoryKind
} from '../../../types'

function balanceStatistics(
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

@Component({
  name: 'dashboard-year-statistics',
  components: { BalanceDoughnutChart, BalanceBarChart },
})
export default class YearStatistics extends Vue{
  year = moment().year()
  month = moment().month() + 1

  get filledMonthes(): FilledMonthes {
    return this.$store.state.costcontrol.filledMonthes
  }

  get years(): string[] {
    return Object.keys(this.$store.state.costcontrol.filledMonthes)
  }

  get months(): { value: number; text: string }[] {
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
  }

  get yearStatistics(): YearStatistic[] {
    return this.$store.state.costcontrol.yearStatistics
  }

  get proceedYearStatistics(): YearStatistic[] {
    return this.yearStatistics.filter(item => item.category__kind == CategoryKind.Proceed)
  }

  get spendingYearStatistics(): YearStatistic[] {
    return this.yearStatistics.filter(item => item.category__kind == CategoryKind.Spending)
  }

  get lineChartData(): ChartData {
    return balanceStatistics(this.yearStatistics, this.spendingYearStatistics, this.proceedYearStatistics)
  }

  get proceedVsSpendingStatistics(): BalanceDoughnutChartItem[] {
    const proceedTotal = this.proceedYearStatistics.reduce((prev, curr) => prev + curr.total, 0)
    const spendingTotal = this.spendingYearStatistics.reduce((prev, curr) => prev + curr.total, 0)
    return [
      { id: 1, name: 'Proceed', color: '#aad962', total: proceedTotal },
      { id: 2, name: 'Spending', color: '#ed0345', total: spendingTotal }
    ]
  }


  fetchStatistics() {
    const { year } = this
    this.$store.dispatch('costcontrol/fetchYearStatistics', { year })
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
