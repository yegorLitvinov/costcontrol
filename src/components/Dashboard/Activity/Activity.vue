<template>
  <div class="bg-light inner-h-100">
    <p class="text-uppercase p-4">Latest Activity</p>
    <activity-item v-for="(m, _, index) in messages" :key="index" :text="m"></activity-item>
  </div>
</template>

<script>
import ActivityItem from './Item'

export default {
  name: 'activity',
  data: () => ({
    messages: ['One dsmaffs fk dsjf jsdafj lsjdf jalsdj jsdk sjafdj fajkl jslfjkl jdklaf jls', 'two', 'three']
  }),
  components: { ActivityItem }
}
</script>

<style scoped lang="scss">

</style>
