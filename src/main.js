// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import BootstrapVue from 'bootstrap-vue'
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'

import App from './App'
import router from './router'

Vue.use(BootstrapVue)
Vue.use(VueResource)
Vue.component('icon', Icon)

import store from './store'

Vue.config.productionTip = false
Vue.http.options.root = '/api/'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
