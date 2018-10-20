<template>
  <div class="d-flex m-auto h-100 align-items-center login">
    <b-form @submit.prevent="onSubmit" class="w-100 m-3">

      <b-form-group label="Email address:" :feedback="error" :state="state">
        <b-form-input
          id="email"
          name="email"
          :state="state"
          required
          placeholder="Enter email"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="Password:" :feedback="error" :state="state">
        <b-form-input
          id="password"
          type="password"
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
    error: '',
  }),
  computed: {
    state(): string | null {
      return this.error ? 'invalid' : null
    },
  },
  methods: {
    getInputValue(id: string): string {
      const el = document.getElementById(id) as HTMLInputElement
      if (!el) {
        return ''
      }
      return el.value
    },
    onSubmit() {
      const email = this.getInputValue('email')
      const password = this.getInputValue('password')
      console.log(email)
      this.submitting = true
      return this.$store
        .dispatch('accounts/login', { email, password })
        .then(() => {
          this.error = ''
          this.submitting = false
        })
        .catch(this.handleError)
    },
    handleError(error: AxiosError) {
      if (error.response) {
        if (error.response.status === 401) {
          this.error = error.response.data.detail
        } else {
          this.error = error.response.statusText
        }
      } else {
        this.error = error.message
      }
      this.submitting = false
    },
  },
})
</script>

<style scoped lang="scss">
.login {
  max-width: 400px;
}
</style>
