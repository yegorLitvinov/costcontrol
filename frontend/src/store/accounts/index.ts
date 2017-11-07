import Vue from 'vue'
import { Module } from 'vuex'

import mutations from './mutations'
import actions from './actions'
import { AccountsState, RootState } from '../../types'

const State = {
  user: {
    id: -1,
    email: '',
    first_name: '',
    last_name: '',
    token: '',
  }
}

export default class AccountsModule implements Module<AccountsState, RootState> {
  namespaced = true
  state = State
  getters = {}
  mutations = mutations
  actions = actions
}
