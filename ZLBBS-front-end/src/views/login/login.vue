<template>
    <div style="margin-top:10px">
        <img style="width: 10%;" src="../../img/logo.png" />
        <h1>知了传课-登录</h1>
        <div style="width:40%; margin: 0px auto;">
            <el-form ref="loginForm" :model="form" :rules="formRules" label-width="0px">
            <el-form-item label="" prop="userName" style="margin-top:40px;">
              <el-row>
                <el-col :span="24">
                  <el-input v-model="form.email" placeholder="email" prefix-icon="el-icon-user-solid"
                    @keyup.enter.native="submitForm" />
                </el-col>
              </el-row>
            </el-form-item>
            <el-form-item label="" prop="password">
              <el-row>
                <el-col :span="24">
                  <el-input v-model="form.password" placeholder="password" prefix-icon="el-icon-lock" show-password
                    @keyup.enter.native="submitForm" />
                </el-col>
              </el-row>
            </el-form-item>
            <el-checkbox v-model="checked" style="float: left">记住我</el-checkbox>
            <el-form-item style="margin-top:55px;">
                <el-button type="warning" class="submitBtn" style="width:100%" @click="submitForm">登录</el-button>
                <el-button type="primary" class="submitBtn" style="width:100%; margin: 0; margin-top: 20px;" @click="Index()">返回</el-button>
            </el-form-item>
            </el-form>
            <el-link style="float: left" type="primary" @click="register()"> 没有账号? 立即注册 </el-link>
            <el-link style="float: right" type="primary"> 找回密码 </el-link>
        </div>
    </div>
</template>
<script>
export default {
  data () {
    return {
      form: {
        email: '',
        password: ''
      },
      formRules: {},
      redirect: '',
      checked: false
    }
  },
  watch: {
    $route: {
      handler: function (route) {
        let redirectPath = decodeURIComponent(route.fullPath).split('redirect=')[1]
        this.redirect = redirectPath
      },
      immediate: true
    }
  },
  methods: {
    submitForm () {
      this.$refs['loginForm'].validate((valid) => {
        if (valid) {
          this.loading = true
          this.$store.dispatch('user/login', this.form).then(() => {
            console.log(this.redirect)
            if (!this.redirect) {
              this.$router.push({
                path: '/'
              })
            } else {
              this.$router.push({
                path: this.redirect
              })
            }
          }).finally(e => {
            this.loading = false
            this.form = {}
          })
        } else {
          return false
        }
      })
    },
    Index () {
      this.$router.push({
        path: '/'
      })
    },
    register () {
      this.$router.push({
        path: '/register'
      })
    }
  }

}
</script>
