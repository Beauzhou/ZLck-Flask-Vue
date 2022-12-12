import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/views/main/index'
import Post from '@/views/post/index'
import Login from '@/views/login/login'
import Register from '@/views/login/register'
import Detail from '@/views/detail/index'
import ModifyInfo from '@/views/modify/index'
import CmsMain from '@/views/admin/main'
import cmsBanner from '@/views/admin/banner'
import CmsComment from '@/views/admin/comment'
import CmsUser from '@/views/admin/user'
import CmsPost from '@/views/admin/post'
import Error403 from '@/views/error/403'
import Error404 from '@/views/error/404'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Main,
      meta: {
        roles: ['0', '1']
      }
    },
    {
      path: '/post',
      name: 'post',
      component: Post,
      meta: {
        roles: ['0', '1']
      }
    },
    {
      path: '/detail',
      name: 'detail',
      component: Detail,
      meta: {
        roles: ['0', '1']
      }
    },
    {
      path: '/modifyInfo',
      name: 'modifyInfo',
      component: ModifyInfo,
      meta: {
        roles: ['0', '1']
      }
    },
    {
      path: '/403',
      name: '403',
      meta: {
        roles: ['0', '1']
      },
      component: Error403
    },
    {
      path: '/404',
      name: '404',
      meta: {
        roles: ['0', '1']
      },
      component: Error404
    },
    {
      path: '/cms/index',
      name: 'CmsIndex',
      meta: {
        roles: ['1']
      },
      component: CmsMain
    },
    {
      path: '/cms/banner',
      name: 'CmsBanner',
      component: cmsBanner,
      meta: {
        roles: ['1']
      }
    },
    {
      path: '/cms/post',
      name: 'cmsPost',
      component: CmsPost,
      meta: {
        roles: ['1']
      }
    },
    {
      path: '/cms/comment',
      name: 'CmsComment',
      component: CmsComment,
      meta: {
        roles: ['1']
      }
    },
    {
      path: '/cms/user',
      name: 'CmsUser',
      component: CmsUser,
      meta: {
        roles: ['1']
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        roles: ['0', '1']
      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        roles: ['0', '1']
      }
    }
  ]
})
