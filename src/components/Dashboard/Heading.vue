<template>
  <div class="header bg-primary w-100 text-white">
    <div class="d-flex m-0 p-0 align-items-center h-100 d-flex justify-content-between">
      <div class="text-uppercase">Dashboard</div>

      <div class="d-flex justify-content-end h-100">
        <div class="nav-link d-flex align-items-center" @click="logout"><div class="m-auto icon-wrapper"><icon name="sign-out" scale="1.5" /></div></div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'heading',
  methods: {
    logout() {
      this.$http.post('accounts/logout/')
        .then(response => {
          Vue.http.headers.common['Authorization'] = undefined
          sessionStorage.removeItem('token')
          this.$router.push('/')
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>

<style scoped lang="scss">
@import "../../styles/constants";

.header {
  height: $heading-height;
}

.nav-link {
  width: $heading-height;
  height: 100%;
  color: white;
  background-color: $warning;
  border-bottom: 2px solid lighten($warning, 10%);
  cursor: pointer;

  .icon-wrapper {
    max-width: 30px;
  }
}
</style>
