<template>
  <b-row class="m-0 p-0">
    <b-col cols="6">Statistics</b-col>
    <b-col cols="6" class="d-flex justify-content-end">
      <b-form-select :options="years" v-model="year" class="mx-2 px-2 py-0 round-select"></b-form-select>
      <b-form-select :options="monthes" v-model="month" class="mx-2 px-2 py-0 round-select"></b-form-select>
    </b-col>
  </b-row>
</template>

<script>
import moment from 'moment'

export default {
  name: 'dashboard-statistics',
  components: { },
  data: () => ({
    years: [{ text: 'Year', value: null }, 2017],
    monthes: [
      { text: 'Month', value: null },
      ...moment.months().map((name, index) => ({value: index, text: name}))
    ],
    month: null,
    year: null
  })
}
</script>

<style scoped lang="scss">
@import '../../styles/constants';

.round-select {
  background-color: $warning;
  color: white;
  border-radius: 10px;
  border: none;
  height: 25px !important;
}
</style>
