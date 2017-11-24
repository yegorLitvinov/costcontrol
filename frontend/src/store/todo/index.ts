import Vue from 'vue'
import { Module } from 'vuex'

import mutations from './mutations'
import actions from './actions'
import { TodoState, RootState } from '../../types'

const State: TodoState = {
  entities: {},
  orderedIds: []
}

export default class CostcontrolModule implements Module<TodoState, RootState>{
  namespaced = true
  state = State
  getters = {}
  mutations = mutations
  actions = actions
}
