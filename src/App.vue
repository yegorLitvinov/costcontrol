<template>
  <div id="app" class="container-fluid m-0 p-0 h-100">
  	<transition name="fade">
	    <router-view></router-view>
		</transition>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="scss">
@import 'styles/bootstrap';
@import 'styles/transitions';
@import url('https://fonts.googleapis.com/css?family=Rubik');

#app {
  font-family: 'Rubik', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
html,
body {
    height: 100%;
}
</style>
