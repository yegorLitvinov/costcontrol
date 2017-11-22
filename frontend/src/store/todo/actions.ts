import Vue from 'vue'
import { ActionContext, ActionTree } from 'vuex'
import axios from 'axios'

import router from '../../router'
import { RootState, TodoState, Todo } from '../../types'

export function getTodos(context: ActionContext<TodoState, RootState>) {
    return axios
      .get<Todo[]>('/todo/todo/')
      .then(function (response) {
        return response.data
      })
      .then(function (data) {
        context.commit('getTodos', data)
        return Promise.resolve(data)
      })
}

export function patchTodo(context: ActionContext<TodoState, RootState>, todo: Todo)
{
  return axios
    .patch<Todo>(`/todo/todo/${todo.id}/`, todo)
    .then(function (response) {
      return response.data
    })
    .then(function (todo) {
      context.commit('patchTodo', todo)
      return Promise.resolve(todo)
    })
}

export function addTodo(context: ActionContext<TodoState, RootState>, todo: Todo)
{
  return axios
    .post<Todo>(`/todo/todo/`, todo)
    .then(function (response) {
      return response.data
    })
    .then(function (todo) {
      context.commit('addTodo', todo)
      return Promise.resolve(todo)
    })
}

export default <ActionTree<TodoState, RootState>>{
    getTodos, patchTodo, addTodo
}
