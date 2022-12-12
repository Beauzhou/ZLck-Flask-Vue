<template>
  <div>
    <div class="error">
      <div class="error-code">4<span>0</span>4</div>
      <div class="error-desc">页面不存在</div>
      <div class="error-handle">
        <el-button type="primary" size="large" @click="goBack">返回</el-button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    goBack () {
      this.$router.go(-2)
    }
  }
}
</script>

<style scoped>
    .error {
        text-align: center;
    }
    .error-code{
        line-height: 1;
        font-size: 250px;
        font-weight: bolder;
        color: #2d8cf0;
        animation: myfirst 1s infinite;
    }
    .error-code span{
        color: #00a854;
    }
    .error-desc{
        font-size: 30px;
        color: #777;
    }
    .error-handle{
        margin-top: 30px;
        padding-bottom: 200px;
    }
    .error-btn{
        margin-left: 100px;
    }
</style>
