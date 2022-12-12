<template>
    <div>
        <h1>发布帖子</h1>
        <el-form ref="form" :model="form" label-width="80px" :rules="rules">
            <el-form-item label="标题" prop="title">
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="模块" prop="board_id">
                <el-select v-model="form.board_id" placeholder="请选择模块" style="width:100%">
                <el-option label="Python" value=1></el-option>
                <el-option label="Flask" value=2></el-option>
                <el-option label="Django" value=3></el-option>
                <el-option label="爬虫" value=4></el-option>
                <el-option label="前端" value=5></el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
              <quill-editor
                v-model="form.content"
                ref="myQuillEditor"
                :options="editorOption">
              </quill-editor>
            </el-form-item>
        </el-form>
        <el-button @click="submit()" style="margin-top:22px;text-align:center" type="danger">发布帖子</el-button>
    </div>
</template>

<script>
import { addPost } from '@/api/post'
import { getToken } from '@/utils/auth'
import { mapGetters } from 'vuex'
import { quillEditor } from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
export default {
  components: {
    quillEditor
  },
  computed: {
    ...mapGetters(['userInfo'])
  },
  data () {
    return {
      form: {
        content: '',
        title: '',
        board_id: '',
        author_id: ''
      },
      rules: {
        title: [
          { required: true, message: '请输入标题', trigger: 'blur' }
        ],
        board_id: [
          { required: true, message: '请选择模块', trigger: 'change' }
        ],
        centent: [
          { required: true, message: '请选择活动区域', trigger: 'blur' }
        ]
      },
      editorOption: {
        placeholder: '请输入...',
        modules: {
          toolbar: [
            ['bold', 'italic', 'underline', 'strike'], // toggled buttons
            ['blockquote', 'code-block'],
            [{'header': 1}, {'header': 2}], // custom button values
            [{'list': 'ordered'}, {'list': 'bullet'}],
            [{'script': 'sub'}, {'script': 'super'}], // superscript/subscript
            [{'indent': '-1'}, {'indent': '+1'}], // outdent/indent
            [{'size': ['small', false, 'large', 'huge']}], // custom dropdown
            [{'header': [1, 2, 3, 4, 5, 6, false]}],
            [{'color': []}, {'background': []}], // dropdown with defaults from theme
            [{'font': []}],
            [{'align': []}]
          ]
        }
      }
    }
  },
  created () {
    if (!getToken()) {
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    }
  },
  methods: {
    submit () {
      console.log(this.$refs.form)
      this.form.author_id = this.userInfo.id
      this.$refs['form'].validate((valid) => {
        if (valid) {
          addPost(this.form).then(res => {
            this.$message({
              message: res.msg,
              type: 'success'
            })
            this.$router.push('/')
          })
        } else {
          return false
        }
      })
    }
  }
}
</script>
<style>
.ql-snow .ql-picker.ql-size .ql-picker-label::before,
.ql-snow .ql-picker.ql-size .ql-picker-item::before {
  content: "14px";
}

.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="small"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="small"]::before {
  content: "10px";
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="large"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="large"]::before {
  content: "18px";
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value="huge"]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value="huge"]::before {
  content: "32px";
}

.ql-snow .ql-picker.ql-header .ql-picker-label::before,
.ql-snow .ql-picker.ql-header .ql-picker-item::before {
  content: "文本";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="1"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="1"]::before {
  content: "标题1";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="2"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="2"]::before {
  content: "标题2";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="3"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="3"]::before {
  content: "标题3";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="4"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="4"]::before {
  content: "标题4";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="5"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="5"]::before {
  content: "标题5";
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="6"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="6"]::before {
  content: "标题6";
}

.ql-snow .ql-picker.ql-font .ql-picker-label::before,
.ql-snow .ql-picker.ql-font .ql-picker-item::before {
  content: "标准字体";
}
.ql-snow .ql-picker.ql-font .ql-picker-label[data-value="serif"]::before,
.ql-snow .ql-picker.ql-font .ql-picker-item[data-value="serif"]::before {
  content: "衬线字体";
}
.ql-snow .ql-picker.ql-font .ql-picker-label[data-value="monospace"]::before,
.ql-snow .ql-picker.ql-font .ql-picker-item[data-value="monospace"]::before {
  content: "等宽字体";
}
</style>
