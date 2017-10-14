<template>
  <div class="px-4 item-wrapper" :class="{selected}">
    <div class="activity-item" :class="{selected}" @click.prevent="handleClick">
      {{ text }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'activity-item',
  props: ['text'],
  data: () => ({
    selected: false
  }),
  methods: {
    handleClick() {
      this.selected = !this.selected
    }
  }
}
</script>

<style scoped lang="scss">
@import '../../../styles/constants';

.activity-item {
  border-left: 2px solid lightgray;
  padding: 20px;

  &::before {
    position: relative;
    top: 10px;
    left: -31px;
    background-color: lightgray;
    color: lightgray;
    text-align: center;
    width: 20px;
    height: 20px;
    border-radius: 10px;
    content: 'o';
    display: inline-block;
  }

  &.selected {
    border-color: white;

    &::before {
      background-color: white;
      color: white;
    }
  }
}

.item-wrapper {
  &.selected {
    background-color: $info;
    color: white;
  }
}

</style>
