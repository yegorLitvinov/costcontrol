<template>
  <div class="pl-4 item-wrapper">
    <div class="activity-item">
      {{ `${record.sign} ${record.amount}\u20bd (${record.created_at}) ${record.comment} (${record.category__name})` }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'activity-item',
  props: ['record']
}
</script>

<style scoped lang="scss">
@import "../../../styles/constants";

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
    content: "o";
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
  &:hover {
    background-color: rgba($info, 0.8);
    color: white;
  }
}
</style>
