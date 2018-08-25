<script lang="ts" type="text/prs.typescript">
import Vue from 'vue'
import { Doughnut, mixins } from 'vue-chartjs'
import { CategoryStatistic, FilledMonthes, ChartData } from '../../../types'

export interface BalanceDoughnutChartItem {
  id: number
  name: string
  color: string
  total: number
}

export default Vue.extend({
  extends: Doughnut,
  props: {
    items: {
      type: Array as () => BalanceDoughnutChartItem[],
      required: true
    },
    onSectorClick: Function,
    label: String
  },
  computed: {
    chartData(): ChartData {
      return {
        labels: this.items.map(item => item.name),
        datasets: [
          {
            label: this.label,
            backgroundColor: this.items.map(item => item.color),
            data: this.items.map(item => item.total)
          }
        ]
      }
    }
  },
  watch: {
    chartData: mixins.reactiveData.watch.chartData
  },
  mounted() {
    (this as any).renderChart(this.chartData, {
      maintainAspectRatio: false,
      legend: {
        position: 'bottom'
      },
      onClick: this.onClick
    })
  },
  methods: {
    onClick(event: MouseEvent) {
      const elements = this.$data._chart.getElementsAtEvent(event)
      if (elements.length && this.onSectorClick) {
        const id = this.items[elements[0]._index].id
        this.onSectorClick(id)
      }
    }
  }
})
</script>
