<template>
  <div class="bg-primary inner-h-100 text-white sidebar">
    <router-link :to="{name: 'dashboard'}" :class="text-uppercase">Main</router-link>
    <router-link :to="{name: 'statistics'}" :class="text-uppercase">Statistics</router-link>
    <router-link :to="{name: 'creation'}" :class="text-uppercase">Create</router-link>
  </div>
</template>

<script>
export default {
  name: 'sidebar'
}
</script>

<style scoped lang="scss">
.sidebar {
  border-top: 1px solid black;
}
</style>
