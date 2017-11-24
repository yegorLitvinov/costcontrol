import Vue from 'vue'
import { MutationTree } from 'vuex'
import axios from 'axios'
import keyBy from 'lodash-es/keyBy'
import findIndex from 'lodash-es/findIndex'
import remove from 'lodash-es/remove'

import { TodoState, Todo } from '../../types'

const getTodos = (state: TodoState, todos: Todo[]) => {
  state.entities = keyBy(todos, (todo: Todo) => todo.id)
  state.orderedIds = todos.map((todo) => todo.id)
}

const patchTodo = (state: TodoState, todo: Todo) => {
  const orderedIds: number[] = [...state.orderedIds]

  remove(orderedIds, (id) => id === todo.id)
  if (todo.completed === true) {
    const firstCompletedIdex = findIndex(orderedIds, (id) => {
      return state.entities[id].completed == true
    })
    if (firstCompletedIdex === -1) {
      orderedIds.push(todo.id)
    } else {
      orderedIds.splice(firstCompletedIdex, 0, todo.id)
    }
  } else {
    orderedIds.unshift(todo.id)
  }

  state.entities = { ...state.entities, [todo.id]: todo}
  state.orderedIds = orderedIds
}

const addTodo = (state: TodoState, todo: Todo) => {
  state.entities = { ...state.entities, [todo.id]: todo}
  state.orderedIds.unshift(todo.id)
}

export default <MutationTree<TodoState>> {
  getTodos, patchTodo, addTodo
}
