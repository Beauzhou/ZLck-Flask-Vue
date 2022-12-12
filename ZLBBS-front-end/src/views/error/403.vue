<template>
    <div class="errPage-container">
        <el-row>
        <el-col :span="12">
            <h1 class="text-jumbo text-ginormous">
            Oops!
            </h1>
            <h2>没权限进入</h2>
        </el-col>
        </el-row>
        <el-button @click="goBack" type="primary">返回</el-button>
        <el-button @click.native="logout" type="primary">重新登录</el-button>
    </div>
</template>
<script>
export default {
  methods: {
    goBack () {
      this.$router.go(-2)
    },
    async logout () {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login`)
    }
  }
}
</script>
<style  scoped>
  .errPage-container {
    width: 800px;
    max-width: 100%;
    margin: 100px auto;
    .pan-gif {
      margin: 0 auto;
      display: block;
    }
    .pan-img {
      display: block;
      margin: 0 auto;
      width: 100%;
    }
    .text-jumbo {
      font-size: 60px;
      font-weight: 700;
      color: #484848;
    }
    .list-unstyled {
      font-size: 14px;
      li {
        padding-bottom: 5px;
      }
      a {
        color: #008489;
        text-decoration: none;
        &:hover {
          text-decoration: underline;
        }
      }
    }
  }
</style>
