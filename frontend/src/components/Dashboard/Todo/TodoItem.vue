<template>
  <div class="d-flex align-items-center w-100 my-3">
    <b-form-checkbox v-model="completed" class="mb-0" />
    <span
      v-if="!focus"
      :class="{'text-secondary del': completed}"
      class="w-100"
      @click="onClick"
    >
      {{text}}
    </span>
    <input
      v-else
      type="text"
      v-model="text"
      @blur="onBlur"
      class="w-100"
      v-focus
      placeholder="Your todo text"
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
      focus: this.todo.text === '',
      completed: this.todo.completed,
      text: this.todo.text,
    }
  },
  methods: {
    onClick() {
      this.focus = true
    },
    onBlur() {
      this.focus = false
      this.$store.dispatch('todo/patchTodo', {
        id: this.todo.id,
        text: this.text
      })
    }
  },
  watch: {
    completed(completed: boolean): void {
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
