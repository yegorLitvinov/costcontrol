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
    <todo-item v-for="(todo, _, index) in todos" :key="todo.id || index" :todo="todo" />
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
    todos: (state: RootState) => values(state.todo.todos),
  }),
  methods: {
    addTodo() {
      this.$store.dispatch('todo/addTodo', {
        text: 'Write todo here',
        completed: false,
      })
    }
  },
  mounted() {
    this.$store.dispatch('todo/getTodos')
  }
})
</script>
