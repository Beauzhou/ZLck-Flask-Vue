<template>
    <div>
        <h2 > {{username}} 设置 </h2>
        <el-form ref="form" :model="form"  style="margin-top:10px" label-width="80px">
            <el-form-item label="邮箱">
                <el-input v-model="form.email" :disabled=true></el-input>
            </el-form-item>
            <el-form-item label="头像">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <el-upload
                    style="float:left"
                    action="/dev-api/file/upload"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
                    <!-- <i class="el-icon-plus avatar-uploader-icon"></i>
                     -->
                     <el-button size="small" type="primary">点击上传</el-button>
                </el-upload>
            </el-form-item>
            <el-form-item label="个性签名">
                <el-input v-model="form.signature" ></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit()">更新</el-button>
                <el-button @click="Index()">取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
<script>
import { mapGetters } from 'vuex'
import { download } from '@/api/file'
import { getUserById, updateUser } from '@/api/user'
export default {
  computed: {
    ...mapGetters(['username']),
    ...mapGetters(['userInfo'])
  },
  created () {
    this.getUser()
  },
  data () {
    return {
      form: {
        email: '',
        signature: '',
        avatar: ''
      },
      imageUrl: undefined
    }
  },
  methods: {
    getUser () {
      getUserById(this.userInfo.id).then(res => {
        this.form.email = res.msg.email
        this.form.signature = res.msg.signature
        this.form.avatar = res.msg.avatar
        this.form.id = res.msg.id
        if (res.msg.avatar) {
          download(res.msg.avatar).then(res => {
            let blob = new Blob([res], {
              type: 'image/jpeg'
            })
            const imageUrl = URL.createObjectURL(blob)
            this.imageUrl = imageUrl
          })
        }
      })
    },
    onSubmit () {
      updateUser({...this.form}).then(res => {
        this.$message.success(res.msg)
      }).finally(e => {
        this.getUser()
      })
    },
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
      this.form.avatar = res.fileName
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    Index () {
      this.$router.push({
        path: '/'
      })
    }
  }
}
</script>
<style scoped>
.avatar {
    width: 178px;
    height: 178px;
    display: block;
}
</style>
