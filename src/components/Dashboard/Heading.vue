<template>
  <div class="header bg-primary w-100 text-white">
    <b-row class="m-0 p-0 align-items-center h-100">
      <b-col cols="12 text-uppercase">
        Dashboard
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'heading'
}
</script>

<style scoped lang="scss">
@import "../../styles/constants";

.header {
  height: $heading-height;
}
</style>
