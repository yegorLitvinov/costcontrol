import Vue from 'vue'
import { MutationTree } from 'vuex'
import axios from 'axios'
import keyBy from 'lodash-es/keyBy'

import { TodoState, Todo } from '../../types'

const getTodos = (state: TodoState, todos: Todo[]) => {
  state.todos = keyBy(todos, (todo: Todo) => todo.id)
}

const patchTodo = (state: TodoState, todo: Todo) => {
  state.todos[todo.id || ''] = todo
}

const addTodo = (state: TodoState, todo: Todo) => {
  state.todos[todo.id || ''] = todo
}

export default <MutationTree<TodoState>> {
  getTodos, patchTodo, addTodo
}
