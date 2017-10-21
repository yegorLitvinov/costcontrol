<template>
  <div class="d-flex justify-content-between">
    <div>Statistics</div>
    <div class="d-flex justify-content-end">
      <b-form-select :options="years" v-model="year" class="mx-2 px-2 py-0 round-select"></b-form-select>
      <b-form-select :options="monthes" v-model="month" class="mx-2 px-2 py-0 round-select"></b-form-select>
    </div>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'dashboard-statistics',
  components: {},
  data: () => ({
    years: [{ text: 'Year', value: null }, 2017],
    monthes: [
      { text: 'Month', value: null },
      ...moment.months().map((name, index) => ({ value: index, text: name.substr(0, 3) }))
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
  width: 90px;
}
</style>
