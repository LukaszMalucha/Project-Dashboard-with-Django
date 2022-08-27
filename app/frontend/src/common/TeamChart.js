import { Doughnut, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Doughnut,
  mixins: [reactiveProp],
  data(){
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false,
        title: {
          fontSize: 16,
          fontColor: 'black',
          display: true,
          text: "Team Personalities"
        },
        scales: {
          xAxes: [{
              gridLines: {
                  color: "rgba(0, 0, 0, 0)",
                  zeroLineColor: "rgba(0, 0, 0, 0)",
              },
              ticks: {
                fontSize: 10,
                suggestedMin: 0,
                beginAtZero: true,
                fontColor: "rgba(0, 0, 0, 0)",
              }
          }],
          yAxes: [{
              gridLines: {
                  color: "rgba(0, 0, 0, 0)",
                  zeroLineColor: "rgba(0, 0, 0, 0)",
              },
              ticks: {
                stepSize: 10,
                suggestedMin: 0,
                beginAtZero: true,
                fontColor: "rgba(0, 0, 0, 0)",
              }
          }],

        },
        tooltips: {
          enabled: true,
          callbacks: {
            label: function(tooltipItem,data) {
              return data['datasets'][0]['data'][tooltipItem['index']] + " team member";
            },
          }
        }
      }
    }
  },
  mounted () {
    this.renderChart(
      this.chartData,
      this.options
      )
  }
}