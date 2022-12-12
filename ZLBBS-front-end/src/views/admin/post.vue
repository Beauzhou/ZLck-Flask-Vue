<template>
  <div style="padding-left:10px">
    <h3>帖子管理</h3>
    <el-table
        v-loading= "loading"
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="title"
          label="标题">
        </el-table-column>
        <el-table-column
          prop="create_time"
          label="发布时间">
        </el-table-column>
        <el-table-column
          prop="name"
          label="所属模块">
        </el-table-column>
        <el-table-column
          prop="username"
          label="作者">
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
      <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="page"
            :page-sizes="[10, 20, 30, 40]"
            :page-size="size"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total">
      </el-pagination>
      <el-dialog
        title="提示"
        :visible.sync="dialogVisible"
        width="30%">
        <span>如果删除帖子，该帖子下所有的评论也会被删除，您确定要删除吗？</span>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="submit()">确 定</el-button>
          <el-button @click="dialogVisible = false">取 消</el-button>
        </span>
      </el-dialog>
  </div>
</template>
<script>
import { getPost, deletePost } from '@/api/post'
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
      getPost({...object}).then(res => {
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
    handleSizeChange (v) {
      this.size = v
      this.page = 1
      this.getList()
    },
    handleCurrentChange (v) {
      this.page = v
      this.size = 10
      this.getList()
    },
    handleClick (id) {
      this.id = id
      this.dialogVisible = true
    },
    submit () {
      deletePost(this.id).then(res => {
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
