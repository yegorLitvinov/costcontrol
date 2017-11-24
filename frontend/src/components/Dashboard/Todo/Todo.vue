<template>
  <div>
    <b-button
      @click="addTodo"
      variant="primary"
      :style="{width: '100px'}"
      class="mb-3"
    >
      <span>Create</span>
    </b-button>
    <transition-group name="todos">
      <todo-item v-for="todo in todos" :key="todo.id" :todo="todo" />
    </transition-group>
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import { mapState } from 'vuex'
import values from 'lodash-es/values'

import { RootState } from '../../../types'
import TodoItem from './TodoItem.vue'

export default Vue.extend({
  components: { TodoItem },
  data: () => ({}),
  computed: mapState({
    todos: (state: RootState) => state.todo.orderedIds.map((id) => {
      const todo = state.todo.entities[id]
      return {...todo}
    }),
  }),
  methods: {
    addTodo() {
      this.$store.dispatch('todo/addTodo', {
        text: '',
        completed: false,
      })
    }
  },
  mounted() {
    this.$store.dispatch('todo/getTodos')
  }
})
</script>

<style lang="scss">
.todos-move {
  transition: transform .5s;
}
</style>
