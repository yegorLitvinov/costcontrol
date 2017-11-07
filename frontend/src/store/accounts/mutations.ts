import Vue from 'vue'
import { MutationTree } from 'vuex'
import axios from 'axios'

import { RootState, AccountsState, BalanceRecord, User } from '../../types'

export const setUser = (state: AccountsState, user: User) => {
  axios.defaults.headers.common['Authorization'] = `Token ${user.token}`
  sessionStorage.setItem('token', user.token || '')
  sessionStorage.setItem('userId', String(user.id || ''))

  state.user = { ...state.user, ...user }
}

export const clearUser = (state: AccountsState) => {
  delete axios.defaults.headers.common.Authorization;
  sessionStorage.removeItem('token')
  sessionStorage.removeItem('userId')

  state.user = {
    ...state.user,
    id: -1,
    first_name: '',
    last_name: '',
    email: '',
    token: ''
  }
}

export default <MutationTree<AccountsState>> {
  setUser, clearUser
}
