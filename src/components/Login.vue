<template>
  <div class="d-flex m-auto h-100 align-items-center login">
    <b-form @submit.prevent="onSubmit" class="w-100 m-3">
      <b-form-group label="Email address:" description="We'll never share your email with anyone else.">
        <b-form-input name="email" v-model="form.email" required placeholder="Enter email"></b-form-input>
      </b-form-group>
      <b-form-group label="Password:">
        <b-form-input type="password" v-model="form.password" required placeholder="Enter password"></b-form-input>
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
export default {
  name: 'login',
  data: () => ({
    form: {
      email: '',
      password: ''
    }
  }),
  methods: {
    onSubmit() {
      this.$router.push('/dashboard')
    }
  }
}
</script>

<style scoped lang="scss">
.login {
  max-width: 400px;
}
</style>
