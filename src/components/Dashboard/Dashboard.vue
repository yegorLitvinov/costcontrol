<template>
  <div class="h-md-100 w-100 d-flex flex-column">
    <heading></heading>
    <div class="h-md-100 row m-0">
      <b-col cols="12" md="2" class="h-md-100 m-0 p-0">
        <sidebar />
      </b-col>
      <b-col cols="12" md="7" class="h-md-100 bg-white m-0 p-2 p-md-3">
        <transition name="fade">
          <router-view></router-view>
        </transition>
      </b-col>
      <b-col cols="12" md="3" class="h-md-100 m-0 p-0">
        <activity></activity>
      </b-col>
    </div>
  </div>
</template>

<script>
import Heading from './Heading'
import Sidebar from './Sidebar/Sidebar'
import Activity from './Activity/Activity'

export default {
  name: 'dashboard',
  components: { Heading, Sidebar, Activity }
}
</script>
