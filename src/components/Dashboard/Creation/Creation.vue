<template>
  <b-row>
    <b-col cols="12" sm="6" md="12" lg="6">
      <balance-record-form
        :categories="spendingCategories"
        :add-record="this.addSpending"
        :header="'Spending'"
      />
    </b-col>
  </b-row>
</template>

<script>
import Vuex from 'vuex'

import BalanceRecordForm from './BalanceRecordForm'

const mapCategories = (categories) => {
  return categories.map(category => ({
    text: category.name,
    value: category.id
  }))
}

export default {
  name: 'creation',
  components: { BalanceRecordForm },
  computed: Vuex.mapState({
    spendingCategories: state => mapCategories(state.spendingCategories)
  }),
  methods: {
    addSpending: function(record) {
      return this.$store.dispatch(
        'addRecord',
        { type: 'spending', formData: record }
      )
    }
  }
}
</script>
