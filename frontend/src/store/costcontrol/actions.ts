import Vue from 'vue'
import { ActionContext, ActionTree } from 'vuex'
import axios from 'axios'

import router from '../../router'
import { RootState, CostcontrolState, BalanceRecord, CategoryKind, PaginatedResults } from '../../types'

// Get 'what' from api and put it into store's 'where'
export function get<D = {}>(context: ActionContext<CostcontrolState, RootState>, payload: { what: string, where: string, asIs?: boolean }) {
  return axios
    .get<D>(payload.what)
    .then(function (response) {
      return response.data
    })
    .then(function (data) {
      if (payload.asIs) {
        context.commit('insertAsIs', { what: data, where: payload.where })
      } else {
        context.commit('insert', { what: data, where: payload.where })
      }
      return Promise.resolve(data)
    })
}

function getHistory(context: ActionContext<CostcontrolState, RootState>, payload?: {page?: number}) {
  return axios.get<PaginatedResults<BalanceRecord>>('/costcontrol/history/', {params: {page: payload && payload.page}}).then(function(response) {
    context.commit('appendHistory', response.data.results)
    return Promise.resolve(response.data)
  })
}

export function getFilledMonthes(context: ActionContext<CostcontrolState, RootState>) {
  return axios
    .get('costcontrol/filled-months/')
    .then(function (response) {
      return response.data
    })
    .then(function (filledMonthes) {
      context.commit('insertFilledMonthes', filledMonthes)
      return Promise.resolve(filledMonthes)
    })
}


export function addRecord(context: ActionContext<CostcontrolState, RootState>, record: BalanceRecord) {
  return axios
    .post<BalanceRecord>('costcontrol/balance-record/', record)
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
      what: `costcontrol/categories/statistics/?year=${payload.year}&month=${payload.month}&kind=${kind}`,
      where: `${kind}Statistics`,
      asIs: true
    })
  })
}

export function fetchYearStatistics(context: ActionContext<CostcontrolState, RootState>, payload: { year: number }) {
  context.dispatch('get', {
    what: `costcontrol/year-statistics/?year=${payload.year}`,
    where: `yearStatistics`,
    asIs: true
  })
}

export default <ActionTree<CostcontrolState, RootState>>{
  get, getHistory, getFilledMonthes, addRecord, fetchStatistics, fetchYearStatistics,
}
