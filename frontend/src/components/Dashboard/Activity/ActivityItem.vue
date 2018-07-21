<template>
  <div class="pl-4 item-wrapper">
    <div class="activity-item">
      {{ category && (category.kind === 'spending' ? '- ' : '+ ')}}
      {{ `${record.amount}\u20bd (${record.created_at}) ${record.comment} (${category ? category.name : ''})` }}
    </div>
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import { Category, CategoryKind, BalanceRecord, RootState } from '../../../types'
import Vue from 'vue'
import { mapState } from 'vuex'

import BalanceRecordForm from './BalanceRecordForm.vue'

export default Vue.extend({
  name: 'activity-item',
  props: {
    record: {
      type: Object as () => BalanceRecord,
      required: true
    }
  },
  data() {
    return {}
  },
  computed: {
    categories() {
      const state: RootState = this.$store.state
      return {
        ...state.costcontrol.spendingCategoriesEntities,
        ...state.costcontrol.proceedCategoriesEntities
      }
    },
    category(): Category | undefined {
      return this.categories[this.record.category]
    }
  },
  methods: {}
})
</script>

<style scoped lang="scss">
@import '../../../styles/constants';

.activity-item {
  border-left: 2px solid lightgray;
  padding: 20px;

  &::before {
    position: relative;
    top: 10px;
    left: -31px;
    background-color: lightgray;
    color: lightgray;
    text-align: center;
    width: 20px;
    height: 20px;
    border-radius: 10px;
    content: 'o';
    display: inline-block;
  }

  &.selected {
    border-color: white;

    &::before {
      background-color: white;
      color: white;
    }
  }
}

.item-wrapper {
  &:hover {
    background-color: rgba($info, 0.8);
    color: white;
  }
}
</style>
