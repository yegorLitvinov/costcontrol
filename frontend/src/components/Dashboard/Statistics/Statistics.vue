<template>
<div>
  <div class="d-flex justify-content-between">
    <div>Statistics</div>
    <div class="d-flex justify-content-end">
      <b-form-select :options="years" v-model="year" class="mx-2 px-2 py-0 round-select"></b-form-select>
      <b-form-select :options="monthes" v-model="month" class="mx-2 px-2 py-0 round-select"></b-form-select>
    </div>
  </div>

    <b-row>
      <b-col cols="12" sm="6" md="12" lg="6" class="mb-3">
        <balance-doughnut-chart :chartData="spendingChartData" />
      </b-col>

      <b-col cols="12" sm="6" md="12" lg="6" class="mb-3">
        <balance-doughnut-chart :chartData="proceedChartData" />
      </b-col>
    </b-row>
  </div>
</template>

<script>
import moment from 'moment'
import BalanceDoughnutChart from './BalanceDoughnutChart'

export default {
  name: 'dashboard-statistics',
  components: { BalanceDoughnutChart },
  data: () => ({
    year: moment().year(),
    month: moment().month() + 1
  }),
  computed: {
    filledMonthes() {
      return this.$store.state.filledMonthes
    },
    years() {
      return Object.keys(this.$store.state.filledMonthes)
    },
    monthes() {
      return moment.months()
        .map((month, index) => ({ value: index + 1, text: month.substr(0, 3) }))
        .filter((month) => {
          try {
            return this.$store.state.filledMonthes[this.year][month.value]
          } catch (error) {
            return false
          }
        })
    },
    spendingChartData() {
      return this.balanceStatistics(this.$store.state.spendingStatistics, 'Spendings')
    },
    proceedChartData() {
      return this.balanceStatistics(this.$store.state.proceedStatistics, 'Proceeds')
    }
  },
  methods: {
    fetchStatistics() {
      const { year, month } = this
      this.$store.dispatch('fetchStatistics', {year, month})
    },
    balanceStatistics(statistics, label) {
      return {
        labels: statistics.map(category => category.name),
        datasets: [{
          label,
          backgroundColor: statistics.map(category => category.color),
          data: statistics.map(category => category.total)
        }]
      }
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
}
</script>

<style scoped lang="scss">
@import "../../../styles/constants";

.round-select {
  background-color: $warning;
  color: white;
  border-radius: 20px;
  border: none;
  height: 35px !important;
  width: 90px;
}
</style>
