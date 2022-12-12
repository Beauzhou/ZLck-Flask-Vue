<template>
    <div style="text-align: initial">
        <div class="post-container">
            <h2> {{data.title}}</h2>
            <p class="post-info-group">
                <span> 发表时间： {{data.create_time}} </span>
                <span> 作者： {{data.username}} </span>
                <span> 所属模块： {{data.name}} </span>
                <span> 评论数： {{data.name}} </span>
            </p>
            <div v-html= "data.content"></div>
        </div>
        <div class="comment-group">
          <h3>评论列表</h3>
          <div>
            <div v-for="(item,index) in comment"  :key="index" class="comment-list-group">
                  <p style=" margin-top: 10px; font-size: 12px;  color: rgb(140, 140, 140); margin-bottom:10px"> {{item.username}}  {{item.create_time}} </p>
                  <p class="comment-txt"> {{item.content}} </p>
              </div>
          </div>
        </div>
        <div class="add-comment-group">
          <h3>发表评论</h3>
          <el-input
            type="textarea"
            :autosize="{ minRows: 2}"
            v-model="content">
          </el-input>
          <el-button style="margin-top:10px" type="primary" @click="submit()">发表评论</el-button>
        </div>
    </div>
</template>

<script>
import { getDetail, addComment } from '@/api/detail'
import { timeFormat } from '@/utils/time'
import { getToken } from '@/utils/auth'
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters(['userInfo'])
  },
  data () {
    return {
      id: '',
      data: {},
      comment: [],
      content: null
    }
  },
  watch: {
    $route: {
      handler: function (route) {
        let id = decodeURIComponent(route.fullPath).split('id=')[1]
        this.id = id
      },
      immediate: true
    }
  },
  created () {
    this.getList()
  },
  methods: {
    getList () {
      getDetail(this.id).then(res => {
        let data = res.data
        data.create_time = timeFormat(data.create_time)
        this.data = data
        data.comment.forEach(v => {
          v.create_time = timeFormat(v.create_time)
        })
        this.comment = res.data.comment
      })
    },
    submit () {
      if (!getToken()) {
        this.$router.push(`/login?redirect=${this.$route.fullPath}`)
      } else {
        let obj = {}
        obj.content = this.content
        obj.post_id = this.id
        obj.author_id = this.userInfo.id
        addComment({...obj}).then(res => {
          this.$message.success(res.data)
          this.getList()
        })
      }
    }
  }
}
</script>

<style scoped>
.post-container {
    border-width: 1px;
    border-style: solid;
    border-color: rgb(230, 230, 230);
    border-image: initial;
    padding: 10px;

}
.post-info-group {
    font-size: 12px;
    color: rgb(140, 140, 140);
    margin-top: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgb(230, 230, 230);
}
.comment-group {
    margin-top: 20px;
    border-width: 1px;
    border-style: solid;
    border-color: rgb(232, 232, 232);
    border-image: initial;
    padding: 10px;
}
.add-comment-group {
    margin-top: 20px;
    padding: 10px;
    border-width: 1px;
    border-style: solid;
    border-color: rgb(232, 232, 232);
    border-image: initial;
}
.comment-list-group  {
    overflow: hidden;
    padding: 10px 0;
    border-bottom: 1px solid #e8e8e8;
}
.comment-content {
    float: left;
    margin-left: 10px;
}
.comment-content .comment-txt {
    margin-top: 10px;
}
</style>
