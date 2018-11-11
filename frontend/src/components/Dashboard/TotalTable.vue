<template>
  <b-row>
    <b-col sm="12" md="6">
      <b-alert v-if="data.accumulated" show :variant="data.accumulated > 0 ? 'success' : 'danger' ">{{ accumulated }}</b-alert>
    </b-col>
  </b-row>
</template>

<script>
import axios from 'axios'

export default {
  name: 'total-table',
  mounted() {
    this.getTotal()
  },
  data() {
    return {
      data: {},
    }
  },
  computed: {
    accumulated() {
      if (!this.data.accumulated) {
        return
      }
      let text = 'Your procced: '
      if (this.data.accumulated <= 0) {
        text = 'Your spending: '
      }
      return text + this.data.accumulated.toLocaleString() + ' ₽'
    },
  },
  methods: {
    getTotal() {
      axios.get('/costcontrol/total/').then(response => {
        this.data = response.data
      })
    },
  },
}
</script>
