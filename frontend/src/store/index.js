import Vue from 'vue'
import Vuex from 'vuex'

import * as mutations from './mutations'
import * as actions from './actions'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      id: '',
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
