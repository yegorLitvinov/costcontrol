import Vue from 'vue'
// Async actions (redux thunk middleware actions)

// Get 'what' from api and put it into store's 'where'
export const get = (context, opts) => {
  Vue.http
    .get(opts.what)
    .then(function(response) {
      return response.json()
    })
    .then(function(json) {
      context.commit('insert', { what: json, where: opts.where })
      return Promise.resolve()
    })
    .catch(function(error) {
      console.error(error)
    })
}

export const addRecord = (context, opts) => {
  return Vue.http
    .post('/api/' + opts.type + '/', opts.formData)
    .then(function(response) {
      return response.json()
    })
    .then(function(record) {
      record.type = opts.type
      context.commit('appendRecord', record)
      return Promise.resolve()
    })
    .catch(function(error) {
      console.error(error)
    })
}

export const fetchStatistics = (context, date) => {
  context.commit('changeDate', date)
  var year = date.getFullYear()
  var month = date.getMonth() + 1
  var url = '/api/statistic/{0}/?year={1}&month={2}'
  context.dispatch('get', {
    what: url.format('spending', year, month),
    where: 'spendingStatistics'
  })
  context.dispatch('get', {
    what: url.format('proceed', year, month),
    where: 'proceedStatistics'
  })
}
