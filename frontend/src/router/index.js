import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import Dashboard from '@/components/Dashboard/Dashboard'
import Statistics from '@/components/Dashboard/Statistics/Statistics'
import YearStatistics from '@/components/Dashboard/Statistics/YearStatistics'
import Creation from '@/components/Dashboard/Creation/Creation'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/login/'
    },
    {
      path: '/login',
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
          path: 'year-statistics',
          name: 'yearStatistics',
          component: YearStatistics
        },
        {
          path: 'creation',
          name: 'creation',
          component: Creation
        }
      ]
    }
  ]
})
