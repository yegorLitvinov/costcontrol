import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import Dashboard from '@/components/Dashboard/Dashboard'
import Statistics from '@/components/Dashboard/Statistics/Statistics'
import Creation from '@/components/Dashboard/Creation/Creation'
import Todo from '@/components/Dashboard/Todo/Todo'

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
          path: 'creation',
          name: 'creation',
          component: Creation
        },
        {
          path: 'todo',
          name: 'todo',
          component: Todo
        }
      ]
    }
  ]
})
