<template>
  <b-row class="m-0 p-0">
    <b-col cols="6">Statistics</b-col>
    <b-col cols="6" class="d-flex justify-content-end">
      <round-select name="Year" :options="years" />
      <round-select name="Month" :options="monthes" />
    </b-col>
  </b-row>
</template>

<script>
import moment from 'moment'

import RoundSelect from './RoundSelect'

export default {
  name: 'dashboard-statistics',
  components: { RoundSelect },
  data: () => ({
    years: [[2017, 2017]],
    monthes: moment.months().map((name, index) => ([index, name]))
  })
}
</script>
