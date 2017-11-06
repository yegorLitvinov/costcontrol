import Vue from 'vue'
import Vuex from 'vuex'

import mutations from './mutations'
import actions from './actions'
import { RootState } from '../types'

Vue.use(Vuex)

export default new Vuex.Store<RootState>({
  state: {
    user: {
      id: 0,
      email: '',
      first_name: '',
      last_name: '',
      token: ''
    },
    history: [],
    spendingCategories: [],
    proceedCategories: [],
    spendingStatistics: [],
    proceedStatistics: [],
    filledMonthes: {}
  },

  // Build something from state
  getters: {},

  mutations,
  actions
})
