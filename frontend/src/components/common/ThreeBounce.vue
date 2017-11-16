<template>
  <div class="sk-three-bounce">
    <div class="sk-child sk-bounce1"></div>
    <div class="sk-child sk-bounce2"></div>
    <div class="sk-child sk-bounce3"></div>
  </div>
</template>

<script>
export default {
  name: 'three-bounce'
}
</script>

<style lang="scss">
$spinkit-spinner-margin: 0px auto;
$spinkit-size: 20px;
$spinkit-spinner-color: white;

@import '~spinkit/scss/_variables.scss';
@import '~spinkit/scss/spinners/7-three-bounce.scss';
</style>
