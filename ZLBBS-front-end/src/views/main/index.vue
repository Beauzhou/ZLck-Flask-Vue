<template>
<div>
    <div class="left-main">
        <el-carousel v-loading="loading" height="270px">
            <el-carousel-item v-for="(item,index) in imgList" :key="index">
            <h3 class="small">
              <img :src="item.imgUrl"/>
            </h3>
            </el-carousel-item>
        </el-carousel>
        <div class="post-group" v-loading="postLoading">
            <el-radio-group v-model="radio1" style="float:left" @change="getList()">
                <el-radio-button label="最新" ></el-radio-button>
                <el-radio-button label="评论最多"></el-radio-button>
            </el-radio-group>
              <div  style="clear:both; float:left; padding-top:15px; border-bottom: 1px solid rgb(230, 230, 230);" v-for="(item,index) in avatarList"  :key="index">
                <div class="author-avatar-group">
                  <img :src="item.imgUrl" style="width:50px;height:50px"/>
                </div>
                <div class="post-info-group">
                  <el-link @click="detail(item.id)">{{item.title}} </el-link>
                  <p style=" margin-top: 10px; font-size: 12px;  color: rgb(140, 140, 140)"> 作者: {{item.username}}   发表时间： {{item.create_time}}  评论：{{item.number}} </p>
                </div>
            </div>
        </div>
    </div>
    <div class="right-main">
        <el-button @click="post()" style="width:100%; margin-bottom: 10px" type="warning">发布帖子</el-button>
        <el-button style="width:100%; margin-left:0px" type="primary" @click="category()">所有板块</el-button>
        <el-button style="width:100%; margin-left:0px" @click="category(1)">Python</el-button>
        <el-button style="width:100%; margin-left:0px" @click="category(2)">Flask</el-button>
        <el-button style="width:100%; margin-left:0px" @click="category(3)">Django</el-button>
        <el-button style="width:100%; margin-left:0px" @click="category(4)">爬虫</el-button>
        <el-button style="width:100%; margin-left:0px" @click="category(5)">前端</el-button>
    </div>
</div>
</template>
<script>
import Cookies from 'js-cookie'
import { download } from '@/api/file'
import { getBanner } from '@/api/banner'
import { timeFormat } from '@/utils/time'
import { getPost } from '@/api/post'
export default {
  name: 'SidebarItem',
  data () {
    return {
      radio1: '最新',
      list: [],
      type: null,
      imgList: [],
      avatarList: [],
      loading: true,
      postLoading: true
    }
  },
  created () {
    this.getBannerList()
    this.getList()
  },
  methods: {
    getList () {
      this.postLoading = true
      let object = {
        type: this.type,
        page: 1,
        size: 99999999999
      }
      let content = Cookies.get('content')
      if (content) {
        object.content = content
        Cookies.remove('content')
      }
      if (this.radio1 === '最新') {
        object.sort = 'time'
      }
      if (this.radio1 === '评论最多') {
        object.sort = 'number'
      }
      getPost({...object}).then(res => {
        let data = res.data
        data.forEach(element => {
          element.create_time = timeFormat(element.create_time)
        })
        this.list = res.data
        if (this.list.length !== 0) {
          this.getAvatar(this.list)
        }
      }).finally(e => {
        this.postLoading = false
      })
    },
    getBannerList () {
      this.loading = true
      getBanner().then(res => {
        this.tableData = res.data
        if (this.tableData.length !== 0) {
          this.getImg()
        }
      }).finally(e => {
        this.loading = false
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
          this.imgList = this.tableData
        })
      })
    },
    getAvatar (imgdata) {
      let data = []
      imgdata.forEach(v => {
        console.log(v)
        if (v.avatar) {
          let result = this.getAxios(v.avatar)
          data.push(result)
        }
      })
      Promise.all(data).then(res => {
        this.$nextTick(() => {
          imgdata.forEach((v, i) => {
            v.imgUrl = res[i]
          })
          this.avatarList = imgdata
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
    getAxios1 (v) {
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
    category (id) {
      this.type = id
      this.getList()
    },
    post () {
      this.$router.push('/post')
    },
    detail (id) {
      this.$router.push({
        path: '/detail',
        query: {
          id: id
        }
      })
    }
  }
}
</script>
<style>
  /* .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  } */
.author-avatar-group {
  float: left;
}
.post-info-group {
  float: left;
  margin-left: 10px;
  border-bottom: 1px solid #e6e6e6;
  /* width: 85%; */
  padding-bottom: 10px;
}
.left-main {
  width: 70%;
  float: left;
}
.right-main {
  width: 28%;
  float: right;
}
.post-group {
  border: 1px solid #ddd;
  margin-top: 20px;
  overflow: hidden;
  border-radius: 5px;
  padding: 10px
}
</style>
