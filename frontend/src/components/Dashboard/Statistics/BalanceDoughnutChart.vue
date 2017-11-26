<script>
import { Doughnut, mixins } from 'vue-chartjs'

export default {
  extends: Doughnut,
  mixins: [mixins.reactiveProp],
  mounted() {
    this.renderChart(this.chartData, {
      maintainAspectRatio: false,
      legend: {
        position: 'bottom'
      }
    })
  }
}
</script>
