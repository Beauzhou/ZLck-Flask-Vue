<template>
  <div style="padding-left:10px">
    <h3>评论管理</h3>
    <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="content"
          label="内容">
        </el-table-column>
        <el-table-column
          prop="username"
          label="作者">
        </el-table-column>
        <el-table-column
          prop="create_time"
          label="发布时间">
        </el-table-column>
        <el-table-column
          prop="post_content"
          label="所属模块">
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
          <!-- <template slot-scope="scope">
            <el-button @click="handleClick(scope.row.id)" type="text" size="small">查看</el-button>
          </template> -->
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
        width="30%"
        :before-close="handleClose">
        <span>您确定要删除这个评论吗？</span>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="handleDelete()">确 定</el-button>
          <el-button @click="dialogVisible = false">取 消</el-button>
        </span>
      </el-dialog>
  </div>
</template>
<script>
import { getComment, deleteComment } from '@/api/detail'
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
      deleteId: undefined
    }
  },
  created () {
    this.getList()
  },
  methods: {
    getList () {
      let object = {
        page: this.page,
        size: this.size
      }
      getComment({...object}).then(res => {
        let data = res.data
        data.forEach(element => {
          // 去掉所有的html标记
          element.post_content = element.post_content.replace(/<[^>]+>/g, '')
          // 去掉所有的空格
          element.post_content = element.post_content.replace(/&nbsp;/ig, '')
          element.create_time = timeFormat(element.create_time)
        })
        this.tableData = res.data
        this.total = res.total
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
      this.dialogVisible = true
      this.deleteId = id
    },
    handleDelete () {
      deleteComment(this.deleteId).then(res => {
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
