import Vue from 'vue'
import router from '../router'
// Async actions (redux thunk middleware actions)

// Get 'what' from api and put it into store's 'where'
export const get = (context, opts) => {
  return Vue.http
    .get(opts.what)
    .then(function(response) {
      return response.json()
    })
    .then(function(json) {
      context.commit('insert', { what: json, where: opts.where })
      return Promise.resolve(json)
    })
}

export const addRecord = (context, opts) => {
  return Vue.http
    .post('balance-record/', { ...opts.formData, kind: opts.type })
    .then(function(response) {
      return response.json()
    })
    .then(function(record) {
      record.type = opts.type
      context.commit('appendRecord', record)
      return Promise.resolve(record)
    })
}

export const fetchStatistics = (context, {year, month}) => {
  ['spending', 'proceed'].forEach(type => {
    context.dispatch('get', {
      what: `category/statistic/?year=${year}&month=${month}&kind=${type}`,
      where: `${type}Statistics`
    })
  })
}

export const login = (context, loginData) => {
  return Vue.http.post(
    'accounts/login/',
    '',
    { headers: { 'Authorization': 'Basic ' + btoa(`${loginData.email}:${loginData.password}`) } }
  )
    .then(response => {
      return response.json()
    })
    .then(data => {
      context.commit('setUser', { ...data.user, token: data.token })
      router.push('/dashboard/')
      return data.user
    })
}

export const logout = (context) => {
  Vue.http.post('accounts/logout/')
  .then(response => {
    context.commit('clearUser')
    router.push('/')
  })
  .catch(error => {
    console.error(error)
  })
}
