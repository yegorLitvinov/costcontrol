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
    .post(opts.type + '/', opts.formData)
    .then(function(response) {
      return response.json()
    })
    .then(function(record) {
      record.type = opts.type
      context.commit('appendRecord', record)
      return Promise.resolve(record)
    })
}

export const fetchStatistics = (context, date) => {
  context.commit('changeDate', date)
  var year = date.getFullYear()
  var month = date.getMonth() + 1
  var url = 'statistic/{0}/?year={1}&month={2}'
  context.dispatch('get', {
    what: url.format('spending', year, month),
    where: 'spendingStatistics'
  })
  context.dispatch('get', {
    what: url.format('proceed', year, month),
    where: 'proceedStatistics'
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
      Vue.http.headers.common['Authorization'] = `Token ${data.token}`
      context.commit('setUser', { ...data.user, token: data.token })
      sessionStorage.setItem('token', data.token)
      sessionStorage.setItem('userId', data.user.id)
      router.push('/dashboard/')
      return data.user
    })
}

export const logout = (context) => {
  Vue.http.post('accounts/logout/')
  .then(response => {
    Vue.http.headers.common['Authorization'] = undefined
    context.commit('clearUser')
    sessionStorage.removeItem('token')
    sessionStorage.removeItem('userId')
    router.push('/')
  })
  .catch(error => {
    console.error(error)
  })
}
