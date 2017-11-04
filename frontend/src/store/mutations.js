import Vue from 'vue'

export const insert = (state, opts) => {
  state[opts.where] = opts.what
}

export const changeDate = (state, date) => {
  state['date'] = date
}

// Append record to history
export const appendRecord = (state, record) => {
  const recordCategory = state[record.type + 'Categories'].find(
    category => category.id === record.category
  )
  record.category__name = recordCategory.name
  state.history.unshift(record)
}

export const setUser = (state, user) => {
  Vue.http.headers.common['Authorization'] = `Token ${user.token}`
  sessionStorage.setItem('token', user.token)
  sessionStorage.setItem('userId', user.id)

  state.user = { ...state.user, ...user }
}

export const clearUser = (state) => {
  Vue.http.headers.common['Authorization'] = undefined
  sessionStorage.removeItem('token')
  sessionStorage.removeItem('userId')

  state.user = {
    ...state.user,
    id: '',
    first_name: '',
    last_name: '',
    email: '',
    token: ''
  }
}
