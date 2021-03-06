// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios, { AxiosError } from 'axios'

import App from './App.vue'
import router from './router'
import './use'
import store from './store'
import ThreeBounce from './components/common/ThreeBounce.vue'

Vue.config.productionTip = false

axios.defaults.headers.common = {
  ...axios.defaults.headers.common,
  'X-Requested-With': 'XMLHttpRequest',
};
axios.defaults.baseURL = '/api/';
axios.interceptors.response.use(
  response => {
    return response;
  },
  (error: AxiosError) => {
    if (error.response && error.response.status === 401) {
      store.commit('accounts/clearUser')
    }
    return Promise.reject(error);
  }
);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})


// Register global components
Vue.component('three-bounce', ThreeBounce)
