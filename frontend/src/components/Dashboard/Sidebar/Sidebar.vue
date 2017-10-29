<template>
  <div class="d-flex flex-column bg-primary inner-h-100 text-secondary sidebar">
    <nav-link
      v-for="nav in navs"
      :key="nav.text"
      :to="nav.to"
      :name="nav.name"
      :text="nav.text"
      :icon="nav.icon"
    />
  </div>
</template>

<script>
import NavLink from './NavLink'

export default {
  name: 'sidebar',
  components: { NavLink },
  data: () => ({
    navs: [
      { to: { name: 'dashboard' }, icon: 'dashboard', text: 'Main' },
      { to: { name: 'statistics' }, icon: 'pie-chart', text: 'Statistics' },
      { to: { name: 'creation' }, icon: 'edit', text: 'Create' }
    ]
  })
}
</script>

<style scoped lang="scss">
.sidebar {
  border-top: 1px solid black;
}
</style>

