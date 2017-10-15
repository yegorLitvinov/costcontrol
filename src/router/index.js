import Vue from 'vue'
import Router from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'

import Login from '@/components/Login'
import Dashboard from '@/components/Dashboard/Dashboard'
import Statistics from '@/components/Dashboard/Statistics'

Vue.use(Router)
Vue.use(BootstrapVue)
Vue.component('icon', Icon)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      children: [
        {
          path: 'statistics',
          name: 'statistics',
          component: Statistics
        },
        {
          path: 'creation',
          name: 'creation',
          component: Statistics
        }
      ]
    }
  ]
})
