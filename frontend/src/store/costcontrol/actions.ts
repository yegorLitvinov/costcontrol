import Vue from 'vue'
import { ActionContext, ActionTree } from 'vuex'
import axios from 'axios'

import router from '../../router'
import { RootState, CostcontrolState, BalanceRecord, CategoryKind, User } from '../../types'

// Get 'what' from api and put it into store's 'where'
export function get<D = {}>(context: ActionContext<CostcontrolState, RootState>, payload: { what: string, where: string }) {
  return axios
    .get<D>(payload.what)
    .then(function (response) {
      return response.data
    })
    .then(function (data) {
      context.commit('insert', { what: data, where: payload.where })
      return Promise.resolve(data)
    })
}

export function addRecord(context: ActionContext<CostcontrolState, RootState>, record: BalanceRecord) {
  return axios
    .post<BalanceRecord>('balance-record/', record)
    .then(function (response) {
      return response.data
    })
    .then(function (record) {
      context.commit('appendRecord', record)
      return Promise.resolve(record)
    })
}

export function fetchStatistics(context: ActionContext<CostcontrolState, RootState>, payload: { year: number, month: number }) {
  [CategoryKind.Proceed, CategoryKind.Spending].forEach(kind => {
    context.dispatch('get', {
      what: `category/statistic/?year=${payload.year}&month=${payload.month}&kind=${kind}`,
      where: `${kind}Statistics`
    })
  })
}

export default <ActionTree<CostcontrolState, RootState>>{
  get, addRecord, fetchStatistics,
}
