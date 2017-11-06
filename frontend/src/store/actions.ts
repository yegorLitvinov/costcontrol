import Vue from 'vue'
import { ActionContext, ActionTree } from 'vuex'
import axios from 'axios'

import router from '../router'
import { RootState, BalanceRecord, CategoryKind, User } from '../types'

// Get 'what' from api and put it into store's 'where'
export function get<D = {}>(context: ActionContext<RootState, any>, payload: { what: string, where: string }) {
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

export const addRecord = (context: ActionContext<RootState, any>, record: BalanceRecord) => {
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

export const fetchStatistics = (context: ActionContext<RootState, any>, payload: { year: number, month: number }) => {
  [CategoryKind.Proceed, CategoryKind.Spending].forEach(kind => {
    context.dispatch('get', {
      what: `category/statistic/?year=${payload.year}&month=${payload.month}&kind=${kind}`,
      where: `${kind}Statistics`
    })
  })
}

export const login = (context: ActionContext<RootState, any>, loginData: { email: string, password: string }) => {
  return axios.post<{ user: User, token: string }>(
    'accounts/login/',
    '',
    { headers: { 'Authorization': 'Basic ' + btoa(`${loginData.email}:${loginData.password}`) } }
  )
    .then(response => {
      return response.data
    })
    .then(data => {
      context.commit('setUser', { ...data.user, token: data.token })
      router.push('/dashboard/')
      return data
    })
}

export const logout = (context: ActionContext<RootState, any>) => {
  return axios
    .post<{}>('accounts/logout/')
    .then(response => {
      context.commit('clearUser')
      router.push('/')
    })
    .catch(error => {
      console.error(error)
    })
}

export default <ActionTree<RootState, {}>> {
  get, addRecord, fetchStatistics, login, logout
}
