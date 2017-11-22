<template>
  <div class="d-flex align-items-center w-100">
    <b-form-checkbox v-model="todo.completed" class="mb-0" />
    <span
      v-if="!focus"
      :class="{'text-secondary del': todo.completed}"
      class="w-100"
      @click="onClick"
    >
      {{todo.text}}
    </span>
    <input
      v-else
      type="text"
      v-model="todo.text"
      @blur="onBlur"
      class="w-100"
      v-focus
    >
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'

import { Todo } from '../../../types'


export default Vue.extend({
  name: 'todo-item',
  props: ['todo'],
  data: function() {
    return {
      focus: false,
    }
  },
  methods: {
    onClick() {
      this.focus = true
    },
    onBlur() {
      this.focus = false
      const { id, text } = this.todo;
      this.$store.dispatch('todo/patchTodo', {id, text})
    }
  },
  watch: {
    'todo.completed': function(completed: boolean): void {
      const { id } = this.todo;
      this.$store.dispatch('todo/patchTodo', {id, completed})
    }
  }
})
</script>

<style scoped lang="scss">
@import "../../../styles/constants";

.del {
  text-decoration: line-through;
}
</style>
