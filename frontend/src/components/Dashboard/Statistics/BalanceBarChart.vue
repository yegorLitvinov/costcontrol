<script>
import { Bar, mixins } from 'vue-chartjs'

export default {
  extends: Bar,
  mixins: [mixins.reactiveProp],
  props: ['data', 'options'],
  mounted() {
    const options = {
      maintainAspectRatio: false,
      legend: {
        position: 'bottom',
      },
      responsive: true,
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
    }
    this.renderChart(this.chartData, options)
  },
}
</script>
