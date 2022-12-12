<template>
  <el-menu :default-active="$route.path" router class="el-menu-demo" mode="horizontal" background-color="#f8f8f8">
    <el-menu-item index="/" style="font-size: 18px;">知了传课Python论坛</el-menu-item>
    <el-menu-item class="inputHover">
      <el-input v-model="input"/>
      <el-button @click="search()">搜索</el-button>
    </el-menu-item>
    <el-menu-item v-if="!username" style="float:right" index="/register">注册</el-menu-item>
    <el-menu-item v-if="!username" style="float:right" index="/login">登录</el-menu-item>
    <el-submenu v-if="username" style="float: right" index="100">
      <template  slot="title">{{ username }}</template>
      <el-menu-item @click.native="adminPage()" v-if="userInfo.is_staff === 1">管理页面</el-menu-item>
      <el-menu-item @click.native="setting()" >设置</el-menu-item>
      <el-menu-item @click.native="logout">退出</el-menu-item>
    </el-submenu>
  </el-menu>
</template>
<script>
import Cookies from 'js-cookie'
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters(['username']),
    ...mapGetters(['userInfo'])
  },
  data () {
    return {
      input: ''
    }
  },
  created () {
  },
  methods: {
    search () {
      Cookies.set('content', this.input)
      window.location.href = '/'
    },
    adminPage () {
      this.$router.push({
        path: '/cms/index'
      })
    },
    async logout () {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    },
    setting () {
      this.$router.push({
        path: '/modifyInfo'
      })
    }
  }
}

</script>
<style scoped>
.icon{
  margin-left: 70%;
}
.el-menu-item:hover{
  background-color: #F8F8F8 !important;
    /* text-decoration: underline; */
}
.el-menu--horizontal>.el-menu-item.is-active {
    /* border-bottom: 2px solid #409EFF; */
    color: #303133;
}
</style>
