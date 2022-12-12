<template>
    <div style="margin-top:10px">
        <img style="width: 10%;" src="../../img/logo.png" />
        <h1>知了传课-注册</h1>
        <div style="width:40%; margin: 0px auto;">
            <el-form ref="registerForm" :model="form" :rules="formRules" label-width="0px">
            <el-form-item label="" prop="username" style="margin-top:40px;">
              <el-row>
                <el-col :span="24">
                  <el-input v-model="form.username" placeholder="用户名" prefix-icon="el-icon-user-solid"/>
                </el-col>
              </el-row>
            </el-form-item>
            <el-form-item label="" prop="email" >
              <el-row>
                <el-col :span="24">
                  <el-input v-model="form.email" placeholder="邮箱" prefix-icon="el-icon-user-solid">
                    <template #suffix>
                      <el-button type="primary" refs="Ibutton"  @click="send()" :disabled="btnisShow">获取验证码</el-button>
                    </template>
                  </el-input>
                </el-col>
              </el-row>
            </el-form-item>
            <el-form-item label="" prop="verificationEmail">
              <el-row>
                <el-col :span="24">
                  <el-input v-model="form.verificationEmail" placeholder="邮箱验证码" prefix-icon="el-icon-lock" show-password />
                </el-col>
              </el-row>
            </el-form-item>
            <el-form-item label="" prop="password">
              <el-row>
                <el-col :span="24">
                  <el-input v-model="form.password" placeholder="密码" prefix-icon="el-icon-lock" show-password />
                </el-col>
              </el-row>
            </el-form-item>
             <el-form-item label="" prop="checkPass">
              <el-row>
                <el-col :span="24">
                  <el-input v-model="form.checkPass" placeholder="确定密码" prefix-icon="el-icon-lock" show-password
                    @keyup.enter.native="submitForm" />
                </el-col>
              </el-row>
            </el-form-item>
            <el-form-item prop="verificationCode">
              <el-row>
                <el-col :span="24">
                  <el-input v-model="form.verificationCode" placeholder="请输入验证码" clearable >
                      <template #suffix>
                        <div @click="refreshCode" >
                            <s-identify :identifyCode="identifyCode"></s-identify>
                        </div>
                      </template>
                  </el-input>
                </el-col>
              </el-row>
            </el-form-item>
            <el-form-item style="margin-top:55px;">
                <el-button type="warning" class="submitBtn" style="width:100%" @click="submitForm()">注册</el-button>
                <el-button type="primary" class="submitBtn" style="width:100%; margin: 0; margin-top: 20px;" @click="Index()">返回</el-button>
            </el-form-item>
            </el-form>
        </div>
    </div>
</template>
<script>
import { register } from '@/api/user'
import { sendEmail } from '@/api/email'
import SIdentify from '@/components/SIdentify'
export default {
  components: { SIdentify },
  data () {
    var checkEmail = (rule, value, callback) => {
      const regEmail = /^\w+@\w+(\.\w+)+$/
      if (regEmail.test(value)) {
        return callback()
      }
      callback(new Error('邮箱格式错误'))
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.form.checkPass !== '') {
          this.$refs.registerForm.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.form.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    var validateVerification = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('验证码不能为空'))
      } else if (value !== this.identifyCode) {
        callback(new Error('验证码错误，请重新输入!'))
      } else {
        callback()
      }
    }
    return {
      form: {
        email: '',
        password: '',
        verificationCode: ''
      },
      formRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { validator: checkEmail, trigger: 'blur' }
        ],
        verificationEmail: [
          { required: true, message: '请输入邮箱验证码', trigger: 'blur' }
        ],
        password: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ],
        verificationCode: [
          {validator: validateVerification, trigger: 'blur'}
        ]
      },
      btnisShow: false,
      redirect: '',
      identifyCode: '',
      identifyCodes: '1234567890abcdefjhijklinopqrsduvwxyz'
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
  mounted () {
    // 初始化验证码
    this.identifyCode = ''
    this.makeCode(this.identifyCodes, 4)
  },
  methods: {
    submitForm () {
      this.$refs['registerForm'].validate((valid) => {
        if (valid) {
          register({...this.form}).then(res => {
            this.$message.success(res.msg)
            this.$router.push({
              path: '/login'
            })
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
    // 邮件验证码
    send () {
      this.$refs['registerForm'].validateField('email', (Error) => {
        if (!Error) {
          sendEmail(this.form.email).then(res => {
            this.$message.success(res.msg + ', 30s后可重新获取验证码')
            this.btnisShow = true
            setTimeout(() => {
              this.btnisShow = false
            }, 30000)
          })
        }
      })
    },
    // 刷新验证码
    refreshCode () {
      this.identifyCode = ''
      this.makeCode(this.identifyCodes, 4)
    },
    makeCode (o, l) {
      for (let i = 0; i < l; i++) {
        this.identifyCode += this.identifyCodes[this.randomNum(0, this.identifyCodes.length)]
      }
    },
    randomNum (min, max) {
      return Math.floor(Math.random() * (max - min) + min)
    } }
}
</script>
