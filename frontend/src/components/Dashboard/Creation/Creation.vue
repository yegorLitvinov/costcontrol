<template>
  <b-row>
    <b-col cols="12" sm="6" md="12" lg="6" class="mb-3">
      <balance-record-form
        :categories="spendingCategories"
        :add-record="this.addSpending"
        header="Spending"
      />
    </b-col>

    <b-col cols="12" sm="6" md="12" lg="6" class="mb-3">
      <balance-record-form
        :categories="proceedCategories"
        :add-record="this.addProceed"
        header="Proceed"
      />
    </b-col>
  </b-row>
</template>

<script lang="ts" type="text/prs.typescript">
import { Category, CategoryKind, BalanceRecord, RootState } from '../../../types'
import Vue from 'vue'
import { mapState } from 'vuex'

import BalanceRecordForm from './BalanceRecordForm.vue'

const mapCategories = (categories: Category[]) => {
  return categories.map(category => ({
    text: category.name,
    value: category.id,
  }))
}

export default Vue.extend({
  name: 'creation',
  components: { BalanceRecordForm },
  data() {
    return {}
  },
  computed: mapState({
    spendingCategories: (state: RootState) =>
      mapCategories(
        state.costcontrol.spendingCategoriesOrderedIds.map(
          id => state.costcontrol.spendingCategoriesEntities[id]
        )
      ),
    proceedCategories: (state: RootState) =>
      mapCategories(
        state.costcontrol.proceedCategoriesOrderedIds.map(
          id => state.costcontrol.proceedCategoriesEntities[id]
        )
      ),
  }),
  methods: {
    addSpending: function(record: BalanceRecord) {
      return this.$store.dispatch('costcontrol/addRecord', {
        type: 'spending',
        ...record,
      })
    },
    addProceed: function(record: BalanceRecord) {
      return this.$store.dispatch('costcontrol/addRecord', {
        type: 'proceed',
        ...record,
      })
    },
  },
})
</script>
