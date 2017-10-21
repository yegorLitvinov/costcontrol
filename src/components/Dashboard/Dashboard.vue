<template>
  <div class="w-100 d-flex flex-column">
    <heading></heading>
    <div class="row m-0">
      <b-col cols="12" md="2" class="m-0 p-0">
        <sidebar />
      </b-col>
      <b-col cols="12" md="7" class="bg-white m-0 p-2 p-md-3">
        <transition name="fade">
          <router-view></router-view>
        </transition>
      </b-col>
      <b-col cols="12" md="3" class="m-0 p-0">
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
  components: { Heading, Sidebar, Activity },
  mounted() {
    if (!sessionStorage.getItem('token')) {
      this.$router.push('/')
    }
  }
}
</script>
