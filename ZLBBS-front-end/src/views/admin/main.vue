<template>
  <div style="padding-left:10px">
      <h3>首页</h3>
      <div class="zl-chart" id="board-post-count"></div>
      <div class="zl-chart" id="day7-post-count"></div>
  </div>
</template>

<script>
import { getCount } from '@/api/post'
import { getCountDay } from '@/api/detail'
import * as echarts from 'echarts'
export default {
  name: 'Home',
  mounted () {
    this.loadBoardPostCountChat()
    this.load7DayPostCountChat()
    this.getDay()
  },
  methods: {
    loadBoardPostCountChat () {
      getCount().then(res => {
        let data = res.data
        let chartDom = document.getElementById('board-post-count')
        let myChart = echarts.init(chartDom)
        let boardNames = []
        let postCounts = []
        let color = [
          {itemStyle: {color: '#3FB17C'}},
          {itemStyle: {color: '#5C7BD9'}},
          {itemStyle: {color: '#9FE080'}},
          {itemStyle: {color: '#FFDC60'}},
          {itemStyle: {color: '#FF915A'}}
        ]
        let option = {
          title: {
            text: '板块帖子数',
            x: 'center',
            y: 'bottom'
          },
          tooltip: {
            trigger: 'axis'
          },
          xAxis: {
            type: 'category',
            data: boardNames
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              data: postCounts,
              type: 'bar'
            }
          ]
        }
        data.forEach((v, i) => {
          boardNames.push(v.name)
          let obj = {}
          obj.value = v.count
          obj.itemStyle = color[i].itemStyle
          postCounts.push(obj)
        })
        postCounts.forEach(v => {

        })
        option && myChart.setOption(option)
      })
    },
    load7DayPostCountChat () {
      getCountDay().then(res => {
        let data = res['data']
        let dates = this.getDay(7)
        console.log(dates)
        let counts = [0, 0, 0, 0, 0, 0, 0]
        data.forEach(v => {
          var indexOf4 = (dates || []).findIndex((item) => item === v.data)
          counts[indexOf4] = v.count
          // if (dates.includes(v.data)) {
          //   counts.push(v.count)
          // } else {
          //   counts.push(0)
          // }
        })
        let chartDom = document.getElementById('day7-post-count')
        let myChart = echarts.init(chartDom)
        let option = {
          title: {
            text: '近7天帖子数',
            x: 'center',
            y: 'bottom'
          },
          tooltip: {
            trigger: 'axis'
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: dates
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              data: counts,
              type: 'line',
              areaStyle: {}
            }
          ]
        }
        option && myChart.setOption(option)
      })
    },
    getDay (days) {
      let oneDay = 24 * 60 * 60 * 1000
      let list = []
      for (let i = days - 1; i > -1; i--) {
        let day = new Date(Date.now() - i * oneDay)
        // let endTime = new Date(Date.now() - oneDay)
        day = this.formatterDate(day, 'yyyy-MM-dd')
        list.push(day)
      }
      return list
    },
    // 时间格式化
    formatterDate (date, fmt) {
      let nowDate = {
        yyyy: date.getFullYear(), // 年
        MM: date.getMonth() + 1, // 月份
        dd: date.getDate(), // 日
        hh: date.getHours(),
        mm: date.getMinutes(),
        ss: date.getSeconds()
      }
      if (/(y+)/.test(fmt)) {
        fmt = fmt.replace(RegExp.$1, (date.getFullYear() + '').substr(4 - RegExp.$1.length))
      }
      for (var k in nowDate) {
        if (new RegExp('(' + k + ')').test(fmt)) {
          fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (nowDate[k]) : (('00' + nowDate[k]).substr(('' + nowDate[k]).length)))
        }
      }
      return fmt
    }
  }

}
</script>

<style scoped>
.zl-chart{
  height: 300px;
  width: 100%;
}
h3 {
  padding: 10px;
  float: left;
}
</style>
