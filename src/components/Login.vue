<template>
  <div class="d-flex m-auto h-100 align-items-center login">
    <b-form @submit.prevent="onSubmit" class="w-100 m-3">
      <b-form-group label="Email address:" :feedback="error" :state="state">
        <b-form-input name="email" v-model="form.email" :state="state" required placeholder="Enter email"></b-form-input>
      </b-form-group>
      <b-form-group label="Password:" :feedback="error" :state="state">
        <b-form-input type="password" v-model="form.password" :state="state" required placeholder="Enter password"></b-form-input>
      </b-form-group>
      <b-form-group>
        <!-- <b-form-checkbox v-model="form.checked">
          I'm agree with my personal data processing
        </b-form-checkbox> -->
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'login',
  data: () => ({
    form: {
      email: '',
      password: ''
    },
    error: ''
  }),
  computed: {
    state() {
      return this.error ? 'invalid' : ''
    }
  },
  methods: {
    onSubmit() {
      this.$http.post(
        'accounts/login/',
        '',
        { headers: { 'Authorization': 'Basic ' + btoa(`${this.form.email}:${this.form.password}`) } }
      )
        .then(response => {
          return response.json()
        })
        .then(data => {
          Vue.http.headers.common['Authorization'] = `Token ${data.token}`
          sessionStorage.setItem('token', data.token)
          this.error = ''
          this.$router.push('/dashboard')
        })
        .catch(error => {
          this.error = error.data.detail
        })
    }
  }
}
</script>

<style scoped lang="scss">
.login {
  max-width: 400px;
}
</style>
