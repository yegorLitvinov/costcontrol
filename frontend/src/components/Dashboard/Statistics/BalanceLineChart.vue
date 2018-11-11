<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import { Line, mixins } from 'vue-chartjs'

export default Vue.extend({
  extends: Line,
  props: ['chartData', 'options'],
  mixins: [mixins.reactiveProp],
  mounted() {
    ;(this as any).renderChart(this.chartData, {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
          },
        ],
      },
      ...this.options,
    })
  },
})
</script>
