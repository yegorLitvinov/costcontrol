import Vue from 'vue'
import { MutationTree } from 'vuex'
import axios from 'axios'

import { RootState, BalanceRecord, User } from '../types'

export const insert = (state: RootState, payload: {what: string, where: string}) => {
  // @ts-ignore
  state[payload.where] = payload.what
}

// Append record to history
export const appendRecord = (state: RootState, record: BalanceRecord) => {
  state.history.unshift(record)
}

export const setUser = (state: RootState, user: User) => {
  axios.defaults.headers.common['Authorization'] = `Token ${user.token}`
  sessionStorage.setItem('token', user.token || '')
  sessionStorage.setItem('userId', String(user.id || ''))

  state.user = { ...state.user, ...user }
}

export const clearUser = (state: RootState) => {
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

export default <MutationTree<RootState>> {
  insert, appendRecord, setUser, clearUser
}
