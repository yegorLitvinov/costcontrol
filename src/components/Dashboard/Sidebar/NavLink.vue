<template>
  <router-link :to="to" :exact="true" tag="div" class="p-2 sidebar-nav-link d-flex align-items-center">
    <span><icon :name="icon" /></span>
    <a class="text-uppercase pl-2 w-100">{{text}}</a>
  </router-link>
</template>

<script>
export default {
  name: 'nav-link',
  props: ['to', 'text', 'icon']
}
</script>

<style scoped lang="scss">
@import '../../../styles/constants';

.sidebar-nav-link {
  a {
    color: $secondary;
    text-decoration: none;
  }

  &:hover, &.router-link-active {
    background-color: rgba($light, 0.1);

    a, svg {
      color: white;
    }
  }

}
</style>

