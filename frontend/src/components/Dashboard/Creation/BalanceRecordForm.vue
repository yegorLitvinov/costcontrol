<template>
  <b-card :header="header" header-tag="header">
    <b-form @submit.prevent="onSubmit">
      <b-form-group
        label="Amount:"
        description="In rubles"
      >
        <b-input
          v-model="record.amount"
          :state="errors.amount.length ? false : null"
          type="number"
          placeholder="Enter amount"
        ></b-input>
        <b-form-invalid-feedback v-for="error in errors.amount" :key="error">
          {{error}}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="Comment:">
        <b-input
          v-model="record.comment"
          :state="errors.comment.length ? false : null"
          placeholder="Enter comment"
        ></b-input>
        <b-form-invalid-feedback v-for="error in errors.comment" :key="error">
          {{error}}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="Category:">
        <b-select
          v-model="record.category"
          :state="errors.category.length ? false : null"
          :options="[{ text: 'Select Category', value: null}].concat(categories)"
        ></b-select>
        <b-form-invalid-feedback v-for="error in errors.category" :key="error">
          {{error}}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-button
        type="submit"
        variant="primary"
        :disabled="submitting"
        :style="{width: '100px'}"
      >
        <three-bounce v-if="submitting" />
        <span v-else>Create</span>
      </b-button>
    </b-form>
  </b-card>
</template>

<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import { mapState } from 'vuex'
import { AxiosError } from 'axios'

import { RootState, Category } from '../../../types'

const defaultRecord = {
  amount: '',
  comment: '',
  category: null,
}
const defaultErrors = {
  amount: [],
  comment: [],
  category: [],
}

export default Vue.extend({
  name: 'balance-record-form',
  props: {
    addRecord: {
      type: Function,
      required: true,
    },
    categories: {
      type: Array as () => Category[],
      required: true,
    },
    header: String,
  },
  data: () => ({
    submitting: false,
    record: { ...defaultRecord },
    errors: { ...defaultErrors },
  }),
  computed: mapState({
    userId: (state: RootState) => state.accounts.user.id,
  }),
  methods: {
    onSubmit(): void {
      this.submitting = true
      this.addRecord({ ...this.record, user: this.userId })
        .then(() => {
          this.record = { ...this.record, ...defaultRecord }
          this.errors = { ...this.errors, ...defaultErrors }
          this.submitting = false
        })
        .catch((error: AxiosError) => {
          const errorResponseData = error.response ? error.response.data : {}
          this.errors = { ...this.errors, ...defaultErrors, ...errorResponseData }
          this.submitting = false
        })
    },
  },
})
</script>
