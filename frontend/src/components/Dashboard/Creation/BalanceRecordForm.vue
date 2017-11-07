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
          :options="[{ text: 'Select Category', value: null}].concat(categories)"
        ></b-form-select>
        <b-form-feedback v-for="error in errors.category" :key="error">
          {{error}}
        </b-form-feedback>
      </b-form-group>

      <b-button type="submit" variant="primary">Create</b-button>
    </b-form>
  </b-card>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapState } from 'vuex'
// eslint-disable-next-line no-unused-vars
import { AxiosError } from 'axios'

// eslint-disable-next-line no-unused-vars
import { RootState } from '../../../types'

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

export default Vue.extend({
  name: 'balance-record-form',
  props: ['addRecord', 'categories', 'header'],
  data: () => ({
    record: { ...defaultRecord },
    errors: { ...defaultErrors }
  }),
  computed: mapState({
    userId: (state: RootState) => state.accounts.user.id
  }),
  methods: {
    onSubmit(): void {
      this.addRecord({ ...this.record, user: this.userId })
        .then(() => {
          this.record = { ...this.record, ...defaultRecord }
          this.errors = { ...this.errors, ...defaultErrors }
        })
        .catch((error: AxiosError) => {
          const errorResponseData = error.response ? error.response.data : {}
          this.errors = { ...this.errors, ...defaultErrors, ...errorResponseData }
        })
    }
  }
})
</script>
