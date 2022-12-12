<template>
    <div>
        <el-header class="header">
        <a href="/" class="brand"><strong>知了</strong>管理系统</a>
        <div class="header-content">
          <div class="greet">欢迎，{{username}} [管理员] </div>
          <div class="signout" @click="index()">回到首页</div>
        </div>
      </el-header>
        <el-col style="width:200px">
            <el-menu
            router
            default-active="/cms/index"
            background-color="#545c64"
            class="el-menu-vertical-demo">
            <el-menu-item index="/cms/index">
                <i class="el-icon-menu"></i>
                <span slot="title">首页</span>
            </el-menu-item>
            <el-menu-item index="/cms/banner">
                <i class="el-icon-document"></i>
                <span slot="title">轮播图管理</span>
            </el-menu-item>
            <el-menu-item index="/cms/post">
                <i class="el-icon-document"></i>
                <span slot="title">帖子管理</span>
            </el-menu-item>
            <el-menu-item index="/cms/comment">
                <i class="el-icon-document"></i>
                <span slot="title">评论管理</span>
            </el-menu-item>
            <el-menu-item index="/cms/user">
                <i class="el-icon-document"></i>
                <span slot="title">用户管理</span>
            </el-menu-item>
            </el-menu>
        </el-col>
    </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters(['username'])
  },
  methods: {
    index () {
      this.$router.push({
        path: '/'
      })
    }
  }
}
</script>
<style scoped>
.el-menu-item {
    height: 56px;
    line-height: 56px;
    font-size: 14px;
    color: #ffffff;
    padding: 0 20px;
    list-style: none;
    cursor: pointer;
    position: relative;
    -webkit-transition: border-color .3s,background-color .3s,color .3s;
    transition: border-color .3s,background-color .3s,color .3s;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    white-space: nowrap;
}
.el-menu.el-menu--horizontal {
    background: #00a65a;
    border-bottom: solid 1px #e6e6e6;
}
.el-menu.el-menu--horizontal :hover{
    background: #00a65a;
    border-bottom: solid 1px #e6e6e6;
    color: #ffffff;
}
.el-col-4 {
    background: rgb(20, 250, 174);
    width: 16.66667%;
    color: #ffffff;
    /* text-align: center; */
}
.el-menu-demo {
    background: #00a65a;
}
.el-menu-demo :hover {
    background: #00a65a;
}
.el-menu-demo :focus {
    background: #00a65a;
}
.el-menu-vertical-demo {
    height: 90vh;
}
.focus :focus{
    background: #00a65a;
}
.header {
  height: 60px;
  background: #00a65a;
  display: flex;
}

.header .brand {
  width: 200px;
  margin-left: -20px;
  background-color: #008d4c;
  font-size: 20px;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}
.header .header-content {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: 20px;
  color: #fff;
}

.header-content .signout {
    cursor: pointer;
  }
</style>
