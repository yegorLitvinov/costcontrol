import Vue from 'vue'
import { ActionContext, ActionTree } from 'vuex'
import axios from 'axios'

import router from '../../router'
import { RootState, AccountsState, BalanceRecord, CategoryKind, User } from '../../types'

export function login (context: ActionContext<AccountsState, RootState>, loginData: { email: string, password: string }) {
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

export function logout (context: ActionContext<AccountsState, RootState>) {
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

export default <ActionTree<AccountsState, RootState>> {
  login, logout
}
