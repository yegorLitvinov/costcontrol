<template>
  <b-card :header="header" header-tag="header">
    <b-form @submit.prevent="onSubmit">
      <b-form-group
        label="Amount:"
        description="In rubles"
      >
        <b-form-input
          v-model="record.amount"
          :state="errors.amount.length ? false : null"
          type="number"
          placeholder="Enter amount"
        ></b-form-input>
        <b-form-feedback v-for="error in errors.amount" :key="error">
          {{error}}
        </b-form-feedback>
      </b-form-group>

      <b-form-group label="Comment:">
        <b-form-input
          v-model="record.comment"
          :state="errors.comment.length ? false : null"
          placeholder="Enter comment"
        ></b-form-input>
        <b-form-feedback v-for="error in errors.comment" :key="error">
          {{error}}
        </b-form-feedback>
      </b-form-group>

      <b-form-group label="Category:">
        <b-form-select
          v-model="record.category"
          :state="errors.category.length ? false : null"
          :options="categories"
        ></b-form-select>
        <b-form-feedback v-for="error in errors.category" :key="error">
          {{error}}
        </b-form-feedback>
      </b-form-group>

      <b-button type="submit" variant="primary">Create</b-button>
    </b-form>
  </b-card>
</template>

<script>
import Vuex from 'vuex'

const defaultRecord = {
  amount: '',
  comment: '',
  category: null
}
const defaultErrors = {
  amount: [],
  comment: [],
  category: []
}

export default {
  name: 'balance-record-form',
  props: ['addRecord', 'categories', 'header'],
  data: () => ({
    record: { ...defaultRecord },
    errors: { ...defaultErrors }
  }),
  computed: Vuex.mapState({
    userId: state => state.user.id
  }),
  methods: {
    onSubmit(evt) {
      this.addRecord({ ...this.record, user: this.userId })
        .then(response => {
          this.record = { ...this.record, ...defaultRecord }
          this.errors = { ...this.errors, ...defaultErrors }
        })
        .catch(error => {
          this.errors = { ...this.errors, ...defaultErrors, ...error.data }
        })
    }
  }
}
</script>
