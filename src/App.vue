<template>
  <b-container id="app" class="h-100">
    <router-view></router-view>
  </b-container>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="scss">
@import 'bootstrap';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
html,
body {
    height: 100%;
}
</style>
