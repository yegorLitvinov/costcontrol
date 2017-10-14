<template>
  <select :name="name" class="round-select p-1 mx-2">
    <option value="">{{name}}</option>
    <option v-for="option in options" :key="option[0]" :value="option[0]">{{option[1]}}</option>
  </select>
</template>

<script>
export default {
  name: 'round-select',
  props: ['name', 'options']
}
</script>

<style scoped lang="scss">
@import '../../styles/constants';

.round-select {
  background-color: $warning;
  color: white;
  border-radius: 5px 10px;
  border: none;
}
</style>
