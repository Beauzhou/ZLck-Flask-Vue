<template>
  <div style="padding-left:10px">
    <h3>轮播图管理</h3>
    <div>
      <el-button type="primary" style="float:right" @click="add()"><i class="el-icon-plus" /> 添加轮播图</el-button>
    </div>
    <el-table
      v-loading= "loading"
      :data="imgData"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="名称">
      </el-table-column>
      <el-table-column
        prop="imgFile"
        label="图片">
        <template #default="scope">
            <!-- <p :src="scope.row.create_time"/> -->
            <img :src="scope.row.imgUrl" style="width:150px;height:150px"/>
        </template>
      </el-table-column>
      <el-table-column
        prop="priority"
        label="优先级">
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="100">
        <template #default="scope">
          <el-button
            type="danger"
            size="mini"
            circle
            @click="handleClick(scope.row.id)"
          >
            <i class="el-icon-delete"></i>
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="30%">
      <span>您确定要删除轮播图吗？</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submit()">确 定</el-button>
        <el-button @click="dialogVisible = false">取 消</el-button>
      </span>
    </el-dialog>
    <el-dialog
      title="添加轮播图"
      :visible.sync="bannergVisible"
      width="30%">
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="名称" prop="name">
          <el-input v-model="form.name" disabled></el-input>
        </el-form-item>
        <el-form-item label="优先级" prop="priority">
          <el-input v-model="form.priority" autocomplete="off" type="number"></el-input>
        </el-form-item>
          <el-form-item label="图片上传">
          <el-upload
            class="avatar-uploader"
            action="/dev-api/file/upload"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitBanner()">确 定</el-button>
        <el-button @click="bannergVisible = false">取 消</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import { getBanner, addBanner, deleteBanner } from '@/api/banner'
import { download } from '@/api/file'
export default {
  name: 'AdminBanner',
  data () {
    return {
      tableData: [],
      imgData: [],
      dialogVisible: false,
      bannergVisible: false,
      imageUrl: '',
      id: null,
      loading: false,
      form: {
        img_url: ''
      },
      rules: {
        name: [
          { required: true, message: '请上传图片', trigger: 'blur' }
        ],
        priority: [
          { required: true, message: '请输入优先级', trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.getList()
  },
  methods: {
    getList () {
      getBanner().then(res => {
        this.tableData = res.data
        this.getImg()
      })
    },
    getImg () {
      let data = []
      this.tableData.forEach(v => {
        let result = this.getAxios(v.name)
        data.push(result)
      })

      Promise.all(data).then(res => {
        this.$nextTick(() => {
          console.log(res)
          this.tableData.forEach((v, i) => {
            v.imgUrl = res[i]
          })
          this.imgData = this.tableData
        })
      })
    },
    getAxios (v) {
      return new Promise(function (resolve, reject) {
        download(v).then(res => {
          let blob = new Blob([res], {
            type: 'image/jpeg'
          })
          const imageUrl = URL.createObjectURL(blob)
          resolve(imageUrl)
        })
      })
    },
    add () {
      this.bannergVisible = true
    },
    handleAvatarSuccess (res, file) {
      this.form.name = res.fileName
      this.form.image_url = res.fileUrl
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传图像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    handleClick (id) {
      this.id = id
      this.dialogVisible = true
    },
    submitBanner () {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          addBanner({...this.form}).then(res => {
            this.$message.success(res.msg)
            this.bannergVisible = false
          }).finally(e => {
            this.getList()
          })
        } else {
          return false
        }
      })
    },
    submit () {
      deleteBanner(this.id).then(res => {
        this.$message.success(res.msg)
        this.getList()
      }).finally(e => {
        this.dialogVisible = false
      })
    }
  }
}
</script>
<style scoped>
h3 {
  padding: 10px;
  float: left;
}
.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
