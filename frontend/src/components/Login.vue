<template>
  <div class="d-flex m-auto h-100 align-items-center login">
    <b-form @submit.prevent="onSubmit" class="w-100 m-3">

      <b-form-group label="Email address:" :feedback="error" :state="state">
        <b-form-input
          name="email"
          v-model="form.email"
          :state="state"
          required
          placeholder="Enter email"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="Password:" :feedback="error" :state="state">
        <b-form-input
          type="password"
          v-model="form.password"
          :state="state"
          required
          placeholder="Enter password"
        >
        </b-form-input>
      </b-form-group>

      <b-button
        type="submit"
        variant="primary"
        :disabled="submitting"
        :style="{width: '100px'}"
      >
        <three-bounce v-if="submitting" />
        <span v-else>Login</span>
      </b-button>
    </b-form>
  </div>
</template>

<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import { AxiosError } from 'axios'

export default Vue.extend({
  name: 'login',
  data: () => ({
    submitting: false,
    form: {
      email: '',
      password: ''
    },
    error: ''
  }),
  computed: {
    state(): string {
      return this.error ? 'invalid' : ''
    }
  },
  methods: {
    onSubmit() {
      this.submitting = true
      return this.$store.dispatch('accounts/login', this.form)
        .then(() => {
          this.submitting = false
        })
        .catch((error: AxiosError) => {
          this.error = error.response ? error.response.data.detail : {}
          this.submitting = false
        })
    }
  }
})
</script>

<style scoped lang="scss">
.login {
  max-width: 400px;
}
</style>
