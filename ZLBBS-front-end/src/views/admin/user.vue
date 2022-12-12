<template>
  <div style="padding-left:10px">
    <h3>用户管理</h3>
    <el-table
        v-loading= "loading"
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="username"
          label="用户名">
        </el-table-column>
        <el-table-column
          prop="email"
          label="邮箱">
        </el-table-column>
        <el-table-column
          prop="create_time"
          label="加入时间">
        </el-table-column>
        <el-table-column
          prop="is_staff"
          label="员工">
          <template #default="scope">
            <el-tag v-if="scope.row.is_staff">是</el-tag>
            <el-tag v-else type="danger">否</el-tag>
          </template>
        </el-table-column>
        <el-table-column
          prop="is_active"
          label="状态">
          <template #default="scope">
            <el-tag v-if="scope.row.is_active" type="success">是</el-tag>
            <el-tag v-else type="danger">否</el-tag>
          </template>
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
        <span>您确定要拉黑此用户吗？</span>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="submit()">确 定</el-button>
          <el-button @click="dialogVisible = false">取 消</el-button>
        </span>
      </el-dialog>
  </div>
</template>
<script>
import { getUser, deleteUser } from '@/api/user'
import { timeFormat } from '@/utils/time'
export default {
  name: 'AdminPost',
  data () {
    return {
      tableData: [],
      dialogVisible: false,
      page: 1,
      size: 10,
      total: 0,
      id: null,
      loading: false
    }
  },
  created () {
    this.getList()
  },
  methods: {
    getList () {
      this.loading = true
      let object = {
        page: this.page,
        size: this.size
      }
      object.sort = 'time'
      getUser({...object}).then(res => {
        let data = res.data
        data.forEach(element => {
          element.create_time = timeFormat(element.create_time)
        })
        this.tableData = res.data
        this.total = res.total
      }).finally(e => {
        this.loading = false
      })
    },
    handleClick (id) {
      this.id = id
      this.dialogVisible = true
    },
    submit () {
      deleteUser(this.id).then(res => {
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
</style>
