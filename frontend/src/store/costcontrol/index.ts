import Vue from 'vue'
import { Module } from 'vuex'

import mutations from './mutations'
import actions from './actions'
import { CostcontrolState, RootState } from '../../types'

const State: CostcontrolState = {
  historyOrderedIds: [],
  historyEntities: {},
  spendingCategoriesEntities: {},
  spendingCategoriesOrderedIds: [],
  proceedCategoriesEntities: {},
  proceedCategoriesOrderedIds: [],
  spendingStatistics: [],
  proceedStatistics: [],
  filledMonthes: {}
}

export default class CostcontrolModule implements Module<CostcontrolState, RootState>{
  namespaced = true
  state = State
  getters = {}
  mutations = mutations
  actions = actions
}
